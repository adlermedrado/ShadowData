from shadow_data.l10n.usa import IdentifierAnonymizer


class TestIdentifierAnonymizer:
    def test_anonymize_ssn(self):
        content = 'My SSN is 123-45-6789.'
        expected_output = 'My SSN is XXX-XX-6789.'
        anonymizer = IdentifierAnonymizer(content)
        anonymizer.anonymize()
        assert anonymizer.cleaned_content == expected_output

    def test_anonymize_multiple_ssns(self):
        content = 'SSNs are 123-45-6789 and 987-65-4321.'
        expected_output = 'SSNs are XXX-XX-6789 and XXX-XX-4321.'
        anonymizer = IdentifierAnonymizer(content)
        anonymizer.anonymize()
        assert anonymizer.cleaned_content == expected_output

    def test_anonymize_no_ssn(self):
        content = 'There is no SSN here.'
        expected_output = 'There is no SSN here.'
        anonymizer = IdentifierAnonymizer(content)
        anonymizer.anonymize()
        assert anonymizer.cleaned_content == expected_output

    def test_anonymize_partial_ssn(self):
        content = 'Partial SSN 123-45 is not complete.'
        expected_output = 'Partial SSN 123-45 is not complete.'
        anonymizer = IdentifierAnonymizer(content)
        anonymizer.anonymize()
        assert anonymizer.cleaned_content == expected_output

    def test_anonymize_invalid_ssn_format(self):
        content = 'Invalid SSN 1234-56-7890.'
        expected_output = 'Invalid SSN 1234-56-7890.'
        anonymizer = IdentifierAnonymizer(content)
        anonymizer.anonymize()
        assert anonymizer.cleaned_content == expected_output
