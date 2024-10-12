import re


def only_digits(content: str) -> str:
    return re.sub(r'\D', '', content)
