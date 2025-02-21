import subprocess

from .rich_utils import out


def run_cmd(cmd, print_output=False):
    """Run a shell command and return its output."""
    output = subprocess.check_output(cmd.split(' '), text=True).strip()

    if print_output:
        out(output)

    return output
