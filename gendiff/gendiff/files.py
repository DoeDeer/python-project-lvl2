# -*- coding: utf-8 -*-


"""Module with utils to work with files."""

import json
import os
from typing import Optional

import yaml

JSON_MIME = 'json'
YAML_MIME = 'yaml'
MIMES = (JSON_MIME, YAML_MIME)
MIMES_READERS = {  # noqa: WPS407
    JSON_MIME: json.load,
    YAML_MIME: yaml.safe_load,
}


def guess_mime(file_name: str) -> Optional[str]:
    """Return file mimetype if json or yaml, None instead."""
    if file_name.endswith('.json'):
        return JSON_MIME
    if any(file_name.endswith(ext) for ext in ('yml', 'yaml')):
        return YAML_MIME


def read_file(file_path: str) -> Optional[dict]:
    """Read json or yaml and convert to python dict."""
    mime = guess_mime(file_path)
    if mime not in MIMES:
        return None

    reader = MIMES_READERS[mime]
    abs_path = os.path.abspath(file_path)
    with open(abs_path, 'rb') as source_file:
        read_dict = reader(source_file)

    return read_dict
