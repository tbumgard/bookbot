__BOOK = "books/frankenstein.txt"  ##the path and file that we want to open

with open(__BOOK) as f: ##open the file
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
    word_count = Count_Words(file_contents) 
    list_of_letter_counts = List_of_Letters_Counts(file_contents)
    sorted_list_of_letters = []
    
    print(f"--- Begin report of {__BOOK} ---")
    print(f"{word_count} words found in the document")
    
    for letter in list_of_letter_counts: ##grab all the characters(letters) and put them into a list to sort
        sorted_list_of_letters.append(letter)

    sorted_list_of_letters.sort()  ##sort the characters list

    for letter in sorted_list_of_letters: ##iterate through the sorted list
        if letter.isalpha(): ##remove non alphabet characters from the printout
            print(f"The '{letter}' character was found {list_of_letter_counts[letter]} times") ##print the results

    print("--- End report ---")
main()
