import pandas as pd


def read_from_console():
    """ Reads text from console.

        Returns:
            String: The user input.

        Examples:
            >>> read_from_console()
            "hello world"
    """
    return input("write your text: ")


def read_from_file(file_path: str):
    """ Reads text from the file.

        Args:
            file_path (str): The file path, from the text is to be read.

        Returns:
            String: The file content.

        Raises:
            TypeError: If parameter is not a string.

        Examples:
            >>> read_from_file()
            "hello world"
    """
    if not isinstance(file_path, str):
        raise TypeError('parameter must be string type.')

    with open(file_path, "r") as file:
        return file.read()


def read_from_file_pandas(file_path: str):
    """ Reads json from the file using pandas.

        Args:
            file_path (str): The file path, from the json is to be read.

        Returns:
            String: The file json content.

        Raises:
            TypeError: If parameter is not a string.

        Examples:
            >>> read_from_file()
            "hello world"
    """
    if not isinstance(file_path, str):
        raise TypeError('parameter must be string type.')

    return pd.read_json(file_path)
