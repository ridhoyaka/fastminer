"""CLI integration for web app."""

from __future__ import annotations

import webbrowser
from pathlib import Path

import typer

app = typer.Typer(name="web", help="Launch the web interface.", no_args_is_help=False)


@app.callback(invoke_without_command=True)
def main(
    host: str = typer.Option("127.0.0.1", help="Host to bind (default: 127.0.0.1)"),
    port: int = typer.Option(5000, help="Port to bind (default: 5000)"),
    no_browser: bool = typer.Option(False, help="Do not open browser automatically"),
):
    """Launch the Fast Miner web app (offline, browser-based)."""
    from dc.web.app import app as flask_app
    from dc.web.app import init_db

    init_db()
    Path("data/uploads").mkdir(parents=True, exist_ok=True)
    Path("models").mkdir(parents=True, exist_ok=True)
    Path("reports").mkdir(parents=True, exist_ok=True)
    Path(".web_data").mkdir(parents=True, exist_ok=True)

    if not no_browser:
        import threading
        import time

        def open_browser():
            time.sleep(1.5)
            webbrowser.open(f"http://{host}:{port}/")

        threading.Thread(target=open_browser, daemon=True).start()

    typer.echo(f"Starting Fast Miner web app at http://{host}:{port}")
    typer.echo("Paths:")
    typer.echo("  data/uploads/  - uploaded files")
    typer.echo("  models/        - saved models")
    typer.echo("  reports/       - outputs & inspection reports")
    typer.echo("  .web_data/     - history database (SQLite)")
    typer.echo("Press Ctrl+C to stop")
    flask_app.run(host=host, port=port, threaded=True, debug=False)
