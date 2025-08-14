def get_num_words(text):
    return len(text.split())

def char_num_times(text):
    char_dict = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1

    return char_dict

def sort_on(items):
    return items["num"]

def sorted_list_of_dict(l):
    unsorted_dict = l
    sorted_list = []

    for key in unsorted_dict:
        dict_of_char = {}
        if key.isalpha():
            dict_of_char["char"] = key
            dict_of_char["num"] = unsorted_dict[key]
            sorted_list.append(dict_of_char)
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
        
