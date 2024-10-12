import spacy
import subprocess

from spacy.language import Language

from shadow_data.pii.enums import ModelLang, ModelCore, ModelSize


class ModelSelector:
    @staticmethod
    def select(lang: ModelLang, core: ModelCore, size: ModelSize) -> Language:
        """
        Loads a spaCy model by combining language, core news, and size.

        Parameters:
        - lang (ModelLang): The language model.
        - core (ModelCoreNews): The core news model.
        - size (ModelSize): The size of the model.

        Returns:
        - nlp: The loaded spaCy model.

        Raises:
        - TypeError: If any of the parameters are not of the expected type.
        """
        if not isinstance(lang, ModelLang):
            raise TypeError(f'Expected lang to be an instance of ModelLang, got {type(lang).__name__}')
        if not isinstance(core, ModelCore):
            raise TypeError(f'Expected core to be an instance of ModelCoreNews, got {type(core).__name__}')
        if not isinstance(size, ModelSize):
            raise TypeError(f'Expected size to be an instance of ModelSize, got {type(size).__name__}')

        model_name = f'{lang.value}_{core.value}_{size.value}'
        try:
            nlp = spacy.load(model_name)
        except OSError:
            try:
                subprocess.run(['python', '-m', 'spacy', 'download', model_name], check=True)
                nlp = spacy.load(model_name)
            except subprocess.CalledProcessError:
                raise RuntimeError(f'Could not download and load model {model_name}')
        return nlp


class SensitiveData:
    def set_model(self, model_lang: ModelLang, model_core: ModelCore, model_size: ModelSize) -> Language:
        model_selector = ModelSelector()
        return model_selector.select(model_lang, model_core, model_size)

    def identify_sensitive_data(
        self, model_lang: ModelLang, model_core: ModelCore, model_size: ModelSize, content
    ) -> list:
        nlp = self.set_model(model_lang, model_core, model_size)
        doc = nlp(content)

        sensitive_data = []

        for ent in doc.ents:
            if ent.label_ in ['PER', 'LOC', 'ORG', 'MISC']:
                sensitive_data.append((ent.text, ent.label_))

        return sensitive_data
