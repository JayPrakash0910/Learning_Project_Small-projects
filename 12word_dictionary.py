from PyDictionary import PyDictionary

dictionary = PyDictionary("EYES","INDENTATION","HEAD")
# print(dictionary.printMeanings())
print(dictionary.getMeanings())  # koi bhi words ka details intro 


# print(dictionary.printAntonyms()) # ulta word 
# print(dictionary.printSynonyms()) # paryavachhi sabd
















"""
from PyDictionary import PyDictionary

dictionary = PyDictionary()
while True:
    word = input("enter your words : ")
    if word =="":
     break
    print(dictionary.meaning(word))
"""

# def main():
#     word_dictionary = {
#         'hi':' a way of greeting',
#         'eyes':'an organ for seeing',
#         'earth':'a planet in space',
#     }
    
#     while True:
#         word=input("ENTER A WORD : ")
#         if word =="":
#             break
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])
# main()        