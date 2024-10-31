def main():
    book_path = 'books/frankenstein.txt'
    
    with open(book_path) as f:
        file_contents = f.read()
        f.close()

    file_content_cleaned = clean_text(file_contents)
    word_count = count_words(file_content_cleaned)
    # print(len(word_count))
    
    char_dict = character_count(file_contents)
    
    summary(book_path, word_count, char_dict)

def count_words(text):
    # print("count_words called")
    # print(f"Length of Text: {len(text)}")
    text_list = text.split()
    text_count = len(text_list)
    return text_count

def clean_text(text):
    # Remove new line characters
    text = text.replace('\n', ' ')

    # Remove periods, exclamations, question, and double quotations.
    text = text.replace('.', '').replace('"', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '')

    # Set all text to lowercase
    text = text.lower()

    # Remove double spaces
    x = text.find('  ')

    counter = 0
    while x != -1:
        text = text.replace('  ', ' ')
        x = text.find('  ')
        counter += 1
        # print(f"Clean Counter: {counter}")
    return text

def character_count(text):

    # Lowercase text
    text = text.lower()

    # Create an empty dictionary
    character_dict = {}

    # Create a list of all the characters in the text broken out.
    text_list = list(text)

    # Iterate over the split text
    for i in text_list:
        # Check if the character is in the dictionary
        if i in character_dict:
            char_count = character_dict[i]
            character_dict[i] = char_count + 1
        else:
            character_dict[i] = 1

    return character_dict

def sort_dictionary(dict):
    sorted_dict = {}

    while len(dict) > 0:
        value = 0
        character = None
        for i in dict:
            current_value = dict[i]
            
            if current_value > value:
                character = i
                value = current_value
        
        sorted_dict[character] = value
        del dict[character]
                

    return sorted_dict

def summary(book_path, word_count, dict):
    summary = f"--- Begin report of {book_path} ---\n"
    summary += f"{word_count} words found in the document\n\n"

    char_dict = sort_dictionary(dict)

    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    for i in char_dict:
        
        if i in alphabet:

            value = char_dict[i]

            if value > 1:
                summary += f"The '{i}' character was found {value} times\n"
            else:
                summary += f"The '{i}' character was found {value} time\n"

    summary += '--- End report ---'
    print(summary)

if __name__ == "__main__":
        main()

