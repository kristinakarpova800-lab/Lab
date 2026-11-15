import pytest
from text_analyzer import get_entities

def test_empty_input():
    result = get_entities("")
    assert len(result) > 0
    assert "Ви не ввели текст" in result[0][0]

def test_basic_entities():
    text = "Петро поїхав до Києва."
    result = get_entities(text)
    
    assert isinstance(result, list)
    
    text_results = str(result)
    assert "Петро" in text_results or "Київ" in text_results

def test_model_loading_integrity():
    import spacy
    nlp = spacy.load("uk_core_news_md")
    doc = nlp("Тест працездатності моделі.")
    assert doc is not None
    assert len(doc) > 0