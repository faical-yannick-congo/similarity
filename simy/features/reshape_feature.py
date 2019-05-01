import pyjq
import json
import os

def reshape(source=None, destination=".", dump=False):
    """the reshape feature that takes a json file and reshape it in a flat
    fashion.
    """
    if source is None:
        return {}

    name = source.split("/")[-1]
    blocks = name.split(".")
    reshaped = "{0}/{1}-reshaped.{2}".format(destination, blocks[0], blocks[1])
    content = {}
    with open(source, "r") as source_f:
        content = json.loads(source_f.read())

    cmd = "jq 'reduce ( tostream | select(length==2) | .[0] |= [join(\".\")] ) as [$p,$v] (\
                        {}\
                        ; setpath($p; $v)\
                        )' %s"%(source)

    flattened = os.popen("{}".format(cmd)).read()

    if dump:
        with open(reshaped, "w") as reshaped_f:
            reshaped_f.write(flattened)

    return json.loads(flattened)
