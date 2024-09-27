import re


def anonymize(original_term: str, to_replace: str, original_content: str) -> str:
    return re.sub(original_term, to_replace, original_content)
