import pytest

from shadow_data.l10n.brazilian import IdentifierAnonymizer


def test_anonymize_valid_cpf():
    identifier_anonymizer = IdentifierAnonymizer("123.456.789-09")
    assert identifier_anonymizer.anonymize() == "12*********"


def test_anonymize_valid_cnpj():
    identifier_anonymizer = IdentifierAnonymizer("12.345.678/0001-95")
    assert identifier_anonymizer.anonymize() == "12************"


def test_invalid_identifier_short_length():
    with pytest.raises(ValueError):
        identifier_anonymizer = IdentifierAnonymizer("123456789")
        identifier_anonymizer.anonymize()


def test_invalid_identifier_long_length():
    with pytest.raises(ValueError):
        identifier_anonymizer = IdentifierAnonymizer("123456789012345")
        identifier_anonymizer.anonymize()
