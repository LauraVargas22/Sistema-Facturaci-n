import modules.customs as cu
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

class Products:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class Invoice:
    def __init__(self):
        self.products = []

    def add_product(self, product: Products):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(p.price for p in self.products)

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        return subtotal * 0.10 if subtotal > 100 else 0

    def calculate_total(self):
        return self.calculate_subtotal() - self.calculate_discount()

    def show_invoice(self):
        console = Console()
        console.print("[bold cyan]=== FACTURA ===[/bold cyan]\n")
        for product in self.products:
            console.print(product)
        console.print(f"[bold white]Subtotal:[/bold white] ${self.calculate_subtotal():.2f}")
        console.print(f"[bold yellow]Descuento aplicado:[/bold yellow] -${self.calculate_discount():.2f}")
        console.print(f"[bold green]Total a pagar:[/bold green] ${self.calculate_total():.2f}")


def main():
    console = Console()
    invoice = Invoice()
    console.print("[bold cyan]=== Sistema de Facturación ===[/bold cyan]\n")
    num_products = int(console.input("[yellow]Ingrese el número de productos a facturar: [/yellow] "))

    for i in range(num_products):
        name = console.input(f"\n[white]Ingrese el nombre del producto {i+1}: [/white]")
        price = float(console.input(f"[white]Ingrese el precio del producto {name}: [/white]"))
        product = Products(name, price)
        invoice.add_product(product)
        cu.borrarPantalla()

    invoice.show_invoice()
