import pyfiglet
from rich.console import Console
from rich.panel import Panel

console = Console()

# Título principal
title1 = pyfiglet.figlet_format("FACTURACION", font="slant",)
subtitle = pyfiglet.figlet_format("ELECTRONICA", font="digital")

def show_title():
    console.print(Panel.fit(
        f"[bold cyan]{title1}[/bold cyan]\n[bold magenta]{subtitle}[/bold magenta]",
        border_style="bright_blue",
        title="📘 SISTEMA DE",
    ))

