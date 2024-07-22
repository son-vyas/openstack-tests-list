import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_skipped_tests(file_path):
    data = load_yaml(file_path)
    skipped_tests = {}
    for failure in data.get('known_failures', []):
        test = failure['test']
        deployment = failure['deployment']
        releases = failure['releases']
        jobs = failure['jobs']
        skipped_tests[test] = {'deployment': deployment, 'releases': releases, 'jobs': jobs}
    return skipped_tests
