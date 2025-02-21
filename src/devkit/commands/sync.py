from pathlib import Path

import click

from ..utils import out, run_cmd


def sync_repository(repository):
    out(f'==> Updating {repository}', style='highlight')

    path_to_repo = f'{Path.home() / "projects"}/{repository}'
    git_status = run_cmd(f'git -C {path_to_repo} status -s')

    if not git_status:
        run_cmd(f'git -C {path_to_repo} checkout main')
        run_cmd(f'git -C {path_to_repo} pull', print_output=True)
    else:
        out('Skipping this repo since there are local changes not yet committed', style='warn')


@click.command()
def sync():
    """Sync local git repositories with remote versions"""
    # TODO: Move this to a config file.
    repositories = ['devkit', 'dotfiles', 'for-joy-over-it', 'github-settings', 'highlights-api', 'jrisner', 'notes']

    for repository in repositories:
        sync_repository(repository)
