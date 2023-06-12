class CusteomException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CusteomException("This is a custom exception.")
except CusteomException as e:
    print(f"Error : {e.message}")