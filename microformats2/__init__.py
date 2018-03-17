import jsonschema

from .schema import Microformat, MicroformatsDocument
from .discovery import get_post_type, PostTypes

__all__ = ['validate', 'schema_for', 'get_post_type', 'PostTypes']


def schema_for(type):
    return Microformat.schema_for(type)


def validate(mf2):
    if 'type' in mf2:
        type = mf2.get('type', ['h-entry'])[0]
        schema = schema_for(type)
    else:
        schema = MicroformatsDocument.get_schema()
    jsonschema.validate(mf2, schema)
