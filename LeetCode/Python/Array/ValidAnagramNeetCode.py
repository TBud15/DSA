def isAnagram(self, s: str, t: str) -> bool:
    # Если строки разной длины, они не могут быть анаграммами.
    if len(s) != len(t):
        return False
    
    # Инициализируем словари для подсчета символов в каждой строке.
    char_count_s, char_count_t = {}, {}
    
    # Подсчитываем количество каждого символа в обеих строках.
    for i in range(len(s)):
        char_count_s[s[i]] = 1 + char_count_s.get(s[i], 0)
        char_count_t[t[i]] = 1 + char_count_t.get(t[i], 0)
    
    # Сравниваем количество каждого символа в двух строках.
    for char in char_count_s:
        if char_count_s[char] != char_count_t.get(char, 0):
            # Если количество символа в строках различается, это не анаграмма.
            return False
    
    # Если все проверки пройдены, строки являются анаграммами.
    return True
