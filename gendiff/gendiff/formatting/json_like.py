# -*- coding: utf-8 -*-


"""Pretty json - like dict formatting module."""

from gendiff.gendiff import diff
from gendiff.gendiff.formatting import core

JSON_DIFF_MAPPER = {  # noqa: WPS407
    diff.ADDED: '+ ',
    diff.REMOVED: '- ',
    diff.UNCHANGED: '  ',
}


def format_json_like(full_diff: dict, level: int = 1) -> str:  # noqa: WPS210
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
        state = state_leaf.get('type_')

        if state is None:
            form_strings.append(
                '{indent}{key}: {changes},\n'.format(
                    indent=indent,
                    key=key,
                    changes=format_json_like(state_leaf, level=level + 1),
                ),
            )

        if state in {diff.ADDED, diff.REMOVED, diff.UNCHANGED}:
            form_strings.append('{indent}{diff}{key}: {value},\n'.format(
                indent=indent[:-2],
                diff=JSON_DIFF_MAPPER[state],
                key=key,
                value=core.py_to_json(state_leaf['value']),
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
                new_val=core.py_to_json(state_leaf['value']),
                old_val=core.py_to_json(state_leaf['old_value']),
            ))

    # last key in json have no ','
    form_strings[-1] = form_strings[-1][:-2]
    form_strings.append('\n{ind}}}'.format(ind=indent[:-4]))
    return ''.join(form_strings)
