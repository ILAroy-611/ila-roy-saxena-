'''
Created on 17-Apr-2020

@author: ila roy
'''
dict1={'CHAM':[],'WOR':[],'T20':[]}
    chamlist=[]
    wor_list=[]
    twenty_list=[]
    for value in match_list:
        country,championship,played,won=value.split(':')
        if championship=="CHAM":
            chamlist.append(country+":"+won)
        elif championship=="WOR":
            wor_list.append(country+":"+won)
        elif championship=="T20":
            twenty_list.append(country+":"+won)
    #Finding the maximum times championship was won
    maxcham=0
    for val in chamlist:
        country,won=val.split(":")
        won=int(won)
        if won>=maxcham:
            maxcham=won
    #Finding the countries that won maximum times
    print(chamlist)
    temp_cham_list=[]
    for val in chamlist:
        country,won=val.split(':')
        won=int(won)
        if won==maxcham:
            temp_cham_list.append(country)
    dict1.update({'CHAM':temp_cham_list})