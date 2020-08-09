# -*- coding: utf-8 -*-


"""Module format files diff."""

import json

from gendiff.gendiff import diff

JSON_FORMAT = 'json'
PLAIN_FORMAT = 'plain'

JSON_DIFF_MAPPER = {  # noqa: WPS407
    diff.ADDED: '+ ',
    diff.REMOVED: '- ',
    diff.UNCHANGED: '  ',
}


def py_to_json(py_obj):
    """Dump python object to json."""  # noqa: DAR
    return json.dumps(py_obj).replace('"', '')


def format_json(full_diff: dict, level: int = 1) -> str:  # noqa: WPS210
    """Format full diff between dicts to json string.

    Args:
        full_diff (dict): dict with changes.
        level (int): level of indents.

    Returns:
        str: pretty looked  string.

    """
    indent = ' ' * 4 * level
    form_strings = ['{\n']
    for key, state_leaf in sorted(full_diff.items(), key=lambda itm: itm[0]):
        state = state_leaf.get('type')

        if state is None:
            form_strings.append(
                '{indent}{key}: {changes},\n'.format(
                    indent=indent,
                    key=key,
                    changes=format_json(state_leaf, level=level + 1),
                ),
            )

        if state in {diff.ADDED, diff.REMOVED, diff.UNCHANGED}:
            form_strings.append('{indent}{diff}{key}: {value},\n'.format(
                indent=indent[:-2],
                diff=JSON_DIFF_MAPPER[state],
                key=key,
                value=py_to_json(state_leaf['value']),
            ))

        if state is diff.CHANGED:
            form_string = (
                '{ind}{add}{key}: {new_val},\n{ind}{rem}{key}: {old_val},\n'
            )
            form_strings.append(form_string.format(
                ind=indent[:-2],
                key=key,
                add=JSON_DIFF_MAPPER[diff.ADDED],
                rem=JSON_DIFF_MAPPER[diff.REMOVED],
                new_val=py_to_json(state_leaf['value']),
                old_val=py_to_json(state_leaf['old_value']),
            ))

    # last key in json have no ','
    form_strings[-1] = form_strings[-1][:-2]
    form_strings.append('\n{ind}}}'.format(ind=indent[:-4]))
    return ''.join(form_strings)


def format_output(full_diff, format_: str = JSON_FORMAT):
    """Format full diff dict to string representation in given format."""  # noqa: DAR
    if format_ == JSON_FORMAT:
        return format_json(full_diff)
