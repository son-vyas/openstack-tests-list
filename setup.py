from setuptools import setup, find_packages

setup(
    name='openstack-tests-list',
    version='0.1.0',
    description='Tool to manage Tempest tests viz. skiplists and allowlists',
    author='Soniya Vyas',
    author_email='svyas@redhat.com',
    url='https://github.com/openstack-k8s-operators/openstack-tests-list',
    packages=find_packages(include=['openstack_tests_list', 'openstack_tests_list.*']),
    entry_points={
        'console_scripts': [
            'tempest-skip=openstack_tests_list.main:main',
        ],
        'openstack_tests_list.cm': [
            'validate=openstack_tests_list.validate:Validate',
            'list=openstack_tests_list.list_yaml:ListSkippedYaml',
            'list-skipped=openstack_tests_list.list_yaml:ListSkippedYaml',
            'addtest=openstack_tests_list.add_test:AddTest',
            'list-allowed=openstack_tests_list.list_allowed:ListAllowedYaml',
        ],
    },
    install_requires=[
        'cliff',
        'inquirer',
        'ruamel.yaml>=0.17.7',
        'tempest',
        'validators',
        'voluptuous'
    ],
    setup_requires=['pbr>=1.8'],
    pbr=True,
)
