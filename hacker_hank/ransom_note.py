from collections import Counter


def check_magazine(magazine: str, note: str) -> None:
    magazine_words = Counter(magazine)
    note_words = Counter(note)

    for word in note_words:
        if word not in magazine_words:
            print("No")
            return
        elif word in magazine_words and note_words.get(word) > magazine_words.get(word):
            print("No")
            return
    print("Yes")
