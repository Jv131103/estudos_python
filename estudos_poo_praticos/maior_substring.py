def maior_substring(s):

    chars = set()

    left = 0
    maior = 0

    for right in range(len(s)):

        while s[right] in chars:
            chars.remove(s[left])
            left += 1

        chars.add(s[right])

        maior = max(maior, right - left + 1)

    return maior


print(maior_substring("abcabcbb"))
