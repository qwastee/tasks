def count_occurrences(string, char):
    return string.count(char)
input_string = "The weather is pleasant today"
character_to_count = 't'
result = count_occurrences(input_string, character_to_count)

print(f"Символ '{character_to_count}' встречается в строке '{input_string}' {result} раз(а).")