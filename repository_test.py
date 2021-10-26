import pytest

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
