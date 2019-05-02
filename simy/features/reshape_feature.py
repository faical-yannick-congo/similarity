import pyjq
import json
import os

def reshape(source=None, destination="."):
    """the reshape feature that takes a json file and reshape it in a flat
    fashion.
    """
    if source is None:
        return {}

    cmd = "echo '%s' | jq 'reduce ( tostream | select(length==2) | .[0] |= [join(\".\")] ) as [$p,$v] (\
                        {}\
                        ; setpath($p; $v)\
                        )'"%(json.dumps(source))

    flattened = os.popen("{}".format(cmd)).read()

    return json.loads(flattened)
