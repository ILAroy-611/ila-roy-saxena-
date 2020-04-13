'''
Created on 13-Apr-2020

@author: ila roy
'''
#DSA-Assgn-12
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
                                        
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

class Ball:        
    def __init__(self,color,name):
        self.__color=color
        self.__name=name
        
    def __str__(self):
        return (self.__color+" "+self.__name)
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
             
#Implement Game class here
class Game:
    def __init__(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=Stack(2)
        self.green_balls_container=Stack(2)
        self.yellow_balls_container=Stack(2)
        self.blue_balls_container=Stack(2)
    
    def grouping_based_on_color(self):
        for i in range(0,self.ball_container.get_max_size()):
            temp=self.ball_container.pop()
            if temp.get_color()=="Red":
                self.red_balls_container.push(temp)
            elif temp.get_color()=="Blue":
                self.blue_balls_container.push(temp)
            elif temp.get_color()=="Green":
                self.green_balls_container.push(temp)
            elif temp.get_color()=="Yellow":
                self.yellow_balls_container.push(temp)
    
    def display_ball_details(self,color):
        if color=="Red":
            self.red_balls_container.display()
        if color=="Blue":
            self.blue_balls_container.display()
        if color=="Green":
            self.green_balls_container.display()
        if color=="Yellow":
            self.yellow_balls_container.display()
    
    def rearrange_balls(self,color):
        if color=="Red":
            for i in range(0,self.red_balls_container.get_max_size()):
                data=self.red_balls_container.pop()
                if data.get_name()== "A":
                    a=data 
                else:
                    b=data 
            self.red_balls_container.push(b)
            self.red_balls_container.push(a)
        elif color=="Blue":
            for i in range(0,self.red_balls_container.get_max_size()):
                data=self.blue_balls_container.pop()
                if data.get_name()== "A":
                    a=data 
                else:
                    b=data 
            self.blue_balls_container.push(b)
            self.blue_balls_container.push(a)
        elif color=="Green":
            for i in range(0,self.red_balls_container.get_max_size()):
                data=self.green_balls_container.pop()
                if data.get_name()== "A":
                    a=data 
                else:
                    b=data 
            self.green_balls_container.push(b)
            self.green_balls_container.push(a)
        elif color=="Yellow":
            for i in range(0,self.red_balls_container.get_max_size()):
                data=self.yellow_balls_container.pop()
                if data.get_name()== "A":
                    a=data 
                else:
                    b=data
            self.yellow_balls_container.push(b)
            self.yellow_balls_container.push(a)
            
    
#Use different values to test your program
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)  
ball_list.push(ball2) 
ball_list.push(ball3) 
ball_list.push(ball4) 
ball_list.push(ball5) 
ball_list.push(ball6) 
ball_list.push(ball7) 
ball_list.push(ball8)   

#Create objects of Game class, invoke the methods and test the program
g=Game(ball_list)  
g.grouping_based_on_color()
g.display_ball_details("Yellow")
g.rearrange_balls("Yellow")
g.display_ball_details("Yellow")
