class BrowserHistory:
    class Node:
        def __init__(self, val): 
            self.val = val
            self.prev = None
            self.next = None
            
    #O(1) time
    def __init__(self, homepage: str):
        self.history = BrowserHistory.Node(homepage)

    #O(1) time
    def visit(self, url: str) -> None:
        node = BrowserHistory.Node(url)
        node.prev = self.history
        self.history.next = node
        self.history = self.history.next
          
    #O(steps) time
    def back(self, steps: int) -> str:
        while self.history.prev and steps:
            self.history = self.history.prev
            steps -= 1
        return self.history.val
        
    #O(steps) time    
    def forward(self, steps: int) -> str:
        while self.history.next and steps:
            self.history = self.history.next
            steps -= 1

class BrowserHistory:
    #O(1) time
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0

    #O(n) time
    def visit(self, url: str) -> None:
        while self.cur + 1 < len(self.history):
            self.history.pop()
        self.history.append(url)
        self.cur += 1
          
    #O(1) time
    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    #O(1) time    
    def forward(self, steps: int) -> str:
        self.cur = min(len(self.history) - 1, self.cur + steps)
        return self.history[self.cur]



class BrowserHistory:
    def __init__(self, homepage: str):
        self.curPage = homepage # We keep track of the page we are currently on
        self.prevStack = [] # We keep track of the pages if we were to go back 
        self.forwardStack = [] # We keep track of the pages if we were to go forward

    def visit(self, url: str) -> None:
        self.prevStack.append(self.curPage) # Step 1
        self.forwardStack = [] # Step 2
        self.curPage = url # Step 3
        

    def back(self, steps: int) -> str:
        possible = min(steps, len(self.prevStack)) # In order to hamdle cases where steps > len(self.prevStack) ,we take the minimum of the two at all times
        
        while possible:  # Step 0
            self.forwardStack.append(self.curPage) # Step 1
            self.curPage = self.prevStack.pop() # Step 2
            possible -= 1 # Step 3 
        
        return self.curPage # We need to return the page we're at currently
    

    def forward(self, steps: int) -> str:
        possible = min(steps, len(self.forwardStack)) # In order to hamdle cases where steps > len(self.forwardStack) ,we take the minimum of the two at all times
        
        while possible:  # Step 0
            self.prevStack.append(self.curPage) # Step 1
            self.curPage = self.forwardStack.pop() # Step 2
            possible -= 1 # Step 3
        
        return self.curPage # We need to return the page we're at currently