def color_validator(color):
    if not isinstance(color, dict):
        raise TypeError("color must be a dictionary")
    if "color" not in color:
        raise KeyError("color dictionary must have a 'color' key")
    if "value" not in color:
        raise KeyError("color dictionary must have a 'value' key")
