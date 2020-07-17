class SafeFourCal :
    def __init__(self,a,b) :
        self.a=a
        self.b=b
    def add(self) :
        result=self.a+self.b
        return result
    def sub(self) :
        result=self.a-self.b
        return result    
    def mul(self) :
        result=self.a*self.b
        return result    
    def div(self) :
        if self.b==0 :
            return
        else :
            result=self.a/self.b
            return result

    
