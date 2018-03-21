import jsl
import jsonschema


#
# common fields
#

string_array = jsl.ArrayField(items=jsl.StringField())
email_array = jsl.ArrayField(items=jsl.StringField(format='email'))
uri_array = jsl.ArrayField(items=jsl.StringField(format='uri'))
datetime_array = jsl.ArrayField(items=jsl.StringField(format='date-time'))

content_field = jsl.DictField(
    properties={'value': jsl.StringField(), 'html': jsl.StringField()}
)
content_array = jsl.ArrayField(jsl.OneOfField([jsl.StringField(), content_field]))

latitude = jsl.ArrayField(items=jsl.StringField(pattern=r'[-+]?\d+(\.\d+)?'))
longitude = jsl.ArrayField(items=jsl.StringField(pattern=r'[-+]?\d+(\.\d+)?'))
altitude = jsl.ArrayField(items=jsl.StringField(pattern=r'[-+]?\d+(\.\d+)?'))

photo_field = jsl.ArrayField(
    jsl.OneOfField(
        [
            jsl.StringField(format='uri'),
            jsl.DictField(
                properties={
                    'value': jsl.StringField(format='uri'), 'alt': jsl.StringField()
                }
            ),
        ]
    )
)

type_of = lambda *types: jsl.ArrayField(
    jsl.StringField(enum=types), required=True, min_length=1
)


#
# microformat schemas
#


class Microformat(jsl.Document):

    class Options:
        additional_properties = True

    value = jsl.StringField()

    @classmethod
    def schema_for(cls, type):
        for subclass in cls.__subclasses__():
            if subclass.type.items.get_enum()[0] == type:
                return subclass.get_schema()


class hGeo(Microformat):
    type = type_of('h-geo')
    properties = jsl.DictField(
        required=True,
        properties={'latitude': latitude, 'longitude': longitude, 'altitude': altitude},
    )


class hAdr(Microformat):
    type = type_of('h-adr')
    properties = jsl.DictField(
        required=True,
        properties={
            'street-address': string_array,
            'extended-address': string_array,
            'post-office-box': string_array,
            'locality': string_array,
            'region': string_array,
            'postal-code': string_array,
            'country-name': string_array,
            'label': string_array,
            'geo': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hGeo, as_ref=True)]
                )
            ),
            'latitude': latitude,
            'longitude': longitude,
            'altitude': altitude,
        },
    )


class hCard(Microformat):
    type = type_of('h-card')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'honorific-prefix': string_array,
            'given-name': string_array,
            'additional-name': string_array,
            'family-name': string_array,
            'sort-string': string_array,
            'honorific-suffix': string_array,
            'nickname': string_array,
            'email': email_array,
            'logo': uri_array,
            'photo': photo_field,
            'url': uri_array,
            'uid': string_array,
            'category': string_array,
            'adr': jsl.ArrayField(
                items=jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hAdr, as_ref=True)]
                )
            ),
            'street-address': string_array,
            'extended-address': string_array,
            'post-office-box': string_array,
            'locality': string_array,
            'region': string_array,
            'postal-code': string_array,
            'country-name': string_array,
            'label': string_array,
            'geo': jsl.ArrayField(
                items=jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hGeo, as_ref=True)]
                )
            ),
            'latitude': latitude,
            'longitude': longitude,
            'altitude': altitude,
            'tel': string_array,
            'note': string_array,
            'bday': datetime_array,
            'key': string_array,
            'org': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(),
                        jsl.DocumentField(jsl.RECURSIVE_REFERENCE_CONSTANT),
                    ]
                )
            ),
            'job-title': string_array,
            'role': string_array,
            'impp': string_array,
            'sex': string_array,
            'gender-identity': string_array,
            'anniversary': datetime_array,
        },
    )


class hItem(Microformat):
    type = type_of('h-item')
    properties = jsl.DictField(
        required=True,
        properties={'name': string_array, 'url': uri_array, 'photo': photo_field},
    )


class hProduct(Microformat):
    type = type_of('h-product')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'photo': photo_field,
            'brand': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'category': string_array,
            'description': content_array,
            'url': uri_array,
            'identifier': jsl.ArrayField(
                jsl.DictField(
                    properties={'type': jsl.StringField(), 'value': jsl.StringField()}
                )
            ),
            'review': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(),
                        jsl.DocumentField('hReview', as_ref=True),
                        jsl.DocumentField('hReviewAggregate', as_ref=True),
                    ]
                )
            ),
            'price': string_array,
        },
    )


class hCite(Microformat):
    type = type_of('h-cite')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'published': datetime_array,
            'author': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'url': uri_array,
            'uid': uri_array,
            'publication': string_array,
            'accessed': datetime_array,
            'content': content_array,
        },
    )


