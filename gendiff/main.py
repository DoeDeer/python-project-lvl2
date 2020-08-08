#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main executable file."""


import argparse


def main():
    """Execute program."""
    parser = argparse.ArgumentParser(
        description='Generate diff between two files in specified format',
    )
    parser.add_argument('first_file', type=str, help='Source file')
    parser.add_argument('second_file', type=str, help='Changed file')

    args = parser.parse_args()


if __name__ == '__main__':
    main()
