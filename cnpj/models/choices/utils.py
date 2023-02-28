from typing import Tuple

def get_key_by_value(choices: Tuple[Tuple], value: str):
    choices: dict = { value:key for key, value in choices}
    key: int = choices.get(value, None)
    if key == None:
        raise Exception(f"Not Found {value}")
    return key