import click
from openstack_tests_list.list_allowed import ListAllowedYaml
from openstack_tests_list.list_skipped import ListSkippedYaml
from openstack_tests_list.validate import ValidateYaml


@click.group()
def cli():
    pass


@cli.command()
@click.option("--file", required=True, type=click.Path(exists=True))
def validate(file):
    validator = ValidateYaml(file)
    validator.take_action()


@cli.command()
def list_allowed():
    allowlist = ListAllowedYaml()
    allowed_tests = allowlist.parse()
    click.echo(allowed_tests)


@cli.command()
def list_skipped():
    skiplist = ListSkippedYaml()
    skipped_tests = skiplist.parse()
    click.echo(skipped_tests)


def main():
    cli()


if __name__ == "__main__":
    cli()
