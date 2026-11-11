print("Count the number of vowels and consonants in a string")
def vowel_consonant(a):
    vowel = "aeiouAEIOU"
    vowel_c = consonant = 0
    for ch in a:
        if ch in vowel:
            vowel_c+=1
        else:
            consonant+=1
    return (f"Number of vowel is : {vowel_c}\nNumber of consnant is : {consonant}")
print(vowel_consonant("koshiki"))        