class hEntry(Microformat):
    type = type_of('h-entry')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'summary': string_array,
            'content': content_array,
            'published': datetime_array,
            'updated': datetime_array,
            'author': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'category': string_array,
            'url': uri_array,
            'uid': string_array,
            'location': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(),
                        jsl.DocumentField(hGeo, as_ref=True),
                        jsl.DocumentField(hAdr, as_ref=True),
                        jsl.DocumentField(hCard, as_ref=True),
                    ]
                )
            ),
            'syndication': uri_array,
            'in-reply-to': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(format='uri'),
                        jsl.DocumentField(hCite, as_ref=True),
                    ]
                )
            ),
            'rsvp': jsl.ArrayField(
                jsl.StringField(
                    enum=['yes', 'no', 'maybe', 'interested'], required=True
                ),
                min_items=1,
                max_items=1,
            ),
            'like-of': uri_array,
            'repost-of': uri_array,
            'bookmark-of': uri_array,
            'items': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.DocumentField(hItem, as_ref=True),
                        jsl.DocumentField(hProduct, as_ref=True),
                    ]
                )
            ),
            'photo': photo_field,
            'video': uri_array,
            'audio': uri_array,
        },
    )


class hEvent(Microformat):
    type = type_of('h-event')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'summary': string_array,
            'start': datetime_array,
            'end': datetime_array,
            'duration': string_array,
            'description': string_array,
            'url': uri_array,
            'category': string_array,
            'location': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(),
                        jsl.DocumentField(hGeo, as_ref=True),
                        jsl.DocumentField(hAdr, as_ref=True),
                        jsl.DocumentField(hCard, as_ref=True),
                    ]
                )
            ),
        },
    )


class hReview(Microformat):
    type = type_of('h-review')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'item': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(),
                        jsl.DocumentField(hCard, as_ref=True),
                        jsl.DocumentField(hItem, as_ref=True),
                        jsl.DocumentField(hProduct, as_ref=True),
                        jsl.DocumentField(hEvent, as_ref=True),
                        jsl.DocumentField(hAdr, as_ref=True),
                        jsl.DocumentField(hGeo, as_ref=True),
                    ]
                )
            ),
            'author': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'published': datetime_array,
            'rating': jsl.ArrayField(jsl.StringField()),
            'category': string_array,
            'url': uri_array,
            'content': content_array,
        },
    )


class hRating(Microformat):
    type = type_of('h-rating')
    properties = jsl.DictField(
        required=True,
        properties={
            'average': string_array,
            'best': string_array,
            'count': string_array,
            'name': string_array,
        },
    )


class hReviewAggregate(Microformat):
    type = type_of('h-review-aggregate')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'rating': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hRating, as_ref=True)]
                )
            ),
            'item': jsl.ArrayField(
                jsl.OneOfField(
                    [
                        jsl.StringField(),
                        jsl.DocumentField(hCard, as_ref=True),
                        jsl.DocumentField(hItem, as_ref=True),
                        jsl.DocumentField(hProduct, as_ref=True),
                        jsl.DocumentField(hEvent, as_ref=True),
                        jsl.DocumentField(hAdr, as_ref=True),
                        jsl.DocumentField(hGeo, as_ref=True),
                    ]
                )
            ),
            'average': string_array,
            'best': string_array,
            'worst': string_array,
            'count': string_array,
            'votes': string_array,
            'category': string_array,
            'url': uri_array,
        },
    )


class hRecipe(Microformat):
    type = type_of('h-recipe')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'ingredient': content_array,
            'yield': string_array,
            'instructions': content_array,
            'duration': string_array,
            'photo': photo_field,
            'summary': content_array,
            'author': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'published': datetime_array,
            'nutrition': string_array,
            'category': string_array,
        },
    )


class hResume(Microformat):
    type = type_of('h-resume')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'summary': content_array,
            'contact': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'education': jsl.ArrayField(jsl.DocumentField(hEvent, as_ref=True)),
            'experience': jsl.ArrayField(jsl.DocumentField(hEvent, as_ref=True)),
            'skill': string_array,
            'affiliation': jsl.ArrayField(jsl.DocumentField(hCard, as_ref=True)),
        },
    )


class hFeed(Microformat):
    type = type_of('h-feed')
    properties = jsl.DictField(
        required=True,
        properties={
            'name': string_array,
            'author': jsl.ArrayField(
                jsl.OneOfField(
                    [jsl.StringField(), jsl.DocumentField(hCard, as_ref=True)]
                )
            ),
            'url': uri_array,
            'photo': photo_field,
            'summary': content_array,
            'children': jsl.ArrayField(jsl.DocumentField(hEntry, as_ref=True)),
        },
    )


class MicroformatsDocument(jsl.Document):

    class Options:
        additional_properties = True

    items = jsl.ArrayField(
        jsl.OneOfField(
            [
                jsl.DocumentField(hGeo, as_ref=True),
                jsl.DocumentField(hAdr, as_ref=True),
                jsl.DocumentField(hCard, as_ref=True),
                jsl.DocumentField(hItem, as_ref=True),
                jsl.DocumentField(hProduct, as_ref=True),
                jsl.DocumentField(hEntry, as_ref=True),
                jsl.DocumentField(hEvent, as_ref=True),
                jsl.DocumentField(hReview, as_ref=True),
                jsl.DocumentField(hReviewAggregate, as_ref=True),
                jsl.DocumentField(hRecipe, as_ref=True),
                jsl.DocumentField(hResume, as_ref=True),
                jsl.DocumentField(hFeed, as_ref=True),
            ]
        )
    )
