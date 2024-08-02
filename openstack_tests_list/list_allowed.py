import yaml
import os


def load_yaml(file_path):
    """Load YAML file from the given path and return the data."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def merge_lists(default_data, component_data):
    """Merge component-specific allowlist into the default allowlist by group name."""
    if not component_data:
        return default_data

    # Transform default data into a dictionary for easier manipulation
    default_groups = {group["name"]: group for group in default_data.get("groups", [])}

    for comp_group in component_data.get("groups", []):
        comp_name = comp_group["name"]
        if comp_name in default_groups:
            # Merge tests in existing group
            existing_group = default_groups[comp_name]
            existing_group["tests"] = list(
                set(existing_group["tests"]) | set(comp_group["tests"])
            )
            # Optionally merge other attributes like 'releases' if needed
            existing_group["releases"] = list(
                set(existing_group["releases"]) | set(comp_group["releases"])
            )
        else:
            # Add new group from component if not found in the default
            default_data["groups"].append(comp_group)

    return default_data


def get_allowed_tests(base_dir, component=None):
    """Fetch and merge the allowed tests based on default and component-specific settings."""
    default_file = os.path.join(base_dir, "list_allowed.yaml")
    default_data = load_yaml(default_file)
    if component:
        component_file = os.path.join(
            base_dir, "..", "components", component, "list_allowed.yaml"
        )
        if os.path.exists(component_file):
            component_data = load_yaml(component_file)
            return merge_lists(default_data, component_data)
    return default_data


class ListAllowedYaml:
    def __init__(self, component=None):
        base_dir = "openstack_tests_list/default"
        self.data = get_allowed_tests(base_dir, component=component)

    def parse(self):
        """Return the merged allowed tests."""
        return self.data
