from json import loads, dumps
from copy import deepcopy


class ColorNotFoundException(Exception):
    pass


class ColorIOException(Exception):
    pass


class ColorAlreadyExistsException(Exception):
    pass


class ColorRepository:
    """
    Color repository class
    """

    __colors_file = "colors.json"

    def __init__(self):
        """
        Constructor
        """
        with open(self.__colors_file, 'r') as file:
            self.__colors = loads(file.read())

    def get_colors(self):
        """
        Get colors
        :return: colors
        """
        return self.__colors

    def get_color(self, color_name):
        """
        Get color
        :param color_name: color name
        :return: color
        """
        for color in self.__colors:
            if color['name'] == color_name:
                return color
        raise ColorNotFoundException("Color not found")

    def insert_color(self, color):
        """
        Insert color
        :param color: color
        :return: None
        """
        old_colors = deepcopy(self.__colors)
        for my_color in self.__colors:
            if my_color['name'] == color['name']:
                raise ColorAlreadyExistsException("Color already exists")
        self.__colors.append(color)
        try:
            with open(self.__colors_file, 'w') as file:
                file.write(dumps(self.__colors))
        except Exception as e:
            self.__colors = old_colors
            raise ColorIOException(e)
