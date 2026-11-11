print("Count the number of vowels and consonants in a string")
a = "ujjainAB"
vowel = "aeiouAEIOU"
vowel_count = consonant_count = 0
for ch in a:
    if ch in vowel:
        vowel_count+=1
    else:
        consonant_count+=1
print(f"Vowel is : {vowel_count}")
print(f"Consonant is : {consonant_count}")

