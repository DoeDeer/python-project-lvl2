# -*- coding: utf-8 -*-


"""Main logic provider module."""

import json
import logging

from gendiff.formatting import json_like, plain

logger = logging.getLogger(__name__)

JSON_FORMAT = 'json'
JSON_LIKE_FORMAT = 'json-like'
PLAIN_FORMAT = 'plain'
ALLOWED_FORMATS = {JSON_FORMAT, JSON_LIKE_FORMAT, PLAIN_FORMAT}  # noqa: WPS407


def py_to_json(py_obj):
    """Dump python object to json."""  # noqa: DAR
    if isinstance(py_obj, dict):
        lines = ['{']
        for key, value in py_obj.items():  # noqa: WPS110: it's ok, broad py obj
            lines.append('{0}: {1}'.format(key, value))
            lines.append('}')
        return ''.join(lines)

    dumped = json.dumps(py_obj)
    if dumped.startswith('"') and dumped.endswith('"'):
        return dumped[1:-1]
    return dumped


def format_json(full_diff: dict) -> str:
    """Return json string of diffs."""  # noqa: DAR
    return json.dumps(full_diff, indent=' ' * 4, sort_keys=True)


def format_output(full_diff, format_: str = JSON_FORMAT):
    """Format full diff dict to string representation in given format."""  # noqa: DAR
    if format_ not in ALLOWED_FORMATS:
        raise ValueError('Wrong format')

    return {
        JSON_FORMAT: format_json,
        JSON_LIKE_FORMAT: json_like.format_json_like,
        PLAIN_FORMAT: plain.format_plain,
    }.get(format_)(full_diff)
