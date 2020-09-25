# -*- coding: utf-8 -*-


"""PLain formatting module."""

from copy import deepcopy

from gendiff import diff
from gendiff.formatting import core


def format_plain(full_diff, high_module: str = '') -> str:
    """Format full diff between dicts to json string.

    Args:
        full_diff (dict): dict with changes.
        high_module (str): higher modules name.

    Returns:
        str: pretty looked  string.

    """
    changes_strings = []
    for key, state_leaf in sorted(full_diff.items(), key=lambda itm: itm[0]):
        state = state_leaf.get('type_')

        if state is None:
            changes_strings.extend(format_plain(
                state_leaf,
                high_module='{0}{1}{2}'.format(
                    high_module,
                    '.' if high_module else '',
                    key,
                ),
            ))

        if state in {diff.ADDED, diff.CHANGED, diff.REMOVED}:
            changes_strings.append(render_string(state_leaf, high_module, key))

    return ''.join(changes_strings)


def render_string(leaf: dict, module: str, key: str) -> str:
    """Render diff dict leaf with module level."""  # noqa: DAR
    # to prevent original data change
    leaf = deepcopy(leaf)
    if leaf['type_'] == diff.ADDED and isinstance(leaf['value'], dict):
        leaf['value'] = 'complex value'

    template = "Property '{module}' was {state_render}"
    state_render_mappings = {
        diff.ADDED: "added with value: '{value}'\n",
        diff.REMOVED: 'removed\n',
        diff.CHANGED: "changed. From '{old_value}' to '{value}'\n",
    }

    module = '{0}.{1}'.format(module, key) if module else key
    state_string = state_render_mappings[leaf['type_']].format(
        value=core.py_to_json(leaf['value']),
        old_value=core.py_to_json(leaf['old_value']),
    )
    return template.format(module=module, state_render=state_string)
