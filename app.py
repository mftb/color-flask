from flask import Flask, request, make_request

from controller import ColorController


app = Flask(__name__)
controller = ColorController()


@app.route('/', methods=['GET'])
def all_colors_endpoint():
    return controller.all_colors()


@app.route('/{color}', methods=['GET'])
def get_color_endpoint(color):
    return controller.get_color(color)


@app.route('/', methods=['POST'])
def get_color_endpoint(request):
    return controller.get_color(request.json)


if __name__ == '__main__':
    app.run(debug=True)
