with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def Count_Words(book): ##returns the number of words in a book
    return len(book.split())

def List_of_Letters_Counts(book):
    letters_counts = {}
    lower_case_book = book.lower()
    for letter in [*lower_case_book]:
        if letter in letters_counts:
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1  

    return letters_counts

def main():
    print(file_contents)
    
    word_count = Count_Words(file_contents) 
    list_of_letter_counts = List_of_Letters_Counts(file_contents)

    print(f"There are {word_count} words in this book.")

    for letter in list_of_letter_counts:
        print(f"{letter}: {list_of_letter_counts[letter]}")

main()
