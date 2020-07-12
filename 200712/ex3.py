class FourCal() :
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
        result=self.a/self.b
        return result
    
class MoreFourCal(FourCal) :
    def pow(self) :
        result=self.a**self.b
        return result

class SafeFourCal(FourCal) :
    def div(self) :
        if self.b==0 :
            pass
        else : 
            result=self.a/self.b
            return result
