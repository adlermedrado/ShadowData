import pytest

from shadow_data.l10n.ClearIdentifier import ClearIdentifier
from shadow_data.l10n.brazil import IdentifierAnonymizer


class TestIdentifierAnonymizer:
    def test_anonymize_valid_cpf(self):
        identifier_anonymizer = IdentifierAnonymizer('123.456.789-09')
        identifier_anonymizer.anonymize()
        assert identifier_anonymizer.cleaned_content == '12*********'

    def test_anonymize_valid_cnpj(self):
        identifier_anonymizer = IdentifierAnonymizer('12.345.678/0001-95')
        identifier_anonymizer.anonymize()
        assert identifier_anonymizer.cleaned_content == '12************'

    def test_invalid_identifier_short_length(self):
        with pytest.raises(ValueError):
            identifier_anonymizer = IdentifierAnonymizer('123456789')
            identifier_anonymizer.anonymize()

    def test_invalid_identifier_long_length(self):
        with pytest.raises(ValueError):
            identifier_anonymizer = IdentifierAnonymizer('123456789012345')
            identifier_anonymizer.anonymize()
