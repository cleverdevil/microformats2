import jsonschema

from .schema import Microformat

__all__ = ['validate', 'schema_for']


def schema_for(type):
    return Microformat.schema_for(type)


def validate(mf2):
    type = mf2.get('type', ['h-entry'])[0]
    schema = schema_for(type)
    jsonschema.validate(mf2, schema)
