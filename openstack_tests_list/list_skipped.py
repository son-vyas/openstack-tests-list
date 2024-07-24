import yaml
import os


def load_yaml(file_path):
    """Load a YAML file and return its content."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def get_skipped_tests(file_path):
    """Parse the skiplist YAML file and return a dictionary of skipped tests."""
    data = load_yaml(file_path)
    skipped_tests = {}
    for failure in data.get("known_failures", []):
        test = failure["test"]
        deployment = failure["deployment"]
        releases = failure["releases"]
        jobs = failure["jobs"]
        skipped_tests[test] = {
            "deployment": deployment,
            "releases": releases,
            "jobs": jobs,
        }
    return skipped_tests


class ListSkippedYaml:
    def __init__(self, file_path=None, base_dir="openstack_tests_list/default"):
        self.file = (
            file_path if file_path else os.path.join(base_dir, "list_skipped.yaml")
        )

    def parse(self):
        return get_skipped_tests(self.file)
