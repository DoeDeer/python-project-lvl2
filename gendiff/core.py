# -*- coding: utf-8 -*-


"""Module with main entities."""

import argparse

from gendiff.diff import build_diff_tree
from gendiff.files import read_file
from gendiff.formatting import (
    JSON_FORMAT,
    JSON_LIKE_FORMAT,
    PLAIN_FORMAT,
    format_output,
)

parser = argparse.ArgumentParser(
    description='Generate diff between two files in specified format',
)
parser.add_argument('first_file', type=str, help='source file')
parser.add_argument('second_file', type=str, help='changed file')
parser.add_argument(
    '-f',
    '--format',
    type=str,
    action='store',
    choices=[JSON_FORMAT, JSON_LIKE_FORMAT, PLAIN_FORMAT],
    default=JSON_LIKE_FORMAT,
    metavar='FORMAT',
    help='set format of output. Available choices: plain, json, json-like',
)


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

    changes = build_diff_tree(source, changed)
    return format_output(changes, format_=form)
