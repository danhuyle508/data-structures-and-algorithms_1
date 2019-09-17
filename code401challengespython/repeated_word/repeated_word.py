from hashtable import HashTable

def repeated_word(phrase):
    start = 0 
    word_table = HashTable()
    words = phrase.split(' ')
    for word in words:
        if not word_table.contains(word):
            word_table.add(word, word_table.hash(word))
        else:
            return word  
    return 'No matching words.'        