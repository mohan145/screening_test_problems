class Stack():
    
    def __init__(self):
        self.stack=[]
        self.top=-1
    
    def pop(self):
        if self.top==-1:
            return "Stack Empty"
        top_element=self.stack[self.top]
        self.top-=1
        self.stack.pop()
        return top_element
    
    def push(self,element):
        self.top+=1
        self.stack.append(element)

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
      
        stack = Stack()  
        
        def isCloseBrace(char):
            if char==")":
                return True
            return False
        
        def isOperator(element):
            if element=="+" or element=="-" or element=="*" or element=="/":
                return True
            return False
  
        for element in A:  
            if isCloseBrace(element):  
                poped_element = stack.pop()
                redundant = True
                while (poped_element != '('):  
                    if isOperator(poped_element):  
                        redundant = False
      
                    poped_element = stack.pop()
      
                if redundant: 
                    return 1
            else: 
                stack.push(element) 
        return 0
