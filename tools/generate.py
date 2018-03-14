import microformats2.schema

import json


print(json.dumps(microformats2.schema.MicroformatsDocument.get_schema(), indent=2))
