def f(c,*a) :
    if c=="add" :
        result=0
        for i in a :
            result=result+i
    elif c=="mul" :
        result=1
        for i in a :
            result=result*i
    elif c=="sub" :
        result=0
        for i in a :
            result=result-i
    elif c=="div" :
        result=1
        for i in a :
            result=result/i
            
    return result
