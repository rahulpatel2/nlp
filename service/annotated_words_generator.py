import constant


def get_end_index_and_type(entities, start):
    for entitiy in entities:
        if ('start' in entitiy['textSpan']['span'] and 'end' in entitiy['textSpan']['span'] and entitiy['textSpan']['span']['start'] == start) or \
                not 'start' in entitiy['textSpan']['span'] and 'end' in entitiy['textSpan']['span'] and entitiy['textSpan']['span']['end'] > start:
            return entitiy['textSpan']['span']['end'], entitiy['type']
    return None, None

def generate_annotated_words(sentence):
    text = sentence['text']
    words = []
    word = ""

    i = 0
    while i != len(text):
        if i == (len(text) - 1):
            i = i + 1
            if len(word) > 0:
                words.append(word)
            break

        end_index, type = get_end_index_and_type(sentence['entities'], i)
        if end_index is None:
            word = word + text[i]
            i = i + 1
        else:
            if len(word) >= 0:
                words.append(word)

            next_index = (end_index + 1)
            new_word = text[i:next_index]
            words.append((new_word, type, constant.TAGS[type]))

            if i != (len(text) - 1):
                i = next_index
            word = ""
    return words