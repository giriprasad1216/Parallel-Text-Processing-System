def load_text(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text


def split_lines(text):
    return text.split("\n")


def to_lowercase(text):
    return text.lower()
