def find_most_common_and_longest_words(text):
    words = text.split()
    most_common_word = max(set(words), key=words.count)

    longest_word = max(words, key=len)

    return most_common_word, longest_word

input_text = input("Введите текст: ")

most_common, longest = find_most_common_and_longest_words(input_text)

print(f"Наиболее часто встречающееся слово: {most_common}")
print(f"Самое длинное слово: {longest}")