def get_grouped_anagrams(words):
    anagram_dict = dict()
    for word in words:
        sorted_word_as_key = "".join(sorted(list(word)))
        if sorted_word_as_key not in anagram_dict.keys():
            anagram_dict[sorted_word_as_key] = []

    for index, word in enumerate(words):
        sorted_word = "".join(sorted(list(word)))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(index + 1)
            
    return [val for key, val in anagram_dict.items()]



res = get_grouped_anagrams(["cat", "tac", "xyz", "kkm"])


