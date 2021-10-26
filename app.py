from flask import Flask, request, make_response

from controller import ColorController


app = Flask(__name__)
controller = ColorController()


@app.route('/', methods=['GET'])
def all_colors_endpoint():
    return make_response(controller.all_colors())


@app.route('/{color}', methods=['GET'])
def get_color_endpoint(color):
    return make_response(controller.get_color(color))


@app.route('/', methods=['POST'])
def add_color_endpoint(request):
    return make_response(controller.add_color(request.json))


if __name__ == '__main__':
    app.run(debug=True)
