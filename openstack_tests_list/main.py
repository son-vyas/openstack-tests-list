import click
from .list_allowed import ListAllowedYaml
from .list_skipped import ListSkippedYaml
from .validate import ValidateYaml


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--file", required=True, type=click.Path(exists=True), help="File to validate."
)
def validate(file):
    validator = ValidateYaml(file)
    validator.take_action()


@cli.command()
@click.option(
    "--component", default=None, help="Specify the component name for allowed tests."
)
def list_allowed(component):
    try:
        allowlist = ListAllowedYaml(component=component)
        allowed_tests = allowlist.parse()
        click.echo(allowed_tests)
    except Exception as e:
        click.echo(f"Error processing allowed tests: {str(e)}")


@cli.command()
@click.option(
    "--component", default=None, help="Specify the component name for skipped tests."
)
def list_skipped(component):
    try:
        skiplist = ListSkippedYaml(component=component)
        skipped_tests = skiplist.parse()
        click.echo(skipped_tests)
    except Exception as e:
        click.echo(f"Error processing skipped tests: {str(e)}")


if __name__ == "__main__":
    cli()
