import click
from ..features import hellofeature

@click.command()

# The hello world feature support as command line.
@click.option('--hello/--no-hello', default=None, help="Here is the hello world.")

def handle(hello):
    """The similarity command line interface.
    simy provides reshaping/flattening capabilities for JSON/XML files and
    ultimately a similarity check between a record and a store of records
    based on some criteria.
    """
    if hello:
        print(hellofeature.helloworld())

if __name__ == '__corr.main__':
    handle()
