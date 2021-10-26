import pytest
from unittest.mock import patch

from controller import ColorController


default_headers = {'Content-Type': 'application/json'}


def test_create_color_controller():
    controller = ColorController()


def test_all_colors():
    controller = ColorController()
    colors, status, headers = controller.all_colors()
    assert status == 200
    assert headers == default_headers
    assert isinstance(colors, str)


def test_get_existing_color():
    controller = ColorController()
    color, status, headers = controller.get_color('red')
    assert status == 200
    assert headers == default_headers
    assert isinstance(color, str)


def test_get_non_existing_color():
    controller = ColorController()
    error, status, headers = controller.get_color('abc')
    assert status == 404
    assert headers == default_headers
    assert isinstance(error, dict)


def test_add_color():
    controller = ColorController()
    new_color = {
        "color": "fuchsia",
        "value": "#abc"
    }
    color, status, headers = controller.add_color(new_color)
    assert status == 201
    assert headers == default_headers
    assert isinstance(color, dict)


def test_add_color_bad_payload1():
    controller = ColorController()
    new_color = {
        "name": "fuchsia",
        "value": "#abc"
    }
    color, status, headers = controller.add_color(new_color)
    assert status == 400
    assert headers == default_headers
    assert isinstance(color, dict)


def test_add_color_bad_payload2():
    controller = ColorController()
    new_color = {
        "color": 123,
        "value": "#abc"
    }
    color, status, headers = controller.add_color(new_color)
    assert status == 400
    assert headers == default_headers
    assert isinstance(color, dict)


def test_add_color_color_exists():
    controller = ColorController()
    new_color = {
        "color": "red",
        "value": "#abc"
    }
    color, status, headers = controller.add_color(new_color)
    assert status == 409
    assert headers == default_headers
    assert isinstance(color, dict)


def test_add_color_io_error():
    controller = ColorController()
    new_color = {
        "color": "fuchsia",
        "value": "#abc"
    }
    with patch('repository.open', side_effect=Exception('IO Error')):
        color, status, headers = controller.add_color(new_color)
        assert status == 503
        assert headers == default_headers
        assert isinstance(color, dict)
