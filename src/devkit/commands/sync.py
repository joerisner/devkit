from pathlib import Path

import click

from ..utils.rich_utils import get_rich_console
from ..utils.shell_utils import run_cmd

console = get_rich_console()


def sync_repository(repository: str) -> None:
    console.print(f'==> Updating {repository}', style='highlight')

    path_to_repo = f'{Path.home() / "projects"}/{repository}'
    git_status = run_cmd(f'git -C {path_to_repo} status -s')

    if not git_status:
        run_cmd(f'git -C {path_to_repo} checkout main')
        run_cmd(f'git -C {path_to_repo} pull', print_output=True)
    else:
        console.print('Skipping this repo since there are local changes not yet committed', style='warn')


@click.command()
def sync() -> None:
    """Sync local git repositories with remote versions"""
    repositories = ['dotfiles', 'for-joy-over-it', 'github-settings', 'highlights-api', 'jrisner', 'notes']

    for repository in repositories:
        sync_repository(repository)
