from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}

for letter in sentence.lower():
    if letter in char_frequency:
        char_frequency[letter] += 1
    elif letter == " ":
        pass
    else:
        char_frequency[letter] = 1
        
print(char_frequency)
pprint(char_frequency, width=1)

char_frequency_sorted = sorted(char_frequency.items(), 
                               key=lambda kv:kv[1], 
                               reverse=True)
print(char_frequency_sorted[0])