# -*- coding: utf-8 -*-


"""Module to find diff between two dicts."""

UNCHANGED = 'UNCHANGED'
CHANGED = 'CHANGED'
ADDED = 'ADDED'
REMOVED = 'REMOVED'
NESTED = 'NESTED'

KEY_STATES = (UNCHANGED, CHANGED, ADDED, REMOVED, NESTED)


def compare_dicts(source: dict, changed: dict) -> dict:  # noqa: WPS210
    """Return dict with diff keys info.

    Args:
        source (dict): source dict with original values.
        changed (dict): changed dict with updated values.

    Returns:
        dict: dict with keys from both source and changed, where values are
        instances of KEY_STATES.

    """
    both_keys = source.keys() | changed.keys()
    added_keys = changed.keys() - source.keys()
    removed_keys = source.keys() - changed.keys()
    keys_states = {}

    for added in added_keys:
        keys_states[added] = ADDED

    for removed in removed_keys:
        keys_states[removed] = REMOVED

    for same in both_keys - (added_keys | removed_keys):
        if isinstance(source[same], dict) and isinstance(changed[same], dict):
            keys_states[same] = NESTED
        elif source[same] == changed[same]:
            keys_states[same] = UNCHANGED
        else:
            keys_states[same] = CHANGED

    return keys_states


def build_diff_tree(source: dict, changed: dict) -> dict:
    """Return dict with full info representation about changes.

    Args:
        source (dict): source dict with original values.
        changed (dict): changed dict with updated values.

    Returns:
        dict: dict with mapping key: {type: KEY_STATE, value: new_value,
        old_value: old_value if state == CHANGED else None.

    """
    diff_states = compare_dicts(source, changed)
    full_diff = {}
    for key, state in diff_states.items():
        if state is NESTED:
            full_diff[key] = build_diff_tree(source[key], changed[key])

        if state is ADDED:
            full_diff[key] = make_leaf(state, changed[key])

        if state in {REMOVED, UNCHANGED}:
            full_diff[key] = make_leaf(state, source[key])

        if state is CHANGED:
            full_diff[key] = make_leaf(state, changed[key], source[key])

    return full_diff


def make_leaf(type_: int, leaf_value, old_value=None):
    """Crete full diff leaf."""  # noqa: DAR
    return {'type_': type_, 'value': leaf_value, 'old_value': old_value}