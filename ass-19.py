'''
Created on 15-Apr-2020

@author: ila roy
'''
#DSA-Assgn-19

def last_instance( num_list,  start,  end,  key):
    #Remove pass and write your logic here
    if key in num_list:
        mid=(start+end)//2
        if key==num_list[mid]:
            for i in range(mid,end+1):
                if key==num_list[i]:
                    count=i  
        elif key>num_list[mid]:
            start=mid+1 
            for i in range(start,end+1):
                if key==num_list[i]:
                    count=i 
        else:
            end=mid-1 
            for i in range(start,end+1):
                if key==num_list[i]:
                    count=i 
    else:
        return -1 
    return count 

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")