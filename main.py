def read_book(book: str, **kwargs):
    '''Takes in the books location as a string and returns the text. 
    If you use words= True it will return the words split'''
    words: bool = kwargs.get("words", False)
    
    with open(book, "r") as reader:
        book_read = reader.read()
        if words:
            return book_read.split()
        else:
            return book_read

def word_count():
    '''Returns the books word length'''
    return len(read_book("books/frankenstein.txt",words=True))

def char_count():
    text = read_book("books/frankenstein.txt")
    char_count = {}
    for char in text.lower():
        if char not in char_count and char.isalpha():
            char_count = char_count | {char: 1}
        if char in char_count:
            char_count[char] += 1
    for letter in char_count:        
        print(f"The '{letter}' character was found {char_count[letter]} times")

char_count()





