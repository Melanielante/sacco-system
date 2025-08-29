import click

@click.group()
def cli():
    """Sacco System CLI"""
    pass

@cli.command()
def hello():
    """Test command"""
    click.echo("Hello, MEL! 🎉 Sacco System CLI is running.")

if __name__ == "__main__":
    cli()
