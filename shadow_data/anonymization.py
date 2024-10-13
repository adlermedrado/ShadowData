import re

from shadow_data.exceptions import InvalidEmailError


class TextProcessor:
    @staticmethod
    def replace_text(original_term: str, to_replace: str, original_content: str) -> str:
        return re.sub(original_term, to_replace, original_content)


class Ipv4Anonymization:
    @staticmethod
    def anonymize_ipv4(text: str, pattern: str = r'\1.X.X.X') -> str:
        return TextProcessor.replace_text(r'\b(\d{1,3})(\.\d{1,3}){3}\b', pattern, text)


class EmailAnonymization:
    @staticmethod
    def anonymize_email(email: str) -> str:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_regex, email):
            raise InvalidEmailError()

        user, domain = email.split('@')
        anonymized_user = '*' * len(user)
        domain_parts = domain.split('.')
        anonymized_domain = (
            '*' * (len(domain_parts[0]) - 3) + domain_parts[0][-3:] + '.' + '.'.join(domain_parts[1:])
        )

        return f'{anonymized_user}@{anonymized_domain}'
