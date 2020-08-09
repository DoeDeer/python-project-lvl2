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
def before_json_complex_plain():
    return 'tests/fixtures/before_complex_plain.json'


@pytest.fixture
def after_json_complex_plain():
    return 'tests/fixtures/after_complex_plain.json'


@pytest.fixture
def before_yaml_complex():
    return 'tests/fixtures/before_complex.yml'


@pytest.fixture
def after_yaml_complex():
    return 'tests/fixtures/after_complex.yaml'


@pytest.fixture
def complex_res():
    return """{
    host: hexlet.io,
  - proxy: 123.234.53.22,
    request: {
        host: hexlet.io,
      - proxy: 123.234.53.22,
      + timeout: 20,
      - timeout: 50,
      + verbose: true
    },
  + timeout: 20,
  - timeout: 50,
  + verbose: true
}"""


@pytest.fixture
def complex_res_plain():
    return """Property 'common.setting2' was removed
Property 'common.setting6' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: 'complex value'
Property 'common.site.base' was removed
Property 'group1.baz' was changed. From 'bas' to 'bars'
Property 'group2' was removed
Property 'group3' was added with value: 'complex value'
"""


def test_complex_json(
    before_json_complex: str,
    after_json_complex: str,
    complex_res: str,
):
    """Test complex json files comparing."""
    assert gendiff(before_json_complex, after_json_complex) == complex_res


def test_complex_yaml(
    before_yaml_complex: str,
    after_yaml_complex: str,
    complex_res: str,
):
    """Test complex json files comparing."""
    assert gendiff(before_yaml_complex, after_yaml_complex) == complex_res


def test_complex_json_plain(
    before_json_complex_plain: str,
    after_json_complex_plain: str,
    complex_res_plain: str,
):
    """Test complex json files comparing."""
    assert gendiff(
        before_json_complex_plain,
        after_json_complex_plain,
        form='plain',
    ) == complex_res_plain
