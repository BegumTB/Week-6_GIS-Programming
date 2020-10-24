def create_a_list(file):
    a_list = open(file)
    list = []
    for line in a_list:
        word = line.strip()
        list += [word]
    return list


wordlist = create_a_list("words.txt")

def make_dic(list):
    word_dic = dict()
    for word in list:
        word_dic[word] = ''
    return word_dic

dictlist = make_dic(wordlist)

def check_for_string(word, dictionary):
    if word in dictionary:
        return True
    return False

check_for_string("word", dictlist)

check_for_string("begum", dictlist)

check_for_string("dgdf", dictlist)
