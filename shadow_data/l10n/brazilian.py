from shadow_data.anonymization import TextProcessor
from shadow_data.utils import only_digits

class IdentifierAnonymizer:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.clean_identifier = only_digits(identifier)

    def anonymize(self) -> str:
        if len(self.clean_identifier) == 11:  # CPF
            return self._anonymize_cpf()
        elif len(self.clean_identifier) == 14:  # CNPJ
            return self._anonymize_cnpj()
        else:
            raise ValueError("Invalid identifier length")

    def _anonymize_cpf(self) -> str:
        return TextProcessor.replace_text(r"(\d{2})(\d{9})", r"\1*********", self.clean_identifier)

    def _anonymize_cnpj(self) -> str:
        return TextProcessor.replace_text(r"(\d{2})(\d{12})", r"\1************", self.clean_identifier)
