# Personally Identifiable Information with Natural Language Processing

PII, or Personally Identifiable Information, refers to any data that can be used to identify a specific individual. This includes names, addresses, phone numbers, social security numbers, email addresses, and other personal details that can be linked to a person. Protecting PII is essential for maintaining privacy and ensuring data security.

spaCy is an open-source library for advanced natural language processing (NLP) in Python. It provides fast and efficient tools for tasks like tokenization, part-of-speech tagging, named entity recognition, and more, with support for multiple languages.

This library primarily uses spaCy to process text and identify personally identifiable information (PII).

**_The code sample below is in Portuguese because the results were better than those from the tests I conducted in English._**

```python 
from shadow_data.pii.enums import ModelLang, ModelCore, ModelSize
from shadow_data.pii.spacy import SensitiveData

# content = 'David Thompson lives at 456 Elmwood Drive, Apartment 12A, Springfield, Illinois, 62704. He works as a Project Manager at BrightTech Innovations, a growing tech firm located at 321 Innovation Way, Springfield, IL 62701. David has been with the company for three years, where he manages a team of developers and designers, ensuring projects are delivered on time and meet client expectations. You can contact him by phone at (555) 123-7890 or by email at david.thompson@brighttech.com. David is highly regarded for his leadership and problem-solving skills within the company.'
content = 'João Silva mora na Rua das Acácias, 123, Apartamento 5B, São Paulo, SP, 01310-000. Ele trabalha como Gerente de Projetos na TechNova Soluções, uma empresa de tecnologia em crescimento localizada na Avenida Paulista, 987, São Paulo, SP, 01311-200. João está na empresa há três anos, onde lidera uma equipe de desenvolvedores e designers, garantindo que os projetos sejam entregues no prazo e atendam às expectativas dos clientes. Você pode contatá-lo pelo telefone (11) 91234-5678 ou pelo e-mail joao.silva@technova.com. João é muito respeitado por suas habilidades de liderança e resolução de problemas dentro da empresa.'
instance = SensitiveData()
sensitive_data = instance.identify_sensitive_data(ModelLang.PORTUGUESE, ModelCore.NEWS, ModelSize.LARGE, content)
print(sensitive_data)
```

### Results:
```plain
[('João Silva', 'PER'), ('Rua das Acácias', 'LOC'), ('Apartamento 5B', 'LOC'), ('São Paulo', 'LOC'), ('SP', 'LOC'), ('Gerente de Projetos', 'MISC'), ('TechNova Soluções', 'LOC'), ('Avenida Paulista', 'LOC'), ('São Paulo', 'LOC'), ('SP', 'LOC'), ('João', 'PER'), ('joao.silva@technova.com', 'LOC'), ('João', 'PER')]
```