# -*- coding: utf-8 -*-


"""Module format files diff."""

import json
from typing import Optional, Tuple

from sortedcontainers import SortedDict

from gendiff.gendiff import diff

JSON_FORMAT = 'json'
PLAIN_FORMAT = 'plain'
INDENT = '  '


def sort_func(key: str) -> Tuple[str, str]:
    """Define keys sort order.

    Args:
        key: original dict key.

    Returns:
        tuple: sort rule.

    """
    key = key.lstrip()
    if any(key.startswith(pref) for pref in ('+', '-')):
        return key[2:], key[0]
    return key, ''


def prepare_to_show(source: dict, changed: dict, level: int = 1) -> dict:
    """Compare to dict and show diffs.

    Args:
        source (dict): original dict.
        changed (dict): updated dict.
        level (int): level of nesting.


    Returns:
        dict: dict with union of source and changed keys, but with state prefix.

    """
    diffs = diff.diff(source, changed)
    to_format_dict = SortedDict(sort_func)
    indent = INDENT * level

    for key, state in diffs.items():
        if state is diff.NESTED:
            to_format_dict['{0}{1}'.format(
                indent,
                key,
            )] = prepare_to_show(source[key], changed[key], level=level + 1)

        if state in {diff.ADDED, diff.CHANGED}:
            to_format_dict['{0}+ {1}'.format(indent[:-2], key)] = changed[key]

        if state in {diff.REMOVED, diff.CHANGED}:
            to_format_dict['{0}- {1}'.format(indent[:-2], key)] = source[key]

        if state is diff.UNCHANGED:
            to_format_dict['{0}{1}'.format(indent, key)] = source[key]

    return to_format_dict


def changes_to_string(changes: dict, form: str = JSON_FORMAT) -> Optional[str]:
    """Return pretty-formed string of given object.

    Args:
        changes (dict): dict with changes, where keys shows diff state.
        form (str): output format type. Choices: json, plain.

    Returns:
        str: formated changes string.

    """
    if form == JSON_FORMAT:
        return json.dumps(changes, indent=2).replace('"', '')
