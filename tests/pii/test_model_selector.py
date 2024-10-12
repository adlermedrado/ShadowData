import pytest
from unittest.mock import patch, MagicMock
from shadow_data.pii.enums import ModelLang, ModelCoreNews, ModelSize
from shadow_data.pii.model_selector import ModelSelector
import subprocess


def test_select_valid_model():
    with patch('spacy.load') as mock_spacy_load:
        mock_spacy_load.return_value = MagicMock()

        lang = ModelLang.ENGLISH
        core = ModelCoreNews.CORE_NEWS
        size = ModelSize.SMALL

        nlp = ModelSelector.select(lang, core, size)

        mock_spacy_load.assert_called_once_with('en_core_news_sm')
        assert isinstance(nlp, MagicMock)


def test_select_invalid_lang_type():
    core = ModelCoreNews.CORE_NEWS
    size = ModelSize

    with pytest.raises(TypeError):
        ModelSelector.select('en', core, size)


def test_select_invalid_core_type():
    lang = ModelLang.ENGLISH
    size = ModelSize.SMALL

    with pytest.raises(TypeError):
        ModelSelector.select(lang, 'core', size)


def test_select_invalid_size_type():
    lang = ModelLang.ENGLISH
    core = ModelCoreNews.CORE_NEWS

    with pytest.raises(TypeError):
        ModelSelector.select(lang, core, 'big')


def test_select_model_download():
    with patch('spacy.load') as mock_spacy_load, patch('subprocess.run') as mock_subprocess_run:
        mock_spacy_load.side_effect = [OSError, MagicMock()]

        mock_subprocess_run.return_value = MagicMock()

        lang = ModelLang.ENGLISH
        core = ModelCoreNews.CORE_NEWS
        size = ModelSize.SMALL

        nlp = ModelSelector.select(lang, core, size)

        mock_subprocess_run.assert_called_once_with(
            ['python', '-m', 'spacy', 'download', 'en_core_news_sm'], check=True
        )
        assert mock_spacy_load.call_count == 2
        assert isinstance(nlp, MagicMock)


def test_select_model_download_failure():
    with patch('spacy.load', side_effect=OSError) as mock_spacy_load, patch(
        'subprocess.run', side_effect=subprocess.CalledProcessError(1, 'cmd')
    ) as mock_subprocess_run:
        lang = ModelLang.ENGLISH
        core = ModelCoreNews.CORE_NEWS
        size = ModelSize.SMALL

        with pytest.raises(RuntimeError):
            ModelSelector.select(lang, core, size)

        mock_subprocess_run.assert_called_once_with(
            ['python', '-m', 'spacy', 'download', 'en_core_news_sm'], check=True
        )
