from rich.console import Console
from rich.theme import Theme


def get_rich_console() -> Console:
    return Console(
        theme=Theme({'error': 'bold red', 'success': 'bold green', 'warn': 'yellow', 'highlight': 'bold magenta'})
    )
