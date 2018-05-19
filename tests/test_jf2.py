import pytest
import microformats2


def test_simple_transform():
    hEntry = {
        "type": ["h-entry"],
        "properties": {
            "name": ["Microformats are amazing"],
            "author": [
                {
                    "value": "W. Developer",
                    "type": ["h-card"],
                    "properties": {
                        "name": ["W. Developer"], "url": ["http://example.com"]
                    },
                }
            ],
            "published": ["2013-06-13 12:00:00"],
            "summary": ["In which I extoll the virtues of using microformats."],
            "content": [{"value": "Blah blah blah", "html": "<p>Blah blah blah</p>"}],
        },
    }

    result = microformats2.to_jf2(hEntry)
    assert result == {
        'type': 'entry',
        'name': 'Microformats are amazing',
        'author': {
            'type': 'card',
            'name': 'W. Developer',
            'url': 'http://example.com'
        },
        'published': '2013-06-13 12:00:00',
        'summary': 'In which I extoll the virtues of using microformats.',
        'content': 'Blah blah blah'
    }


def test_h_event_transform():
    hEvent = {
        "type": ["h-event"],
        "properties": {
            "name": ["IndieWebCamp 2012"],
            "url": ["http://indiewebcamp.com/2012"],
            "start": ["2012-06-30"],
            "end": ["2012-07-01"],
            "location": [
                {
                    "value": "Geoloqi",
                    "type": ["h-card"],
                    "properties": {
                        "name": ["Geoloqi"],
                        "org": ["Geoloqi"],
                        "url": ["http://geoloqi.com/"],
                        "street-address": ["920 SW 3rd Ave. Suite 400"],
                        "locality": ["Portland"],
                        "region": ["Oregon"],
                    },
                }
            ],
        },
    }

    result = microformats2.to_jf2(hEvent)
    assert result == {
        "type": "event",
        "name": "IndieWebCamp 2012",
        "url": "http://indiewebcamp.com/2012",
        "start": "2012-06-30",
        "end": "2012-07-01",
        "location": {
            "type": "card",
            "name": "Geoloqi",
            "org": "Geoloqi",
            "url": "http://geoloqi.com/",
            "street-address": "920 SW 3rd Ave. Suite 400",
            "locality": "Portland",
            "region": "Oregon"
        }
    }

def test_h_adr_transform():
    hAdr = {
        "type": ["h-adr"],
        "properties": {
            "street-address": ["17 Austerstræti"],
            "locality": ["Reykjavík"],
            "country-name": ["Iceland"],
            "postal-code": ["107"],
            "name": ["17 Austerstræti Reykjavík Iceland 107"],
        },
    }

    result = microformats2.to_jf2(hAdr)
    assert result == {
        "type": "adr",
        "street-address": "17 Austerstræti",
        "locality": "Reykjavík",
        "country-name": "Iceland",
        "postal-code": "107",
        "name": "17 Austerstræti Reykjavík Iceland 107",
    }


def test_nested_h_card_transform():
    hCard = {
        "type": ["h-card"],
        "properties": {
            "name": ["Mitchell Baker"],
            "url": ["http://blog.lizardwrangler.com/"],
            "org": [
                {
                    "value": "Mozilla Foundation",
                    "type": ["h-card"],
                    "properties": {
                        "name": ["Mozilla Foundation"], "url": ["http://mozilla.org/"]
                    },
                }
            ],
        },
    }

    result = microformats2.to_jf2(hCard)
    assert result == {
        "type": "card",
        "name": "Mitchell Baker",
        "url": "http://blog.lizardwrangler.com/",
        "org": {
            "type": "card",
            "name": "Mozilla Foundation",
            "url": "http://mozilla.org/"
        }
    }


def test_h_product_transform():
    hProduct = {
        "type": ["h-product"],
        "properties": {
            "name": ["Microformats For Dummies"],
            "photo": ["http://example.org/mfd.png"],
            "description": [
                {
                    "value": "Want to get started using microformats, but intimidated by hyphens and mediawiki? This book contains everything you need to know!",
                    "html": "<p>Want to get started using microformats, but intimidated by hyphens and mediawiki? This book contains everything you need to know!</p>",
                }
            ],
            "price": ["20.00"],
            "brand": [
                {
                    "value": "ACME Publishing inc.",
                    "type": ["h-card"],
                    "properties": {
                        "name": ["ACME Publishing inc."],
                        "url": ["http://example.com/acme"],
                    }
                }
            ]
        }
    }

    result = microformats2.to_jf2(hProduct)
    assert result == {
        "type": "product",
        "name": "Microformats For Dummies",
        "photo": "http://example.org/mfd.png",
        "description": "Want to get started using microformats, but intimidated by hyphens and mediawiki? This book contains everything you need to know!",
        "price": "20.00",
        "brand": {
            "type": "card",
            "name": "ACME Publishing inc.",
            "url": "http://example.com/acme"
        }
    }
