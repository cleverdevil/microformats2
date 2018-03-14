from microformats2 import validate

import json
import sys


data = json.loads(open(sys.argv[1], 'rb').read())
validate(data)
