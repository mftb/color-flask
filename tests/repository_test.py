import pytest
from unittest.mock import patch

from repository import ColorRepository, ColorIOException, ColorNotFoundException, ColorAlreadyExistsException


def test_create_color_repository():
    """
    Test if the ColorRepository can be created.
    """
    ColorRepository()


def test_repository_all_colors():
    repo = ColorRepository()
    assert isinstance(repo.all_colors(), str)


def test_repository_get_color():
    repo = ColorRepository()
    assert isinstance(repo.get_color("red"), str)


def test_repository_get_color_not_found():
    repo = ColorRepository()
    with pytest.raises(ColorNotFoundException):
        repo.get_color("fuchsia")


def test_repository_insert_color():
    repo = ColorRepository()
    color = {
        "color": "fuchsia",
        "value": "#abc"
    }
    repo.insert_color(color)
    assert isinstance(repo.get_color("fuchsia"), str)


def test_repository_insert_already_existing_color():
    repo = ColorRepository()
    color = {
        "color": "red",
        "value": "#abc"
    }
    with pytest.raises(ColorAlreadyExistsException):
        repo.insert_color(color)


def test_repository_insert_io_error():
    repo = ColorRepository()
    color = {
        "color": "fuchsia",
        "value": "#abc"
    }
    with patch('repository.open', side_effect=Exception('IO Error')):
        with pytest.raises(ColorIOException):
            repo.insert_color(color)
