def word_counting(content):
    words = []
    words = content.split()
    return len(words)

def characters_counting(content) :
    if isinstance(content, str) == False:
        raise TypeError("expecting string as input")
    effective_content = ""
    effective_content = content.lower()
    character_count = {}
    for i in range(0, len(effective_content)) :
        if (effective_content[i] in character_count) == True:
            character_count[effective_content[i]] += 1
        else:
                character_count[effective_content[i]] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def sorted_character_count(dictionary):
    sorted_count = []
    temp_dict = {}
    for key in dictionary:
        temp_dict = {}
        temp_dict["name"] = key
        temp_dict["num"] = dictionary[key]
        sorted_count.append(temp_dict)
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count