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
def json_like_flat_res():
    return """{
    host: hexlet.io,
  - proxy: 123.234.53.22,
  + timeout: 20,
  - timeout: 50,
  + verbose: true
}"""


@pytest.fixture
def plain_flat_res():
    return """Property 'proxy' was removed
Property 'timeout' was changed. From '50' to '20'
Property 'verbose' was added with value: 'true'
"""


@pytest.fixture
def json_flat_res():
    return """{
    "host": {
        "old_value": null,
        "type_": "UNCHANGED",
        "value": "hexlet.io"
    },
    "proxy": {
        "old_value": null,
        "type_": "REMOVED",
        "value": "123.234.53.22"
    },
    "timeout": {
        "old_value": 50,
        "type_": "CHANGED",
        "value": 20
    },
    "verbose": {
        "old_value": null,
        "type_": "ADDED",
        "value": true
    }
}"""


def test_json_like_flat_json(
    before_json_flat: str,
    after_json_flat: str,
    json_like_flat_res: str,
):
    """Test flat json files comparing."""
    assert gendiff(
        before_json_flat,
        after_json_flat,
        'json-like'
    ) == json_like_flat_res


def test_json_like_flat_yaml(
    before_yaml_flat: str,
    after_yaml_flat: str,
    json_like_flat_res: str,
):
    """Test flat yaml files comparing."""
    assert gendiff(
        before_yaml_flat,
        after_yaml_flat,
        'json-like',
    ) == json_like_flat_res


def test_plain_flat_json(
    before_json_flat: str,
    after_json_flat: str,
    plain_flat_res: str,
):
    """Test flat json files comparing in plain format."""
    assert gendiff(
        before_json_flat,
        after_json_flat,
        form='plain',
    ) == plain_flat_res


def test_plain_flat_yaml(
    before_yaml_flat: str,
    after_yaml_flat: str,
    plain_flat_res: str,
):
    """Test flat yaml files comparing in plain format."""
    assert gendiff(
        before_yaml_flat,
        after_yaml_flat,
        form='plain',
    ) == plain_flat_res


def test_json_flat_json(
    before_json_flat,
    after_json_flat,
    json_flat_res: str,
):
    """Test flat json files comparing in json format."""
    assert gendiff(before_json_flat, after_json_flat) == json_flat_res


def test_json_flat_yaml(
    before_yaml_flat: str,
    after_yaml_flat: str,
    json_flat_res: str,
):
    """Test flat yaml files comparing in json format."""
    assert gendiff(before_yaml_flat, after_yaml_flat) == json_flat_res
