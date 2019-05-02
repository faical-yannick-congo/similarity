import click
import json
from ..features import reshape_feature

# Simy cli stuff for multiple commands interface.
@click.group()
def cli():
    """the similarity command line interface.
    simy provides reshaping/flattening capabilities for JSON/XML files and
    ultimately a similarity check between a record and a store of records
    based on some criteria.
    """
    pass

@cli.command()
@click.option('--src', default=None, help="The json file to be reshaped.")
@click.option('--dst', default=None, help="Provide a custom destination for the reshaped json.")
@click.option('--gen/--no-gen', default=None, help="Request the creation of the reshaped json.")
@click.option('--prt/--no-prt', default=None, help="Request the creation of the reshaped json.")
def reshape(src, dst, gen, prt):
    """flattens any nested dictionary using jq.
    """
    source = None
    dump = False
    destination = "."

    if src:
        with open(src, "r") as source_f:
            source = json.loads(source_f.read())

    if dst:
        destination = dst

    flattened = reshape_feature.reshape(source, destination)

    if gen:
        name = src.split("/")[-1]
        blocks = name.split(".")
        reshaped = "{0}/{1}-reshaped.{2}".format(destination, blocks[0], blocks[1])
        with open(reshaped, "w") as reshaped_f:
            reshaped_f.write(json.dumps(flattened, sort_keys=True, indent=4, separators=(',', ': ')))

    if prt:
        print(json.dumps(flattened, sort_keys=True, indent=4, separators=(',', ': ')))

handle = click.CommandCollection(sources=[cli])

if __name__ == '__simy.main__':
    handle()
