import spacy

nlp = spacy.load("uk_core_news_md")

def get_entities(text):
    if not text or not text.strip():
        return [(f"""Ви не ввели текст для аналізу! 
Поверніться до поля вводу та додайте текст, після натисніть кнопку 'Розпізнати' і отримайте свій результат😊""", None)]

    doc = nlp(text)
    entities = []
    last_idx = 0

    for ent in doc.ents:
        if ent.start_char > last_idx:
            entities.append((text[last_idx:ent.start_char], None))
        
        entities.append((ent.text, ent.label_))
        last_idx = ent.end_char

    if last_idx < len(text):
        entities.append((text[last_idx:], None))

    return entities


def get_entity_list(text):
   
    if not text or not text.strip():
        return []

    doc = nlp(text)
    return [{"Слово": ent.text, "Тип": ent.label_} for ent in doc.ents]