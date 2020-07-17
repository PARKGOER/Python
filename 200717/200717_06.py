class MyError(Exception) :
    pass

def say_nick(nick) :
    if nick == "천사" :
        print(nick)
    elif nick == "바보" :
        raise MyError ()
    else :
        pass
