# -*- coding: utf-8 -*-


"""Module format files diff."""

import json

from gendiff.gendiff import diff

JSON_FORMAT = 'json'
JSON_LIKE_FORMAT = 'json-like'
PLAIN_FORMAT = 'plain'

JSON_DIFF_MAPPER = {  # noqa: WPS407
    diff.ADDED: '+ ',
    diff.REMOVED: '- ',
    diff.UNCHANGED: '  ',
}


def py_to_json(py_obj):
    """Dump python object to json."""  # noqa: DAR
    return json.dumps(py_obj).replace('"', '')


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
        state = state_leaf.get('type')

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


def format_plain(full_diff, high_module: str = ''):
    """Format full diff between dicts to json string.

    Args:
        full_diff (dict): dict with changes.
        high_module (str): higher modules name.

    Returns:
        str: pretty looked  string.

    """
    changes_strings = []
    for key, state_leaf in sorted(full_diff.items(), key=lambda itm: itm[0]):
        state = state_leaf.get('type')

        if state is None:
            changes_strings.extend(format_plain(
                state_leaf,
                high_module='{0}{1}{2}'.format(
                    high_module,
                    '.' if high_module else '',
                    key,
                ),
            ))

        if state is diff.ADDED:
            format_string = (
                "Property '{module}{key}' was added with value: '{value}'\n"
            )
            changes_strings.append(
                format_string.format(
                    module=high_module + '.' if high_module else '',
                    key=key,
                    value='complex value' if isinstance(
                        state_leaf['value'],
                        dict,
                    ) else py_to_json(state_leaf['value']),
                ),
            )

        if state is diff.REMOVED:
            changes_strings.append(
                "Property '{module}{key}' was removed\n".format(
                    module=high_module + '.' if high_module else '',
                    key=key,
                ),
            )

        if state is diff.CHANGED:
            format_string = (
                "Property '{0}{1}' was changed. From '{2}' to '{3}'\n"
            )
            changes_strings.append(format_string.format(
                high_module + '.' if high_module else '',
                key,
                py_to_json(state_leaf['old_value']),
                py_to_json(state_leaf['value']),
            ))
    return ''.join(changes_strings)


def format_json(full_diff: dict) -> str:
    return json.dumps(full_diff, indent=' ' * 4, sort_keys=True)


def format_output(full_diff, format_: str = JSON_FORMAT):
    """Format full diff dict to string representation in given format."""  # noqa: DAR
    if format_ == JSON_FORMAT:
        return format_json(full_diff)
    if format_ == PLAIN_FORMAT:
        return format_plain(full_diff)
    if format_ == JSON_LIKE_FORMAT:
        return format_json_like(full_diff)
