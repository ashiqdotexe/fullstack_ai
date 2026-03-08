# general equation = [expression for item in iterable conditions(if exist)]
# finding squares of number
square_number = [number**2 for number in range(1,11)]
print(square_number)
#finding even numbers
even_number = [number for number in range(1,51) if number%2==0]
print(even_number)
# converting words into upper cases
words = ["apple", "banana", "mango"]
upper_case_conversion = [word.capitalize() for word in words]
print(upper_case_conversion)

words_2 = ["python", "java", "c++", "go"]
finding_length = [f"Length of {word_2} is: {len(word_2)} " for word_2 in words_2]
print(finding_length)

nums = [5, 12, 8, 20, 3, 15]
greater_than_ten = [num for num in nums if num > 10]
print(greater_than_ten)

word = "programming"
removing_vowel = [char for char in word if char not in "aeiou"]
print(removing_vowel)