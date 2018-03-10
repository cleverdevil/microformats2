microformats2
=============

A Python package for validating JSON-encoded 
[Microformats2](http://microformats.org/wiki/microformats2) using 
[JSON Schema](http://json-schema.org).


Usage
-----

Validating MF2 JSON:

```python
import microformats2

mf2 = { 
    "type": ["h-event"],
    "properties": {
        "name": ["IndieWebCamp 2012"],
        "url": ["http://indiewebcamp.com/2012"],
        "start": ["2012-06-30"],
        "end": ["2012-07-01"],
        "location": [{
            "value": "Geoloqi",
            "type": ["h-card"],
            "properties": {
                "name": ["Geoloqi"],
                "org": ["Geoloqi"],
                "url": ["http://geoloqi.com/"],
                "street-address": ["920 SW 3rd Ave. Suite 400"],
                "locality": ["Portland"],
                "region": ["Oregon"]
            }
        }]
    }
}

microformats2.validate(mf2)
```

Get the schema for a particular microformat:

```python3

import microformats2
import json

print(json.dumps(microformats2.schema_for('h-entry'), indent=2))
```
