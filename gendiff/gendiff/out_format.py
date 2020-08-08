# -*- coding: utf-8 -*-


"""Module format files diff."""

import json
from typing import Optional

from gendiff.gendiff import diff


def prepare_to_show(source: dict, changed: dict) -> dict:
    """Compare to dict and show diffs.

    Args:
        source (dict): original dict.
        changed (dict): updated dict.


    Returns:
        dict: dict with union of source and changed keys, but with state prefix.

    """
    diffs = diff.diff(source, changed)
    to_format_dict = {}

    for key, state in diffs.items():
        if state in {diff.ADDED, diff.CHANGED}:
            to_format_dict['+ {0}'.format(key)] = changed[key]

        if state in {diff.REMOVED, diff.CHANGED}:
            to_format_dict['- {0}'.format(key)] = source[key]

        if state is diff.UNCHANGED:
            to_format_dict[key] = source[key]

    return to_format_dict


def changes_to_string(changes: dict, form: str = json) -> Optional[str]:
    """Return pretty-formed string of given object.

    Args:
        changes (dict): dict with changes, where keys shows diff state.
        form (str): output format type. Choices: json, plain.

    Returns:
        str: formated changes string.

    """
    if form == json:
        return json.dumps(changes, indent=2, sort_keys=True)
