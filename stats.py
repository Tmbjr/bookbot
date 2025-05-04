def count_words(string):
    return len(string.split())
    #print(f"{num_words} words found in the document")


def count_characters(string):
    char_dict = {}

    for i in range(0, len(string)):

        char = string[i].lower()

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    count_list = []

    for key in dict:
        count_list.append({"char" : key, "num" : dict[key]})

    count_list.sort(reverse=True, key=sort_on)

    return count_list
    
