from shadow_data.anonymization import TextProcessor


class TestTextProcessor:
    def test_anonymize_single_term(self):
        original_content = "The user's name is João Silva."
        original_term = 'João Silva'
        to_replace = 'ANONYMOUS'

        expected_output = "The user's name is ANONYMOUS."

        assert TextProcessor.replace_text(original_term, to_replace, original_content) == expected_output

    def test_anonymize_multiple_occurrences(self):
        original_content = 'João Silva bought a car. João Silva sold a house.'
        original_term = 'João Silva'
        to_replace = 'ANONYMOUS'

        expected_output = 'ANONYMOUS bought a car. ANONYMOUS sold a house.'

        assert TextProcessor.replace_text(original_term, to_replace, original_content) == expected_output

    def test_anonymize_no_match(self):
        original_content = "The user's name is Carlos Pereira."
        original_term = 'João Silva'
        to_replace = 'ANONYMOUS'

        expected_output = original_content

        assert TextProcessor.replace_text(original_term, to_replace, original_content) == expected_output

    def test_anonymize_partial_match(self):
        original_content = 'João Silva bought a car. João sold a house.'
        original_term = 'João Silva'
        to_replace = 'ANONYMOUS'

        expected_output = 'ANONYMOUS bought a car. João sold a house.'

        assert TextProcessor.replace_text(original_term, to_replace, original_content) == expected_output
