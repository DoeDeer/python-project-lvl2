# -*- coding: utf-8 -*-


"""complex json diff tests."""


import json

import pytest

from gendiff.core import gendiff
from gendiff.formatting import JSON_LIKE_FORMAT, PLAIN_FORMAT


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
    with open('tests/fixtures/complex_json_like_result.txt') as res:
        return res.read()


@pytest.fixture
def complex_res_plain():
    with open('tests/fixtures/complex_plain_result.txt') as res:
        return res.read()


@pytest.fixture
def complex_res_json():
    with open('tests/fixtures/complex_json_result.json') as res:
        return json.load(res)


def test_json_like_complex_json(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_json_like: str,
):
    """Test complex json files comparing in json-like format."""
    assert gendiff(
        before_json_complex,
        after_json_complex,
        form=JSON_LIKE_FORMAT,
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
        form=JSON_LIKE_FORMAT,
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
        form=PLAIN_FORMAT,
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
        form=PLAIN_FORMAT,
    ) == complex_res_plain


def test_json_complex_json(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_json: str,
):
    """Test complex json files comparing in json format."""
    assert json.loads(
               gendiff(before_json_complex, after_json_complex),
           ) == complex_res_json


def test_json_complex_yaml(
    before_json_complex: str,
    after_json_complex: str,
    complex_res_json: str,
):
    """Test complex json files comparing in json format."""
    assert json.loads(
               gendiff(before_json_complex, after_json_complex),
           ) == complex_res_json
