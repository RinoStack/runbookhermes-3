import click

@click.command()
def respond():
    """Handle incident response"""
    click.echo("Processing incident...")

if __name__ == '__main__':
    respond()