from app.io.input import *
from app.io.output import *


def main():
    text_from_console = read_from_console()
    text_from_file = read_from_file('./data/text.txt')
    text_from_file_pandas = read_from_file_pandas('./data/jsn.json')

    write_to_console(f"text from console: {text_from_console}\n")
    write_to_console(f"text from file:\n{text_from_file}")
    write_to_console(f"text from file with pandas:\n{text_from_file_pandas}")

    write_to_file("./data/output.txt",
                  f"text from console: {text_from_console}\n\n" +
                  f"text from file:\n{text_from_file}\n" +
                  f"text from file with pandas:\n{text_from_file_pandas}\n")


if __name__ == "__main__":
    main()