# n=int(input("number"))
# n2=int(input("number2"))
# print(n/n2)
#
# #unexpected errors, when provide error in input
import nlp as nlp
import spacy
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
# complete_text = ('connect jio')
m=[]
for i in range(2):
    first_para=input("enter the string")
    m.append(first_para)
print(m)
c=[]
d=[]
count=0
for i in m:
    wordsk = i.split(" ")
    for k in wordsk:
        if k not in c:
            c.append(k)
        else:
            d.append(k)
            count+=1

#     wordsk = i.rstrip("\n").split(",")
#     print(wordsk)
#     for j in wordsk:
#         for c in j:
#             if j not in c:
#                 c.append(j)
#             else:
#                 d.append(j)
#                 count += 1
#
#
if count == 0:
    print("no common elements")
print(d)

# complete_doc = nlp(complete_text)
# # Remove stop words and punctuation symbols
# words = [token.text for token in complete_doc
#          if not token.is_stop and not token.is_punct]
# word_freq = Counter(words)
# # 5 commonly occurring words with their frequencies
# common_words = word_freq.most_common(5)
# print (common_words)
# [('Gus', 4), ('London', 3), ('Natural', 3), ('Language', 3), ('Processing', 3)]
# # Unique words
# unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
# print (unique_words)