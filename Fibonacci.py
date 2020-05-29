class Fibonacci():
    def __init__(self, nth):
        self.nth = nth

    def run(self):

        a = 0
        b = 1
        
        if self.nth == 1: 
            return a 
        elif self.nth == 2: 
            return b 
        else: 
            for i in range(2,self.nth): 
                c = a + b 
                a = b 
                b = c 
            return b