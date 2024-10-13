from shadow_data.utils import only_digits


class TestOnlyDigits:
    def test_only_digits_with_numbers_and_letters(self):
        assert only_digits('abc123') == '123'

    def test_only_digits_with_only_numbers(self):
        assert only_digits('123456') == '123456'

    def test_only_digits_with_special_characters(self):
        assert only_digits('!@#123$%^') == '123'

    def test_only_digits_with_no_numbers(self):
        assert only_digits('abcdef') == ''

    def test_only_digits_with_empty_string(self):
        assert only_digits('') == ''

    def test_only_digits_with_spaces(self):
        assert only_digits(' 1 2 3 ') == '123'
