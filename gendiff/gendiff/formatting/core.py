# -*- coding: utf-8 -*-


"""Main logic provider module."""

import json

from gendiff.gendiff.formatting import json_like, plain

JSON_FORMAT = 'json'
JSON_LIKE_FORMAT = 'json-like'
PLAIN_FORMAT = 'plain'


def py_to_json(py_obj):
    """Dump python object to json."""  # noqa: DAR
    return json.dumps(py_obj).replace('"', '')


def format_json(full_diff: dict) -> str:
    """Return json string of diffs."""  # noqa: DAR
    return json.dumps(full_diff, indent=' ' * 4, sort_keys=True)


def format_output(full_diff, format_: str = JSON_FORMAT):
    """Format full diff dict to string representation in given format."""  # noqa: DAR
    if format_ == JSON_FORMAT:
        return format_json(full_diff)
    if format_ == PLAIN_FORMAT:
        return plain.format_plain(full_diff)
    if format_ == JSON_LIKE_FORMAT:
        return json_like.format_json_like(full_diff)
