from enum import Enum
from urllib.parse import urlparse

import re


def is_url(value):
    if type(value) == dict:
        value = value.get('properties', {}).get('url', [''])[0]

    try:
        parsed = urlparse(value)
        if len(parsed.scheme) == 0:
            return False
        if len(parsed.netloc) == 0:
            return False
        return True
    except:
        return False


class PostTypes(Enum):
    event = 'event'
    rsvp = 'rsvp'
    repost = 'repost'
    like = 'like'
    reply = 'reply'
    video = 'video'
    photo = 'photo'
    note = 'note'
    article = 'article'


def get_post_type(mf2):
    content = None

    props = mf2.get('properties', {})

    # If the post is an "event" item (may be a [microformats2] root class
    # name of [h-event]), Then it is an event.
    if mf2.get('type', [''])[0] == 'h-event':
        return PostTypes.event

    # If the post has an "rsvp" property with a valid value (one of "yes",
    # "no", "maybe", "interested"), Then it is an RSVP post.
    if props.get('rsvp', [''])[0] in ('yes', 'no', 'maybe', 'interested'):
        return PostTypes.rsvp

    # If the post has a "repost-of" property with a valid URL, Then it is a
    # repost (AKA "share") post.
    if is_url(props.get('repost-of', [''])[0]):
        return PostTypes.repost

    # If the post has a "like-of" property with a valid URL, Then it is a like
    # (AKA "favorite") post.
    if is_url(props.get('like-of', [''])[0]):
        return PostTypes.like

    # If the post has an "in-reply-to" property with a valid URL, Then it is a
    # reply post.
    if is_url(props.get('in-reply-to', [''])[0]):
        return PostTypes.reply

    # If the post has a "video" property with a valid URL, Then it is a video
    # post.
    if is_url(props.get('video', [''])[0]):
        return PostTypes.video

    # If the post has a "photo" property with a valid URL, Then it is a photo
    # post.
    if is_url(props.get('photo', [''])[0]):
        return PostTypes.photo

    # If the post has a "content" property with a non-empty value,
    if len(props.get('content', [])):
        # Then use its first non-empty value as the content
        for prop in props['content']:
            if isinstance(prop, dict):
                if len(prop.get('value', '')):
                    content = prop['value']
                    break
                elif len(prop.get('html', '')):
                    content = prop['html']
                    break
            elif isinstance(prop, str):
                if len(prop):
                    content = prop

    # Else if the post has a "summary" property with a non-empty value,
    if content is None and len(props.get('summary', [])):
        # Then use its first non-empty value as the content
        for summary in prop['summary']:
            if len(summary):
                content = summary
                break

    # Else it is a note post.
    if content is None:
        return PostTypes.note

    # Otherwise...
    if (
        # If the post has no "name" property
        (not props.get('name'))

        or

        # or has a "name" property with an empty string value (or no value)
        (props.get('name', [''])[0] == '')
    ):
        # Then it is a note post.
        return PostTypes.note

    # Take the first non-empty value of the "name" property
    for name in props['name']:
        if len(name):
            # Trim all leading/trailing whitespace
            name = name.strip()

            # Collapse all sequences of internal whitespace to a single space
            # (0x20) character each
            exp = re.compile(r'\W+')
            name = exp.sub(' ', name)

            # Do the same with the content
            content = content.strip()
            content = exp.sub(' ', content)

            # If this processed "name" property value is NOT a prefix of the
            # processed content,
            if not content.startswith(name):
                # Then it is an article post.
                return PostTypes.article
            else:
                return PostTypes.note

    return PostTypes.note
