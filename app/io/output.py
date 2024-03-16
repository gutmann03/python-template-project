
def write_to_console(text: str):
    """ Writes text into console.

        Args:
            text (str): The text to be written in concole.

        Raises:
            TypeError: If parameter text is not a string.

        Examples:
            >>> write_to_console('hello')
    """
    if not isinstance(text, str):
        raise TypeError('parameter must be string type.')

    print(text)


def write_to_file(file_path: str, text: str):
    """ Writes text into console.

        Args:
            file_path (str): The file path, where text is to be written.
            text (str): The text to be written in file.

        Raises:
            TypeError: If parameters are not a string.

        Examples:
            >>> write_to_file('file_path', 'hello')
    """
    if not isinstance(text, str) or not isinstance(file_path, str):
        raise TypeError('parameters must be string type.')

    with open(file_path, "w") as file:
        file.write(text)
