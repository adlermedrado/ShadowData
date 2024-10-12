import spacy
import subprocess
import logging

from spacy import Language

from shadow_data.pii.enums import ModelLang, ModelCoreNews, ModelSize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelSelector:
    @staticmethod
    def select(lang: ModelLang, core: ModelCoreNews, size: ModelSize) -> Language:
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
        if not isinstance(core, ModelCoreNews):
            raise TypeError(f'Expected core to be an instance of ModelCoreNews, got {type(core).__name__}')
        if not isinstance(size, ModelSize):
            raise TypeError(f'Expected size to be an instance of ModelSize, got {type(size).__name__}')

        model_name = f'{lang.value}_{core.value}_{size.value}'
        try:
            nlp = spacy.load(model_name)
        except OSError:
            logger.info(f'Model {model_name} not found. Attempting to install the model...')
            try:
                subprocess.run(['python', '-m', 'spacy', 'download', model_name], check=True)
                nlp = spacy.load(model_name)
            except subprocess.CalledProcessError as e:
                logger.error(f'Failed to download model {model_name}: {e}')
                raise RuntimeError(f'Could not download and load model {model_name}')

        return nlp
