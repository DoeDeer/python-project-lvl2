# -*- coding: utf-8 -*-


"""Module with main entities."""

from gendiff.gendiff.files import read_file
from gendiff.gendiff.out_format import prepare_to_show, changes_to_string


def gendiff(ff_path: str, sf_path: str, form: str = 'json') -> str:
    """Generate diff between two files in specified format.

    Args:
        ff_path (str): path to source file.
        sf_path (str): path to changed file.
        form (str): output string format. Choices: json, plain

    Returns:
        str: string with diffs, format as specified.

    """
    source = read_file(ff_path)
    changed = read_file(sf_path)

    changes = prepare_to_show(source, changed)
    return changes_to_string(changes, form=form)
