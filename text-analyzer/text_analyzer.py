#Python Text Analyzer-Word Frequency Counter
#Mini project

text=input("Enter a text: ")
text=text.lower()
text=text.replace(","," ")
text=text.replace("."," ")

words=text.split()
words = [w for w in words if w != ""]

freq={}
unique_words=set(words)

for w in words:
    freq[w]=freq.get(w,0)+1

most_count=0
most_name=None

for name,count in freq.items():
    if count>most_count:
        most_count=count
        most_name=name

least_count=float("inf")
least_name=None

for name,count in freq.items():
    if count<least_count:
        least_count=count
        least_name=name

print("Total words:", len(words))
print("Unique words:", len(unique_words))
print("Most frequent:", most_name, most_count)
print("Least frequent:", least_name, least_count)