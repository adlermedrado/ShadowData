# Localized anonymization for Brazilian individual (CPF) and corporate (CNPJ) tax IDs.

```python
from shadow_data.l10n.brazil import IdentifierAnonymizer

# Anonymize CPF

cpf = '806.846.761-09'
cpf_anonymized = IdentifierAnonymizer(cpf)
cpf_anonymized.anonymize()
print(f'Original CPF: {cpf} : Anonymized CPF: {cpf_anonymized.cleaned_content}')

cnpj = '26.283.050/0001-17'
cnpj_anonymized = IdentifierAnonymizer(cnpj)
cnpj_anonymized.anonymize()
print(f'Original CNPJ: {cnpj} : Anonymized CPF: {cnpj_anonymized.cleaned_content}')
```

### Results

```plain
Original CPF: 806.846.761-09 : Anonymized CPF: 80*********
Original CNPJ: 26.283.050/0001-17 : Anonymized CPF: 26************
```
