# Localized anonymization for U.S. Social Security Numbers.

```python
from shadow_data.l10n.usa import IdentifierAnonymizer

text_content_with_ssn = "Billy's SSN is 479-92-5042. Please make sure it's anonymized."
anonymizer = IdentifierAnonymizer(text_content_with_ssn)
anonymizer.anonymize()

print(f'Original: {text_content_with_ssn} | Anonymized: {anonymizer.cleaned_content}')
```

### Results

```plain
Original: Billy's SSN is 479-92-5042. Please make sure it's anonymized. | Anonymized: Billy's SSN is XXX-XX-5042. Please make sure it's anonymized.
```