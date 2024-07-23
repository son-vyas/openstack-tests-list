import click
from openstack_tests_list.list_allowed import get_allowed_tests
from openstack_tests_list.list_skipped import get_skipped_tests
from openstack_tests_list.validate import Validate


@click.group()
def cli():
    pass


@cli.command()
@click.option("--file", required=True, type=click.Path(exists=True))
def validate(file):
    validator = Validate(None, None)
    # Create a mock object to pass as args
    args = type("obj", (object,), {"file": file})
    validator.take_action(args)


@cli.command()
@click.option("--file", required=True, type=click.Path(exists=True))
def list_allowed(file):
    allowed_tests = get_allowed_tests(file)
    click.echo(allowed_tests)


@cli.command()
@click.option("--file", required=True, type=click.Path(exists=True))
def list_skipped(file):
    skipped_tests = get_skipped_tests(file)
    click.echo(skipped_tests)


def main():
    cli()


if __name__ == "__main__":
    cli()
