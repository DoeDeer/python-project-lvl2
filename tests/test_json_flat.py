# -*- coding: utf-8 -*-


"""Flat json diff tests."""


import pytest

from gendiff.gendiff.core import gendiff


@pytest.fixture
def before_json_flat():
    return 'tests/fixtures/before_flat.json'


@pytest.fixture
def after_json_flat():
    return 'tests/fixtures/after_flat.json'


@pytest.fixture
def flat_json_res():
    return """{
    host: hexlet.io,
  - proxy: 123.234.53.22,
  + timeout: 20,
  - timeout: 50,
  + verbose: true
}"""


def test_flat(before_json_flat: str, after_json_flat: str, flat_json_res: str):
    """Test flat files comparing."""
    assert gendiff(before_json_flat, after_json_flat) == flat_json_res
