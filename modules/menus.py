from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show_menu():
    table = Table(
        title="📘 [bold cyan]FACTURACIÓN[/bold cyan]",
        header_style="bold magenta",
        border_style="bright_blue",
        show_lines=True
    )
    table.add_column("Opción", justify="center", style="bold yellow", no_wrap=True)
    table.add_column("Descripción", style="white")

    table.add_row("1", "📈  Nueva Factura  ")
    table.add_row("2", "🚪  Salir  ")

    console.print(Panel.fit(table, border_style="cyan", title="Menú Principal"))