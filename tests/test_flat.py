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
def before_yaml_flat():
    return 'tests/fixtures/before_flat.yml'


@pytest.fixture
def after_yaml_flat():
    return 'tests/fixtures/after_flat.yaml'


@pytest.fixture
def flat_res():
    return """{
    host: hexlet.io,
  - proxy: 123.234.53.22,
  + timeout: 20,
  - timeout: 50,
  + verbose: true
}"""


def test_flat_json(
    before_json_flat: str,
    after_json_flat: str,
    flat_res: str,
):
    """Test flat json files comparing."""
    assert gendiff(before_json_flat, after_json_flat) == flat_res


def test_flat_yaml(
    before_yaml_flat: str,
    after_yaml_flat: str,
    flat_res: str,
):
    """Test flat json files comparing."""
    assert gendiff(before_yaml_flat, after_yaml_flat) == flat_res
