"""
# Name : Harish kumar
# Date : 06-july-2024
# Program 1 : create a program in python to calculate no of vowels and count of each individual vowels in guvi geeks network private limited?
# """



def count_vowels(s):
    vowels = 'aeiou'
    vowel_counts = {v: 0 for v in vowels}
    total_vowels = 0
   
    for i in s.lower():
        if i in vowels:
            vowel_counts[i] += 1
            total_vowels += 1
    
    return total_vowels, vowel_counts

name = "guvi geeks network private limited"


total_vowels, vowel_counts = count_vowels(name)

print(f"Total number of vowels: {total_vowels}")
print("Count of each individual vowel:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")


"""
Name : Harish kumar
Date : 06-july-2024
Program 2 : create a pyramid of number from 1 to 20 using for loop
"""
n = 1
max_num = 20
level = 1

while n <= max_num:
    for _ in range(level):
        if n <= max_num:
            print(n, end=' ')
            n += 1
    print()  
    level += 1


"""
Name : Harish kumar
Date : 06-july-2024
Program 3 : create a program that takes string and returns a new string with vowels removed
"""

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for i in s:
        if i not in vowels:
            result += i
    return result

name_input = input("Enter a string: ")

name_output = remove_vowels(name_input)

print("String with vowels removed:", name_output)


"""
Name : Harish kumar
Date : 06-july-2024
Program 4 : create a program that takes string and returns a unique character in it
"""
def get_unique_characters(s):
    unique_chars = ""
    for i in s:
        if s.count(i) == 1:
            unique_chars += i
    return unique_chars

input_string = input("Enter a string: ")

unique_string = get_unique_characters(input_string)

print("String with unique characters:", unique_string)


"""
Name : Harish kumar
Date : 06-july-2024
Program 5 : create a program that takes string and returns true if it palindrome,false otherwise
"""
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

input_string = input("Enter a string: ")

result = is_palindrome(input_string)

print("Is the string a palindrome?", result)

"""
Name : Harish kumar
Date : 06-july-2024
Program 6 : create a program that takes string and returns number of words in it
"""

def count_words(s):

    words = s.split()

    return len(words)

input_string = input("Enter a string: ")
num_words = count_words(input_string)
print(f"Number of words in the string: {num_words}")


"""
Name : Harish kumar
Date : 06-july-2024
Program 7 : write a program that takes two strings and returns common sub string between them.
"""

def common_substrings(str1, str2):
    common_subs = set()
    len1, len2 = len(str1), len(str2)

    for i in range(len1):
        for j in range(i + 1, len1 + 1):
            substring = str1[i:j]
            if substring in str2:
                common_subs.add(substring)

    return common_subs

str1 = "abcdef"
str2 = "zabxcdefg"
print(f"The common substrings are: {common_substrings(str1, str2)}")


"""
Name : Harish kumar
Date : 06-july-2024
Program 8 : write a program that takes a string and returns most frequent character in it.
"""

from collections import Counter

def most_frequent_character(s):
    frequency = Counter(s)
    
    most_frequent = max(frequency, key=frequency.get)
    
    return most_frequent


test_string = "examplestring"
print(f"The most frequent character is: '{most_frequent_character(test_string)}'")



"""
Name : Harish kumar
Date : 06-july-2024
Program 9 : write a program that takes a string and returns if it is anagram of another string or false other wise.
"""

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
print(f"'{str1}' and '{str2}' are anagrams: {are_anagrams(str1, str2)}")