##the path and file that we want to open
__BOOK = "books/frankenstein.txt"  

##open the file
with open(__BOOK) as f: 
    file_contents = f.read()    

##returns the number of words in a book
def Count_Words(book): 
    return len(book.split())

##returns a dictionary of letters and the number of times they show up in book. tuple of ['string'] : count(int)
def List_of_Letters_Counts(book):
    letters_counts = {}
    lower_case_book = book.lower()
    for letter in [*lower_case_book]:
        if letter in letters_counts:
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1  

    return letters_counts

##main program
def main():
    word_count = Count_Words(file_contents) 
    list_of_letter_counts = List_of_Letters_Counts(file_contents)
    sorted_list_of_letters = []
    
    print(f"--- Begin report of {__BOOK} ---")
    print(f"{word_count} words found in the document")
    
    ##grab all the characters(letters) and put them into a list to sort
    for letter in list_of_letter_counts: 
        sorted_list_of_letters.append(letter)

    ##sort the characters list  
    sorted_list_of_letters.sort()  

    ##iterate through the sorted list
    for letter in sorted_list_of_letters: 
        ##remove non alphabet characters from the printout
        if letter.isalpha(): 
            ##print the results
            print(f"The '{letter}' character was found {list_of_letter_counts[letter]} times") 

    print("--- End report ---")

main()
