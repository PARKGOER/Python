class MyError(Exception) :
    pass

def say_nick(nick) :
    if nick == "천사" :
        print(nick)
    elif nick == "바보" :
        raise MyError ()
    else :
        pass

try :
    say_nick("천사")
    say_nick("바보")
    
except MyError :
    print("허용되지 않는 별명입니다")
