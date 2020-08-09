# -*- coding: utf-8 -*-


"""Module with main entities."""

from gendiff.gendiff.diff import diff_dicts
from gendiff.gendiff.files import read_file
from gendiff.gendiff.formatting import JSON_FORMAT, format_output


def gendiff(ff_path: str, sf_path: str, form: str = JSON_FORMAT) -> str:
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

    changes = diff_dicts(source, changed)
    return format_output(changes, format_=form)
