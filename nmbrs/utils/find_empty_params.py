def find_empty_params(**kwargs):
    empty_params = []
    for param_name, param_value in kwargs.items():
        if param_value is None or param_value == "":
            empty_params.append(param_name)
    return empty_params
