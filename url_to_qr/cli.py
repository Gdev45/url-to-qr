import qrcode
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
from datetime import datetime
import os

console = Console()


def generate_qr(url: str, output_dir="qr_codes"):
    # Create folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"qr_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    # Generate QR
    qr = qrcode.make(url)
    qr.save(filepath)

    return filepath


def main():
    console.print(
        Panel.fit(
            "[bold cyan]QR Code Generator[/bold cyan]\nTurn any URL into a permanent QR code",
            box=box.ROUNDED,
        )
    )

    while True:
        url = Prompt.ask("\n[bold green]Enter a URL[/bold green] (or type 'exit')")

        if url.lower() == "exit":
            console.print("\n[bold red]Goodbye![/bold red]")
            break

        if not url.startswith("http"):
            console.print("[yellow]⚠️ Make sure your URL starts with http:// or https://[/yellow]")
            continue

        filepath = generate_qr(url)

        console.print(
            Panel.fit(
                f"[bold white]QR Code created![/bold white]\n[green]{filepath}[/green]",
                box=box.DOUBLE,
            )
        )


if __name__ == "__main__":
    main()