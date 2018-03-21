import os.path
import json

import pytest
import microformats2


def test_article():
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

    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.article


def test_event():
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

    assert microformats2.get_post_type(hEvent) == microformats2.PostTypes.event


def test_note_name_only():
    hEntry = {"type": ["h-entry"], "properties": {"name": ["microformats.org at 7"]}}

    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.note


def test_article_with_summary():
    hEntry = {
        "type": ["h-entry"],
        "properties": {
            "url": ["http://microformats.org/2012/06/25/microformats-org-at-7"],
            "name": ["microformats.org at 7"],
            "content": [
                {
                    "value": "Last week the microformats.org community \n            celebrated its 7th birthday at a gathering hosted by Mozilla in \n            San Francisco and recognized accomplishments, challenges, and \n            opportunities.\n\n        The microformats tagline “humans first, machines second” \n            forms the basis of many of our \n            principles, and \n            in that regard, we’d like to recognize a few people and \n            thank them for their years of volunteer service",
                    "html": "\n        <p class=\"p-summary\">Last week the microformats.org community \n            celebrated its 7th birthday at a gathering hosted by Mozilla in \n            San Francisco and recognized accomplishments, challenges, and \n            opportunities.</p>\n\n        <p>The microformats tagline “humans first, machines second” \n            forms the basis of many of our \n            <a href=\"http://microformats.org/wiki/principles\">principles</a>, and \n            in that regard, we’d like to recognize a few people and \n            thank them for their years of volunteer service </p>\n",
                }
            ],
            "summary": [
                "Last week the microformats.org community \n            celebrated its 7th birthday at a gathering hosted by Mozilla in \n            San Francisco and recognized accomplishments, challenges, and \n            opportunities."
            ],
            "updated": ["2012-06-25 17:08:26"],
            "author": [
                {
                    "value": "Tantek",
                    "type": ["h-card"],
                    "properties": {"name": ["Tantek"], "url": ["http://tantek.com/"]},
                }
            ],
        },
    }

    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.article


def test_photo():
    hEntry = {
        "type": ["h-entry"],
        "properties": {
            "name": ["microformats.org at 7"],
            "url": [
                "http://microformats.org/",
                "http://microformats.org/2012/06/25/microformats-org-at-7",
                "http://microformats.org/2012/06/25/microformats-org-at-7",
                "http://microformats.org/",
                "http://microformats.org/wiki/microformats2-parsing",
                "http://microformats.org/wiki/value-class-pattern",
                "http://microformats.org/wiki/",
                "http://microformats.org/discuss",
            ],
            "photo": [
                "http://example.com/images/logo.gif",
                "http://example.com/posterimage.jpg",
            ],
        },
    }

    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.photo


def get_test_data(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    d = open(dir_path + '/post-type-discovery-tests/' + filename, 'r').read()
    return json.loads(d)['items'][0]


def test_article_aaron():
    hEntry = get_test_data('article-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.article


def test_article_tantek():
    hEntry = get_test_data('article-tantek.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.article


def test_like_aaron():
    hEntry = get_test_data('like-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.like


def test_note_aaron():
    hEntry = get_test_data('note-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.note


def test_note_aaron2():
    hEntry = get_test_data('note-aaron2.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.note


def test_photo_aaron():
    hEntry = get_test_data('photo-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.photo


def test_photo_tantek():
    hEntry = get_test_data('photo-tantek.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.photo


def test_reply_aaron():
    hEntry = get_test_data('reply-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.reply


def test_reply_aaronmultiple():
    hEntry = get_test_data('reply-aaronmultiple.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.reply


def test_repost_aaron():
    hEntry = get_test_data('repost-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.repost


def test_rsvp_aaron():
    hEntry = get_test_data('rsvp-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.rsvp


def test_rsvp_aaronmultiple():
    hEntry = get_test_data('rsvp-aaronmultiple.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.rsvp


def test_rsvp_tantek():
    hEntry = get_test_data('rsvp-tantek.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.rsvp


def test_video_aaron():
    hEntry = get_test_data('video-aaron.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.video


def test_video_shane():
    hEntry = get_test_data('video-shane.json')
    assert microformats2.get_post_type(hEntry) == microformats2.PostTypes.video
