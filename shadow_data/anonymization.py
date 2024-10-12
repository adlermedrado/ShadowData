import re


class TextProcessor:
    @staticmethod
    def replace_text(original_term: str, to_replace: str, original_content: str) -> str:
        return re.sub(original_term, to_replace, original_content)


class Ipv4Anonymization:
    @staticmethod
    def anonymize_ipv4(text: str, pattern: str = r'\1.X.X.X') -> str:
        return TextProcessor.replace_text(r'\b(\d{1,3})(\.\d{1,3}){3}\b', pattern, text)
