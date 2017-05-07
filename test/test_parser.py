from __future__ import unicode_literals

import io

import pytest

import pytoml as toml


def test_name_of_fileobj_is_used_in_errors():
    source = io.StringIO("[")
    source.name = "<source>"
    error = pytest.raises(toml.TomlError, lambda: toml.load(source))
    assert error.value.filename == "<source>"


def test_when_fileobj_has_no_name_attr_then_repr_of_fileobj_is_used_in_errors():
    source = io.StringIO("[")
    error = pytest.raises(toml.TomlError, lambda: toml.load(source))
    assert error.value.filename == repr(source)
