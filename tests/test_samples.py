import pytest
import microformats2


def test_valid_h_entry():
    hEntry = {
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

    assert microformats2.validate(hEntry) is None


def test_valid_h_event():
    hEvent = {
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

    assert microformats2.validate(hEvent) is None


def test_valid_h_adr():
    hAdr = {
        "type": [
            "h-adr"
        ],
        "properties": {
            "street-address": [
                "17 Austerstræti"
            ],
            "locality": [
                "Reykjavík"
            ],
            "country-name": [
                "Iceland"
            ],
            "postal-code": [
                "107"
            ],
            "name": [
                "17 Austerstræti Reykjavík Iceland 107"
            ]
        }
    }

    assert microformats2.validate(hAdr) is None


def test_valid_h_card():
    hCard = {
        "type": [
            "h-card"
        ],
        "properties": {
            "photo": [
                "http://example.org/photo.png"
            ],
            "name": [
                "Joe Bloggs"
            ],
            "url": [
                "http://example.org"
            ],
            "email": [
                "mailto:joebloggs@example.com"
            ],
            "street-address": [
                "17 Austerstræti"
            ],
            "locality": [
                "Reykjavík"
            ],
            "country-name": [
                "Iceland"
            ]
        }
    }

    assert microformats2.validate(hCard) is None


def test_valid_nested_h_card():
    hCard = {
        "type": ["h-card"],
        "properties": {
            "name": ["Mitchell Baker"],
            "url": ["http://blog.lizardwrangler.com/"],
            "org": [{
                "value": "Mozilla Foundation",
                "type": ["h-card"],
                "properties": {
                    "name": ["Mozilla Foundation"],
                    "url": ["http://mozilla.org/"]
                }
            }]
        }
    }

    assert microformats2.validate(hCard) is None


def test_valid_h_geo():
    hGeo = {
        "type": [
            "h-geo"
        ],
        "properties": {
            "latitude": [
                "-27.116667"
            ],
            "longitude": [
                "-109.366667"
            ],
            "name": [
                "-27.116667, -109.366667"
            ]
        }
    }

    assert microformats2.validate(hGeo) is None


def test_valid_h_item():
    hItem = {
        "type": [
            "h-item"
        ],
        "properties": {
            "name": [
                "The Item Name"
            ],
            "photo": [
                "http://example.org/items/1/photo.png"
            ],
            "url": [
                "http://example.org/items/1"
            ]
        }
    }

    assert microformats2.validate(hItem) is None


def test_valid_h_product():
    hProduct = {
        "type": [
            "h-product"
        ],
        "properties": {
            "name": [
                "Microformats For Dummies"
            ],
            "photo": [
                "http://example.org/mfd.png"
            ],
            "description": [
                {
                    "value": "Want to get started using microformats, but intimidated by hyphens and mediawiki? This book contains everything you need to know!",
                    "html": "<p>Want to get started using microformats, but intimidated by hyphens and mediawiki? This book contains everything you need to know!</p>"
                }
            ],
            "price": [
                "20.00"
            ],
            "brand": [
                {
                    "value": "ACME Publishing inc.",
                    "type": [
                        "h-card"
                    ],
                    "properties": {
                        "name": [
                            "ACME Publishing inc."
                        ],
                        "url": [
                            "http://example.com/acme"
                        ]
                    }
                }
            ]
        }
    }

    assert microformats2.validate(hProduct) is None


def test_valid_h_recipe():
    hRecipe = {
        "type": [
            "h-recipe"
        ],
        "properties": {
            "name": [
                "Bagels"
            ],
            "ingredient": [
                "Flour",
                "Sugar",
                "Yeast"
            ],
            "yield": [
                "4"
            ],
            "instructions": [
                {
                    "value": "Start by mixing all the ingredients together.",
                    "html": "<ol>       <li>Start by mixing all the ingredients together.</li>     </ol>"
                }
            ]
        }
    }

    assert microformats2.validate(hRecipe) is None


def test_valid_h_review():
    hReview = {
        "type": [
            "h-review"
        ],
        "properties": {
            "name": [
                "Microformats: is structured data worth it?"
            ],
            "item": [
                {
                    "value": "Microformats",
                    "type": [
                        "h-item"
                    ],
                    "properties": {
                        "name": [
                            "Microformats"
                        ],
                        "url": [
                            "http://microformats.org"
                        ]
                    }
                }
            ],
            "rating": [
                "5"
            ],
            "published": [
                "2013-06-12 12:00:00"
            ],
            "author": [
                {
                    "value": "Joe Bloggs",
                    "type": [
                        "h-card"
                    ],
                    "properties": {
                        "name": [
                            "Joe Bloggs"
                        ],
                        "url": [
                            "http://example.com"
                        ]
                    }
                }
            ],
            "content": [
                {
                    "value": "Yes, microformats are undoubtedly great. They are the simplest way to markup structured data in HTML and reap the benefits thereof, including using your web page as your API by automatic conversion to JSON. The alternatives of microdata/schema and RDFa are much more work, require more markup, and are more complicated (harder to get right, more likely to break).",
                    "html": "<p>Yes, microformats are undoubtedly great. They are the simplest way to markup structured data in HTML and reap the benefits thereof, including using your web page as your API by automatic conversion to JSON. The alternatives of microdata/schema and RDFa are much more work, require more markup, and are more complicated (harder to get right, more likely to break).</p>"
                }
            ]
        }
    }

    assert microformats2.validate(hReview) is None


def test_valid_h_resume():
    hResume = {
        "type": [
            "h-resume"
        ],
        "properties": {
            "name": [
                "Joe Bloggs resume"
            ],
            "contact": [
                {
                    "value": "Joe Bloggs",
                    "type": [
                        "h-card"
                    ],
                    "properties": {
                        "name": [
                            "Joe Bloggs"
                        ],
                        "photo": [
                            "http://example.org/photo.png"
                        ],
                        "url": [
                            "http://example.org"
                        ]
                    }
                }
            ],
            "summary": [
                "Joe is a top-notch llama farmer with a degree in Llama husbandry and a thirst to produce the finest wool known to man"
            ],
            "skill": [
                "Llama husbandry"
            ]
        }
    }

    assert microformats2.validate(hResume) is None
