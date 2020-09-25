# -*- coding: utf-8 -*-


"""Module to find diff between two dicts."""

UNCHANGED = 'UNCHANGED'
CHANGED = 'CHANGED'
ADDED = 'ADDED'
REMOVED = 'REMOVED'
NESTED = 'NESTED'

KEY_STATES = (UNCHANGED, CHANGED, ADDED, REMOVED, NESTED)


def build_diff_tree(source: dict, changed: dict) -> dict:
    """Return dict with full info representation about changes.

    Args:
        source (dict): source dict with original values.
        changed (dict): changed dict with updated values.

    Returns:
        dict: dict with mapping key: {type: KEY_STATE, value: new_value,
        old_value: old_value if state == CHANGED else None.

    """
    both_keys = source.keys() | changed.keys()
    added_keys = changed.keys() - source.keys()
    removed_keys = source.keys() - changed.keys()
    full_diff = {}

    for added in added_keys:
        full_diff[added] = make_leaf(ADDED, changed[added])

    for removed in removed_keys:
        full_diff[removed] = make_leaf(REMOVED, source[removed])

    for same in both_keys - (added_keys | removed_keys):
        source_item = source[same]
        changed_item = changed[same]
        if isinstance(source_item, dict) and isinstance(changed_item, dict):
            full_diff[same] = build_diff_tree(source_item, changed_item)
        elif source_item == changed[same]:
            full_diff[same] = make_leaf(UNCHANGED, source_item)
        else:
            full_diff[same] = make_leaf(CHANGED, changed_item, source_item)

    return full_diff


def make_leaf(type_: str, leaf_value, old_value=None):
    """Crete full diff leaf."""  # noqa: DAR
    return {'type_': type_, 'value': leaf_value, 'old_value': old_value}
