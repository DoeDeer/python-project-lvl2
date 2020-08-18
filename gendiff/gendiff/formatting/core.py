# -*- coding: utf-8 -*-


"""Main logic provider module."""

import json
import logging

from gendiff.gendiff.formatting import json_like, plain

logger = logging.getLogger(__name__)

JSON_FORMAT = 'json'
JSON_LIKE_FORMAT = 'json-like'
PLAIN_FORMAT = 'plain'


def py_to_json(py_obj):
    """Dump python object to json."""  # noqa: DAR
    return json.dumps(py_obj).replace('"', '')


def format_json(full_diff: dict) -> str:
    """Return json string of diffs."""  # noqa: DAR
    return json.dumps(full_diff, indent=' ' * 4, sort_keys=True)


def format_dummy(full_diff: dict) -> str:
    """Format unknown type."""  # noqa: DAR
    logger.error('Wrong formatting type. Returning json output.')
    return format_json(full_diff)


def format_output(full_diff, format_: str = JSON_FORMAT):
    """Format full diff dict to string representation in given format."""  # noqa: DAR
    return {
        JSON_FORMAT: format_json,
        JSON_LIKE_FORMAT: json_like.format_json_like,
        PLAIN_FORMAT: plain.format_plain,
    }.get(format_, format_dummy)(full_diff)
