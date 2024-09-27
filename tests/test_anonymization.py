from shadow_data.anonymization import anonymize

def test_anonymize_single_term():
    original_content = "The user's name is João Silva."
    original_term = "João Silva"
    to_replace = "ANONYMOUS"

    expected_output = "The user's name is ANONYMOUS."

    assert anonymize(original_term, to_replace, original_content) == expected_output

def test_anonymize_multiple_occurrences():
    original_content = "João Silva bought a car. João Silva sold a house."
    original_term = "João Silva"
    to_replace = "ANONYMOUS"

    expected_output = "ANONYMOUS bought a car. ANONYMOUS sold a house."

    assert anonymize(original_term, to_replace, original_content) == expected_output

def test_anonymize_no_match():
    original_content = "The user's name is Carlos Pereira."
    original_term = "João Silva"
    to_replace = "ANONYMOUS"

    expected_output = original_content

    assert anonymize(original_term, to_replace, original_content) == expected_output

def test_anonymize_partial_match():
    original_content = "João Silva bought a car. joão silva sold a house."
    original_term = "João Silva"
    to_replace = "ANONYMOUS"

    expected_output = "ANONYMOUS bought a car. joão silva sold a house."

    assert anonymize(original_term, to_replace, original_content) == expected_output