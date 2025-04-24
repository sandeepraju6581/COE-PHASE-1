# str = "Hi hello 7656 this ^%$^ is Nagul"
str=input("Enter a string: ")
alphabet_count = 0
vowel_count = 0
special_char_count = 0
space_count = 0

vowels = "aeiouAEIOU"

for char in str:
    if char.isalpha():
        alphabet_count += 1
        if char in vowels:
            vowel_count += 1
    elif char.isspace():
        space_count += 1
    elif not char.isdigit():
        special_char_count += 1

print("Number of alphabets:", alphabet_count)
print("Number of vowels:", vowel_count)
print("Number of special characters:", special_char_count)
print("Number of spaces:", space_count)

#startswith()
#endswith()
