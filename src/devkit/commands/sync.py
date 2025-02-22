import inspect
import sys
from pathlib import Path

import click

from ..utils import error, out, run_cmd


def validate_config(config):
    if config is None or 'sync' not in config or config['sync'] is None or 'repositories' not in config['sync']:
        error("Missing required 'sync' configuration")
        out("\nAdd a 'sync' node to the config file with a list of repositories to sync. For example:\n")
        out(
            inspect.cleandoc("""
            sync:
              repositories:
                - foo
                - bar
            """)
        )
        sys.exit(1)


def get_repos():
    config = click.get_current_context().obj['config']
    validate_config(config)

    return config['sync']['repositories']


def sync_repository(repository):
    out(f'==> Updating {repository}', style='highlight')

    path_to_repository = Path.home() / 'projects' / repository

    if not path_to_repository.exists():
        error(f"Could not find directory '{path_to_repository}'")
        sys.exit(1)

    git_status = run_cmd(f'git -C {path_to_repository} status -s')

    if not git_status:
        run_cmd(f'git -C {path_to_repository} checkout main')
        run_cmd(f'git -C {path_to_repository} pull', print_output=True)
    else:
        out('Skipping this repo since there are local changes not yet committed', style='warn')


@click.command()
def sync():
    """Sync local git repositories with remote versions"""
    repositories = get_repos()

    for repository in repositories:
        sync_repository(repository)
