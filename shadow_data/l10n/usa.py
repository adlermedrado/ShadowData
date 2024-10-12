import re

from shadow_data.l10n.ClearIdentifier import ClearIdentifier


class IdentifierAnonymizer(ClearIdentifier):
    def anonymize(self):
        ssn_pattern = r'\b(\d{3})-(\d{2})-(\d{4})\b'
        self.cleaned_content = re.sub(ssn_pattern, r'XXX-XX-\3', self.content_to_anonymize)
