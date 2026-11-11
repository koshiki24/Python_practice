print('''Find the longest substring without repeating characters.
Example: "abcabcbb" → 3 ("abc")''')
print('''Find the longest substring without repeating characters.
Example: "abcabcbb" → 3 ("abc")''')

a = "abcabcbbd"
result = ""
longest = ""

for ch in a:
    if ch not in result:
        result = result + ch
    else:
        if len(result) > len(longest):
            longest = result

        result = result[result.index(ch) + 1:] + ch

if len(result) > len(longest):
    longest = result

print(longest)
print(len(longest))