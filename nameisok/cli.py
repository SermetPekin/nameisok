import click

from .core import get_status_package_cli
from .types_ import StrOrTuple

@click.command()
@click.argument("name")
def main(name: StrOrTuple):
    """CLI command to check PyPI package name availability."""
    get_status_package_cli(name)
    print('\n')

