import yaml


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def get_allowed_tests(file_path):
    data = load_yaml(file_path)
    allowed_tests = {}
    for group in data.get("groups", []):
        name = group["name"]
        tests = group["tests"]
        releases = group["releases"]
        allowed_tests[name] = {"tests": tests, "releases": releases}
    return allowed_tests
