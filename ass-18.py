'''
Created on 15-Apr-2020

@author: ila roy
'''
#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    text_list=text.split(" ")
    unknown_words_list=[]
    for i in text_list:
        if i not in vocabulary:
            unknown_words_list.append(i)
    if len(unknown_words_list)==0:
        return -1 
    else:
        return set(unknown_words_list)

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)