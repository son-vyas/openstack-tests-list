import yaml
import validators


class ValidateYaml:
    def __init__(self, file):
        self.file = file

    def take_action(self):
        with open(self.file, "r") as yaml_file:
            try:
                content = yaml.safe_load(yaml_file)
            except yaml.YAMLError as e:
                print(f"Error parsing YAML file: {e}")
                return

        if "known_failures" in content:
            self.validate_skiplist(content["known_failures"])
        elif "groups" in content:
            self.validate_allowlist(content["groups"])
        else:
            print("Invalid format: Missing 'known_failures' or 'groups' key")

    def validate_skiplist(self, skiplist):
        for item in skiplist:
            if "test" not in item:
                print(f"Invalid skiplist item: {item}")

    def validate_allowlist(self, allowlist):
        for group in allowlist:
            if "name" not in group or "tests" not in group:
                print(f"Invalid allowlist group: {group}")
