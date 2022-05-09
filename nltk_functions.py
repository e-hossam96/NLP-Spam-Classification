def text_to_tokens(message, tokenizer, lemmatizer, stop_words):
    message_tokenized = tokenizer.tokenize(message)
    message_lower = [string.lower() for string in message_tokenized]
    message_lemmatized = [lemmatizer.lemmatize(string) for string in message_lower]
    message_important = [string for string in message_lemmatized if string not in stop_words]
    return message_important

def text_to_count_vector(message, features, tokenizer, lemmatizer, stop_words, np):
    base_dict = {word:0 for word in features}
    tokens = text_to_tokens(message, tokenizer, lemmatizer, stop_words)
    for token in tokens:
        if token in features:
            base_dict[token] += 1
    count_vector = np.array(list(base_dict.values()))
    return count_vector