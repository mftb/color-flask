import pytest

from validator import color_validator

valid_color = {
    "color": "red",
    "value": "#f00"
}


def test_color_validator_valid_input():
    try:
        color_validator(valid_color)
    except Exception as e:
        pytest.fail("Unexpected MyError ..")


def test_color_validator_bad_input_wrong_keys1():
    bad_color = {
        "name": "red",
        "value": "#f00"
    }
    with pytest.raises(KeyError):
        color_validator(bad_color)


def test_color_validator_bad_input_wrong_keys2():
    bad_color = {
        "color": "red",
        "hex": "#f00"
    }
    with pytest.raises(KeyError):
        color_validator(bad_color)


def test_color_validator_bad_input_wrong_type():
    bad_color = "asdasd"
    with pytest.raises(TypeError):
        color_validator(bad_color)


def test_color_validator_bad_input_wrong_keys_type1():
    bad_color = {
        "color": 123,
        "value": "#f00"
    }
    with pytest.raises(TypeError):
        color_validator(bad_color)


def test_color_validator_bad_input_wrong_keys_type2():
    bad_color = {
        "color": "blue",
        "value": 123
    }
    with pytest.raises(TypeError):
        color_validator(bad_color)
