

def main():
    path_to_file = "./books/frankenstein.txt"

    file_content = read_file(path_to_file)
    # print(file_content)

    total_words = count_words(file_content)
    # print(total_words)

    char_dict = character_count(file_content)
    # print(char_dict)

    list_of_dicts = dict_to_list_dict(char_dict)
    # print(list_of_dicts)

    sorted_dicts = dict_list_sorter(list_of_dicts)
    dict_printer(path_to_file,total_words, sorted_dicts)



def read_file(path):
    with open(path) as f:

        file_content = f.read()
        return file_content

def count_words(char_strings):
    array_of_strings = char_strings.split()
    length_of_strings = len(array_of_strings)
    return length_of_strings


def character_count(char_string):
    new_dict = {}
    for each in char_string:
        each = each.lower()
        if each in new_dict:
            new_dict[each] += 1
        else :
            new_dict[each] = 1
    return new_dict

def dict_to_list_dict(char_dict):
    dict_list = []

    for key, char in char_dict.items(): 
        if key.isalpha():
            dict_list.append({"name": key, "num": char})
    return dict_list

def sort_on(dict):
    return dict["num"]

def dict_list_sorter(list_dict):
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def dict_printer(file_path,total_words,dicts_list):
    print(f"--- Begin report of {file_path} ---")
    print(f"{total_words} words found in the document")
    print()
    for each in dicts_list:
        print(f"The '{each["name"]}' character was found {each["num"]} times")
    print("--- End report ---")


main()