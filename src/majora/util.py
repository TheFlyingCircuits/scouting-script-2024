def extract_max_value(values_as_text: str) -> int:
    split_values = values_as_text.split(';')

    max_value = 0
    for value in split_values:
        value = int(value)
        if value > max_value:
            max_value = value

    return max_value
