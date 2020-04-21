'''
Created on 21-Apr-2020

@author: ila roy
'''
#DSA-Assgn-26

def count_strings(number):
    #Remove pass and write your logic here
    list1=[]
    k = 1
    str_0 = ["0","1"]
    list2 = []
    str1=""
    if number == 1 :
        count =2 
        return count 
    while k <2 :
        for i in str_0:
            for j in str_0:
                str1+=i +j
                list1.append(str1)
                str1=""
        k+=1 
    list1.remove("11")
    if number >2 :
        while (k <number ):
            for i in list1:
                for j in str_0 :
                    str1+=i+j 
                    list2.append(str1)
                    str1=""
            k+=1 
            for i in list2:
                if "11" in i:
                    index=list2.index(i)
                    list2.pop(index)
            list1=list2 
            list2=[]
    count=len(list1)
    return count
        

#Pass different values to the function and test your program
number=1
print("The number of strings that can be made are:",count_strings(number))