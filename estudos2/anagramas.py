def is_anagram(text1, text2):
    if not text1 or not text2:
        return False
    text1 = text1.strip().lower()
    text2 = text2.strip().lower()
    return sorted(text1) == sorted(text2)


print(is_anagram("roma", "amor"))
