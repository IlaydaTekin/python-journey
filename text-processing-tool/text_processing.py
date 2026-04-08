#text-processing-tool

#To create a input and list
text=input("Enter a text: ")
words=text.split()

stop_words = ["is", "and", "the", "a", "an", "to"]

#To lower the words in the list
def lower_words(words):
    words=list(map(lambda w: w.lower(),words))
    return words

lowered=lower_words(words)

#To remove punctuation
def remove_punctuation(words):
    words=list(map(lambda w: w.replace(".","").replace(",","").replace("?","").replace("!",""), words))
    return words

remove_punc=remove_punctuation(lowered)

#To remove stop_words
def remove_stop_words(words, stop_words):
    words=list(filter(lambda w: w not in stop_words,words))
    return words

remove_stop=remove_stop_words(remove_punc,stop_words)

#To find long words
def long_word(words):
    words=list(filter(lambda w:len(w)>=4, words))
    return words

long_only=long_word(remove_stop)

#To remove iteration words
def unique_words(words):
    return list(set(words))

unique=unique_words(long_only)

#To put words according to the length
def sort_by_asc(words):
    return sorted(words, key=lambda w: len(w))

sorted_asc=sort_by_asc(unique)

#To put words according to the length desc
def sort_by_desc(words):
    return sorted(words, key=lambda w: len(w),reverse=True)
    
sorted_desc=sort_by_desc(unique)

#To find word frequency
def word_frequency(words):
    freq={}
    for w in words:
        freq[w]=freq.get(w,0)+1
    return freq

frequency=word_frequency(long_word)

print("Original words:", words)
print("Lowered words:",lowered)
print("Remove punctuation:",remove_punc)
print("Removed from stop words:", remove_stop)
print("Longer words:", long_only)
print("Unique words:",unique)
print("Sorted by length based on increase:",sorted_asc)
print("Sorted by length based on decrease:",sorted_desc)
print("Frequency of words", frequency)