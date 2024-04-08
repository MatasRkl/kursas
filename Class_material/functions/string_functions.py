def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def reverse(text):
    return text[::-1]


def caps_on_words(text):
    return text.upper()
