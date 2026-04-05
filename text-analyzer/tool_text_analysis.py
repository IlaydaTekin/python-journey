#Python Text Analysis Tool 
#Word Frequency, Length & Grouping

text=input("Enter a text: ")

#To clean the words
text=text.lower()
text=text.replace("."," ")
text=text.replace(","," ")
text=text.replace("?"," ")
text=text.replace("!"," ")

#To make text into list
words=text.split()

#To clean the words from the stop_words
stop_words = ["the", "and", "of", "a", "an"]
clean_words=[]

for w in words:
    if w not in stop_words:
        clean_words.append(w)

#To find frequency of the words
freq_dict={}

for word in clean_words:
    freq_dict[word]=freq_dict.get(word,0)+1

#To find the length of words in dictionary
length_dict={}

for word in freq_dict:
    length_dict[word]=len(word)

#To put words that length is 5 or more into a new dictionary
long_words={}

for word,length in length_dict.items():
    if length>=5:
        long_words[word]=length

#To find the most used word

most_freq=0
most_name=None

for name,frequency in freq_dict.items():
    if frequency>most_freq:
        most_freq=frequency
        most_name=name

#To find smallest word
smallest_len=float("inf")
smallest_name=None

for name,length in length_dict.items():
    if length<smallest_len:
        smallest_len=length
        smallest_name=name

#To group words based on their initials
grouped={}

for word in clean_words:
    first_letter=word[0]

    if first_letter not in grouped:
        grouped[first_letter]=[]

    if word not in grouped[first_letter]:
        grouped[first_letter].append(word)


print("Words:", words)
print("Clean words:", clean_words)
print("Frequency of words:", freq_dict)
print("Lenght of words:", length_dict)
print("Words that have 5 or more letters:", long_words)
print("The most used word:",most_name,most_freq)
print("Smallest word:", smallest_name,smallest_len)
print("Grouped words based on the initials:",grouped)