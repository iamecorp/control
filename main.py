# Программа для фильтрации массива строк

def filter_strings(input_array):
    result_array = []
    for string in input_array:
        if len(string) <= 3:
            result_array.append(string)
    return result_array

# Примеры использования
input_array1 = ["Hello", "2", "world", ":-)"]
result1 = filter_strings(input_array1)
print(result1)

input_array2 = ["1234", "1567", "-2", "computer science"]
result2 = filter_strings(input_array2)
print(result2)

input_array3 = ["Russia", "Denmark", "Kazan"]
result3 = filter_strings(input_array3)
print(result3)