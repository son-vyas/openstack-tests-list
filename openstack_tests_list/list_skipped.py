import yaml
import os


def load_yaml(file_path):
    """Load a YAML file and return its content."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def merge_lists(default_data, component_data):
    """Merge component-specific skiplist with the default skiplist ensuring unique test entries per job."""
    if not component_data:
        return default_data

    # Build a dictionary where each key is a job and each value is a set of tests
    job_to_tests = {}

    # Helper function to add tests to the job mapping
    def add_tests_to_job(test_entry):
        for job in test_entry["jobs"]:
            if job not in job_to_tests:
                job_to_tests[job] = set()
            job_to_tests[job].add(test_entry["test"])

    # Process default and component data to fill job_to_tests
    for entry in default_data.get("known_failures", []):
        add_tests_to_job(entry)
    for entry in component_data.get("known_failures", []):
        add_tests_to_job(entry)

    # Reconstruct the known_failures list ensuring unique tests per job
    unique_failures = []
    for job, tests in job_to_tests.items():
        for test in tests:
            # Find or create the failure entry for this job
            found = False
            for failure in unique_failures:
                if test == failure["test"]:
                    if job not in failure["jobs"]:
                        failure["jobs"].append(job)
                    found = True
                    break
            if not found:
                unique_failures.append(
                    {
                        "test": test,
                        "jobs": [job],
                        # 'deployment' and 'releases' could be generalized if needed
                    }
                )

    return {"known_failures": unique_failures}


def get_skipped_tests(base_dir, component=None):
    """Fetch and merge the skipped tests based on default and component-specific settings."""
    default_file = os.path.join(base_dir, "list_skipped.yaml")
    default_data = load_yaml(default_file)
    if component:
        component_file = os.path.join(
            base_dir, "..", "components", component, "list_skipped.yaml"
        )
        if os.path.exists(component_file):
            component_data = load_yaml(component_file)
            return merge_lists(default_data, component_data)
    return default_data


class ListSkippedYaml:
    def __init__(self, component=None):
        base_dir = "openstack_tests_list/default"
        self.data = get_skipped_tests(base_dir, component=component)

    def parse(self):
        """Return the merged skipped tests."""
        return self.data
