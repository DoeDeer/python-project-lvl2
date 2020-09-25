#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main executable file."""

from gendiff.core import gendiff, parser


def main():
    """Execute program."""
    args = parser.parse_args()
    print(gendiff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
