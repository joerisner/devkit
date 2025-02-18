import click

from .commands.sync import sync

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
def cli() -> None:
    """A CLI for local development conveniences"""
    pass


cli.add_command(sync)
