import subprocess

from .rich_utils import get_rich_console

console = get_rich_console()


def run_cmd(cmd: str, print_output: bool = False) -> str:
    output = subprocess.check_output(cmd.split(' '), text=True).strip()

    if print_output:
        console.print(output)

    return output
