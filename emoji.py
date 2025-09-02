message = input (">>> ")

emoji_mapping = {
":|" : "🗿",
"8" : "👀",
"<3" : "😍"
}

word = message.split(" ")

output =""
for w in word:
    output = output + emoji_mapping.get(w, w) + " "

print(output)