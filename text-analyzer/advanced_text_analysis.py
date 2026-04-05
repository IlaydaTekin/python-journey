#Advanced Text Analysis Tool in Python
#Word Frequency&Lenght Analysis

text=input("Enter a text: ")

#To clean the text
text=text.lower()
text=text.replace("."," ")
text=text.replace(","," ")
text=text.replace("?"," ")
text=text.replace("!"," ")

#To make the text into list
words=text.split()

#To clean words from the stop_words
stop_words = ["is", "the", "and", "a", "to"]
clean_words=[]

for w in words:
    if w in stop_words:
        continue
    else:
        clean_words.append(w)

#To create a dictionary and frequency
freq_dic={}

for word in clean_words:
    freq_dic[word]=freq_dic.get(word,0)+1

#To create lenght dictionary
length_dic={}

for word in freq_dic:
    length_dic[word]=len(word)

#To find top 3 used words
top_words = sorted(freq_dic.items(), key=lambda x: x[1], reverse=True)

#To find average lenght of words
all_count=length_dic.values()
average=sum(all_count)/len(all_count)

#To find the longest 2 words
longest_words=sorted(length_dic.items(),key=lambda x: x[1], reverse=True)

#To group by the lenght
group_len={}

for word in clean_words:
    lenght=len(word)

    if lenght not in group_len:
        group_len[lenght]=[]

    if word not in group_len[lenght]:
        group_len[lenght].append(word)

print("Words:",words)
print("Clean word:", clean_words)
print("Frequency of words:", freq_dic)
print("Lenght of words:",length_dic)

print("Most used 3 words:")
for word, count in top_words[:3]:
    print(word, "->", count)

print("Average lenght of words:", round(average, 2))

print("Most used 3 words:")
for word, count in top_words[:3]:
    print(word, "->", count)

print("Grouped word based on the lenght:",group_len)