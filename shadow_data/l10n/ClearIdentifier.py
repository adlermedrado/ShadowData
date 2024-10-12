from abc import ABC, abstractmethod


class ClearIdentifier(ABC):
    cleaned_content: str

    def __init__(self, content_to_anonymize):
        self.content_to_anonymize = content_to_anonymize

    @abstractmethod
    def anonymize(self):
        pass
