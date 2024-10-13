import pytest

from shadow_data.anonymization import EmailAnonymization
from shadow_data.exceptions import InvalidEmailError


class TestEmailAnonymization:
    def test_anonymize_email_valid(self):
        email = 'user@example.com'
        expected = '****@****ple.com'
        result = EmailAnonymization.anonymize_email(email)
        assert result == expected

    def test_anonymize_email_short_domain(self):
        email = 'user@ex.com'
        expected = '****@ex.com'
        result = EmailAnonymization.anonymize_email(email)
        assert result == expected

    def test_anonymize_email_no_domain(self):
        email = 'user@'
        with pytest.raises(InvalidEmailError):
            EmailAnonymization.anonymize_email(email)

    def test_anonymize_email_no_user(self):
        email = '@example.com'
        with pytest.raises(InvalidEmailError):
            EmailAnonymization.anonymize_email(email)

    def test_anonymize_email_invalid_format(self):
        email = 'userexample.com'
        with pytest.raises(InvalidEmailError):
            EmailAnonymization.anonymize_email(email)
