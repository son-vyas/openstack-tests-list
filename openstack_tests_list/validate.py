import yaml
from cliff.command import Command
import validators

class Validate(Command):
    def take_action(self, parsed_args):
        with open(parsed_args.file, 'r') as yaml_file:
            try:
                content = yaml.safe_load(yaml_file)
            except yaml.YAMLError as e:
                self.app.log.error(f"Error parsing YAML file: {e}")
                return

        if 'known_failures' in content:
            self.validate_skiplist(content['known_failures'])
        elif 'groups' in content:
            self.validate_allowlist(content['groups'])
        else:
            self.app.log.error("Invalid format: Missing 'known_failures' or 'groups' key")

    def validate_skiplist(self, skiplist):
        for item in skiplist:
            if 'test' not in item or not validators.url(item.get('lp', '')):
                self.app.log.error(f"Invalid skiplist item: {item}")

    def validate_allowlist(self, allowlist):
        for group in allowlist:
            if 'name' not in group or 'tests' not in group:
                self.app.log.error(f"Invalid allowlist group: {group}")
