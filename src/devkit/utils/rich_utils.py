from rich.console import Console
from rich.theme import Theme


def out(str, style=None):
    """Print to the console using Rich."""
    console = Console(
        theme=Theme({'error': 'bold red', 'success': 'bold green', 'warn': 'yellow', 'highlight': 'bold magenta'})
    )

    console.print(str, style=style)
