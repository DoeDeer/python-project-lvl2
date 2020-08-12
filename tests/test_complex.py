# -*- coding: utf-8 -*-


"""complex json diff tests."""


import pytest

from gendiff.gendiff.core import gendiff


@pytest.fixture
def before_json_complex():
    return 'tests/fixtures/before_complex.json'


@pytest.fixture
def after_json_complex():
    return 'tests/fixtures/after_complex.json'


@pytest.fixture
def before_yaml_complex():
    return 'tests/fixtures/before_complex.yml'


@pytest.fixture
def after_yaml_complex():
    return 'tests/fixtures/after_complex.yaml'


@pytest.fixture
def complex_res_json_like():
    return """{
    common: {
        setting1: Value 1,
      - setting2: 200,
        setting3: true,
      + setting4: blah blah,
      + setting5: {key5: value5},
      - setting6: {key: value}
    },
    group1: {
      + baz: bars,
      - baz: bas,
        foo: bar
    },
  - group2: {abc: 12345},
  + group3: {fee: 100500}
}"""


@pytest.fixture
def complex_res_plain():
    return """Property 'common.setting2' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'common.setting6' was removed
Property 'group1.baz' was changed. From 'bas' to 'bars'
Property 'group2' was removed
Property 'group3' was added with value: 'complex value'
"""


@pytest.fixture
def complex_res_json():
    return """{
    "common": {
        "setting1": {
            "old_value": null,
            "type": "UNCHANGED",
            "value": "Value 1"
        },
        "setting2": {
            "old_value": null,
            "type": "REMOVED",
            "value": "200"
        },
        "setting3": {
            "old_value": null,
            "type": "UNCHANGED",
            "value": true
        },
        "setting4": {
            "old_value": null,
            "type": "ADDED",
            "value": "blah blah"
        },
        "setting5": {
            "old_value": null,
            "type": "ADDED",
            "value": {
                "key5": "value5"
            }
        },
        "setting6": {
            "old_value": null,
            "type": "REMOVED",
            "value": {
                "key": "value"
            }
        }
    },
    "group1": {
        "baz": {
            "old_value": "bas",
            "type": "CHANGED",
            "value": "bars"
        },
        "foo": {
            "old_value": null,
            "type": "UNCHANGED",
            "value": "bar"
        }
    },
    "group2": {
        "old_value": null,
        "type": "REMOVED",
        "value": {
            "abc": "12345"
        }
    },
    "group3": {
        "old_value": null,
        "type": "ADDED",
        "value": {
            "fee": "100500"
        }
    }
}"""


def test_json_like_complex_json(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_json_like: str,
):
    """Test complex json files comparing in json-like format."""
    assert gendiff(
        before_json_complex,
        after_json_complex,
        'json-like',
    ) == complex_res_json_like


def test_json_like__complex_yaml(
    before_yaml_complex: str,
    after_yaml_complex: str,
    complex_res_json_like: str,
):
    """Test complex yaml files comparing in json-like format."""
    assert gendiff(
        before_yaml_complex,
        after_yaml_complex,
        'json-like',
    ) == complex_res_json_like


def test_plain_complex_json(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_plain: str,
):
    """Test complex json files comparing in plain format."""
    assert gendiff(
        before_json_complex,
        after_json_complex,
        form='plain',
    ) == complex_res_plain


def test_plain_complex_yaml(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_plain: str,
):
    """Test complex json files comparing in plain format."""
    assert gendiff(
        before_json_complex,
        after_json_complex,
        form='plain',
    ) == complex_res_plain


def test_json_complex_json(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_json: str,
):
    """Test complex json files comparing in json format."""
    assert gendiff(before_json_complex, after_json_complex) == complex_res_json


def test_json_complex_yaml(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_json: str,
):
    """Test complex json files comparing in json format."""
    assert gendiff(before_json_complex, after_json_complex) == complex_res_json
