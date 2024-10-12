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