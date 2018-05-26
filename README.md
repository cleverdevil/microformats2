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

For those of you not using Python, who just want a raw JSON schema file to use,
refer to
[schema.json](https://raw.githubusercontent.com/cleverdevil/microformats2/master/schema.json)
which was generated using this command:

```python3
python tools/generate.py > schema.json
```

Determine the post type for a MF2 JSON entry, using the [Post Type
Discovery](https://www.w3.org/TR/post-type-discovery/) guidelines from the W3C.

```python3

import microformats2

mf2 = {
    "type": [
        "h-entry"
    ],
    "properties": {
        "name": [
            "Microformats are amazing"
        ],
        "author": [
            {
                "value": "W. Developer",
                "type": [
                    "h-card"
                ],
                "properties": {
                    "name": [
                        "W. Developer"
                    ],
                    "url": [
                        "http://example.com"
                    ]
                }
            }
        ],
        "published": [
            "2013-06-13 12:00:00"
        ],
        "summary": [
            "In which I extoll the virtues of using microformats."
        ],
        "content": [
            {
                "value": "Blah blah blah",
                "html": "<p>Blah blah blah</p>"
            }
        ]
    }
}

assert microformats2.get_post_type(mf2) == microformats2.PostTypes.article
```

Convert MF2 JSON to JF2:

```python
jf2 = microformats2.to_jf2(mf2)
assert jf2 == {
    "type": "entry",
    "name": "Microformats are amazing",
    "author": {
        "type": "card",
        "name": "W. Developer",
        "url": "http://example.com"
    },
    "published": "2013-06-13 12:00:00",
    "summary": "In which I extoll the virtues of using microformats.",
    "content": "Blah blah blah"
}
```
