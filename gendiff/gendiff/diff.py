# -*- coding: utf-8 -*-


"""Module to fund diff between two dicts."""

UNCHANGED = 0
CHANGED = 1
ADDED = 2
REMOVED = 3

KEY_STATES = (UNCHANGED, CHANGED, ADDED, REMOVED)


def diff(source: dict, changed: dict) -> dict:
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
        if source[same] == changed[same]:
            keys_states[same] = UNCHANGED
        else:
            keys_states[same] = CHANGED

    return keys_states
