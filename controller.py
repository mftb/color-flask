from repository import ColorRepository, ColorNotFoundException, ColorIOException, ColorAlreadyExistsException
from validator import color_validator


class ColorController:
    __headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.__repository = ColorRepository()

    def all_colors(self):
        return self.__repository.all_colors(), 200, self.__headers

    def get_color(self, color_name):
        try:
            return self.__repository.get_color(color_name), 200, self.__headers
        except ColorNotFoundException:
            return {"error": "Color not found"}, 404, self.__headers

    def add_color(self, color):
        try:
            color_validator(color)
            self.__repository.insert_color(color)
            return {"message": "Color added"}, 201, self.__headers
        except ColorIOException:
            return {"message": "Error while saving color"}, 503, self.__headers
        except ColorAlreadyExistsException:
            return {"message": "Color already exists"}, 409, self.__headers
        except TypeError:
            return {"message": "Invalid color data"}, 400, self.__headers
        except KeyError:
            return {"message": "Invalid color data"}, 400, self.__headers
