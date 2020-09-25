# -*- coding: utf-8 -*-


"""Module with utils to work with files."""

import json
import os
from typing import Optional, Union

import yaml

JSON_EXT = '.json'
YAML_EXT = ('.yml', '.yaml')
EXTENSIONS = (JSON_EXT, YAML_EXT)
EXT_READERS = {  # noqa: WPS407
    JSON_EXT: json.load,
    YAML_EXT: yaml.safe_load,
}


def guess_extension(file_name: str) -> Optional[Union[str, tuple]]:
    """Return file extension if json or yaml, None instead."""
    if file_name.lower().endswith(JSON_EXT):
        return JSON_EXT
    if any(file_name.lower().endswith(ext) for ext in YAML_EXT):
        return YAML_EXT


def read_file(file_path: str) -> Optional[dict]:
    """Read json or yaml and convert to python dict."""
    mime = guess_extension(file_path)
    if mime not in EXTENSIONS:
        raise ValueError('Wrong file extension')

    reader = EXT_READERS[mime]
    abs_path = os.path.abspath(file_path)
    with open(abs_path, 'rb') as source_file:
        read_dict = reader(source_file)

    return read_dict
