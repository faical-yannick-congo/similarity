import click
from ..features import hellofeature

@click.command()

# The hello world feature support as command line.
@click.option('--hello/--no-hello', default=None, help="Here is the hello world.")

def handle(hello):
    if hello:
        print(hellofeature.helloworld())

if __name__ == '__corr.main__':
    handle()
