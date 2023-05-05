def emojize(message):
    emojis = {
    ":)": "😄",
    ":(": "😞"
    }
    output = ""
    word_list = message.split(" ")
    for word in word_list:
        output += emojis.get(word,word) + " "
    return output
    
converted = emojize(input("> "))
print(converted)