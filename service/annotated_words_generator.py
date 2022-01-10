import constant


def get_entities_data(entities, start):
    for entitiy in entities:
        if ('start' in entitiy['textSpan']['span'] and 'end' in entitiy['textSpan']['span'] and entitiy['textSpan']['span']['start'] == start) or \
                not 'start' in entitiy['textSpan']['span'] and 'end' in entitiy['textSpan']['span'] and entitiy['textSpan']['span']['end'] > start:

            type = "Default"
            if 'type' in entitiy:
                type = entitiy['type']

            wiki_data_ids = []
            if 'entitySenses' in entitiy:
                for entity_sense in entitiy['entitySenses']:
                    if 'kgEntityId' in entity_sense:
                        wiki_data_ids.append(entity_sense['kgEntityId'])

            return entitiy['textSpan']['span']['end'], type, wiki_data_ids
    return None, None, []

def generate_annotated_words(sentence):
    text = sentence['text']
    words = []
    word = ""

    i = 0
    while i != len(text):
        if i == (len(text) - 1):
            word = word + text[i]
            if len(word) > 0:
                words.append(word)
            break

        if 'entities' in sentence:
            end_index, type, wiki_data_ids = get_entities_data(sentence['entities'], i)
        else:
            end_index = None
            type = None
            wiki_data_ids = []

        if end_index is None:
            word = word + text[i]
            i = i + 1
        else:
            if len(word) >= 0:
                words.append(word)

            next_index = (end_index + 1)
            new_word = text[i:next_index]
            color = constant.DEFAULT_TAG_COLOR
            if type in constant.TAGS:
                color = constant.TAGS[type]
            words.append([(new_word, type, color), wiki_data_ids])

            if next_index >= len(text) -1:
                break

            if i != (len(text) - 1):
                i = next_index
            word = ""
    return words
