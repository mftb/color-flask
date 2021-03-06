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
    __repo_file = "repo.json"

    def __init__(self):
        """
        Constructor
        """
        with open(self.__colors_file, 'r') as file:
            self.__colors = loads(file.read())
        with open(self.__repo_file, 'w') as file:
            file.write(dumps(self.__colors))

    def all_colors(self):
        """
        Get colors
        :return: colors
        """
        return dumps(self.__colors)

    def get_color(self, color_name):
        """
        Get color
        :param color_name: color name
        :return: color
        """
        for color in self.__colors:
            if color['color'] == color_name:
                return dumps(color)
        raise ColorNotFoundException("Color not found")

    def insert_color(self, color):
        """
        Insert color
        :param color: color
        :return: None
        """
        old_colors = deepcopy(self.__colors)
        for my_color in self.__colors:
            if my_color['color'] == color['color']:
                raise ColorAlreadyExistsException("Color already exists")
        self.__colors.append(color)
        try:
            with open(self.__repo_file, 'w') as file:
                file.write(dumps(self.__colors))
        except Exception as e:
            self.__colors = old_colors
            raise ColorIOException(e)
