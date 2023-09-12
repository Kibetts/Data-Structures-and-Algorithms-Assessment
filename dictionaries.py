def word_frequency(sentence):
    frequencies = {}
    words = []
    current_word = ""
    
    for char in sentence.lower() + " ":
        if char.isalnum():
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""

    for word in words:
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
            
    return frequencies
            