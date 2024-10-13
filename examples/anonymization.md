# Simple text replacement and IPV4 anonymization

```python
from shadow_data.anonymization import EmailAnonymization, TextProcessor, Ipv4Anonymization, PhoneNumberAnonymization

original_content = 'Little John likes to play with the staff.'
anonymized_content = TextProcessor.replace_text('Little John', 'XXXXXX XXXX', original_content)
print(f'Original content: {original_content} | Anonymized content: {anonymized_content}')

original_ip = '200.189.45.128'
anonymized_content = Ipv4Anonymization.anonymize_ipv4(original_ip)
print(f'Original IP: {original_ip} | Anonymized IP: {anonymized_content}')

original_email = 'john@emailaddress.com'
anonymized_content = EmailAnonymization.anonymize_email(original_email)
print(f'Original Email: {original_email} | Anonymized Email: {anonymized_content}')

original_phone_number = '+55 (11) 91234-5678'
anonymized_content = PhoneNumberAnonymization.anonymize_phone_number(original_phone_number)
print(f'Original Phone: {original_phone_number} | Anonymized Phone: {anonymized_content}')

original_phone_number = '11-91234-5678'
anonymized_content = PhoneNumberAnonymization.anonymize_phone_number(original_phone_number)
print(f'Original Phone: {original_phone_number} | Anonymized Phone: {anonymized_content}')
```

### Results:

```plain
Original content: Little John likes to play with the staff. | Anonymized content: XXXXXX XXXX likes to play with the staff.
Original IP: 200.189.45.128 | Anonymized IP: 200.X.X.X
Original Email: john@emailaddress.com | Anonymized Email: ****@*********ess.com
Original Phone: +55 (11) 91234-5678 | Anonymized Phone: +** (**) *****-5678
Original Phone: 11-91234-5678 | Anonymized Phone: **-*****-5678
```