#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main executable file."""


import argparse

from gendiff.gendiff.core import gendiff


def main():
    """Execute program."""
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
        choices=['json', 'json-like', 'plain'],
        default='json',
        metavar='FORMAT',
        help='set format of output. Available choices: plain, json, json-like',
    )

    args = parser.parse_args()
    print(gendiff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
