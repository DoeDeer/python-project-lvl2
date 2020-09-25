# -*- coding: utf-8 -*-


"""Flat json diff tests."""


import json

import pytest

from gendiff.core import gendiff
from gendiff.formatting import JSON_LIKE_FORMAT, PLAIN_FORMAT


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
    with open('tests/fixtures/flat_json_like_result.txt') as res:
        return res.read()


@pytest.fixture
def plain_flat_res():
    with open('tests/fixtures/flat_plain_result.txt') as res:
        return res.read()


@pytest.fixture
def json_flat_res():
    with open('tests/fixtures/flat_json_result.json') as res:
        return json.load(res)


def test_json_like_flat_json(
    before_json_flat: str,
    after_json_flat: str,
    json_like_flat_res: str,
):
    """Test flat json files comparing."""
    assert gendiff(
        before_json_flat,
        after_json_flat,
        form=JSON_LIKE_FORMAT,
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
        form=JSON_LIKE_FORMAT,
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
        form=PLAIN_FORMAT,
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
        form=PLAIN_FORMAT,
    ) == plain_flat_res


def test_json_flat_json(
    before_json_flat,
    after_json_flat,
    json_flat_res: str,
):
    """Test flat json files comparing in json format."""
    assert json.loads(
        gendiff(before_json_flat, after_json_flat),
    ) == json_flat_res


def test_json_flat_yaml(
    before_yaml_flat: str,
    after_yaml_flat: str,
    json_flat_res: str,
):
    """Test flat yaml files comparing in json format."""
    assert json.loads(
        gendiff(before_yaml_flat, after_yaml_flat),
    ) == json_flat_res
