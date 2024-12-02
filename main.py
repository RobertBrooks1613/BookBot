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

print(word_count())





