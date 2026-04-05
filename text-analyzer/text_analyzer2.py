#Python Text Analyzer-Word Frequency&Lenght Statistics
#Mini Project

text=input("Enter a text: ")
text=text.lower()
text=text.replace(","," ")
text=text.replace("."," ")

words=text.split()
words = [w for w in words if w != ""]

lenght_word={}

for w in words:
    lenght_word[w]=len(w)

max_word=0
long_name=None

for name,lenght in lenght_word.items():
    if lenght>max_word:
        max_word=lenght
        long_name=name

min_word=float("inf")
short_name=None

for name,lenght in lenght_word.items():
    if lenght<min_word:
        min_word=lenght
        short_name=name

long_word={}

for name,lenght in lenght_word.items():
    if lenght > 4:
        long_word[name]=lenght

freq_dict={}
for word in words:
    freq_dict[word]=freq_dict.get(word,0)+1


print("Words:", words)
print("Lenght of word:", lenght_word)
print("Longest word:", long_name,max_word)
print("Shortest word", short_name,min_word)
print("Words longer than 4:", long_word)
print("Frequency of words:",freq_dict)