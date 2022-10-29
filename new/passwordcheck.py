from . import views


def oneUpper(s):
    for i in s:
        if i.isupper():
            return True 
            break
    else:
        return False

def oneLower(s):
    for i in s:
        if i.islower():
            return True 
            break
    else:
        return False

def oneSpecial(s):
    for i in s:
        if i in ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',';',':','?','/','.','>','<',',','~','`',"'",'"',"\\"]:
            return True
            break
    else:
        return False

def check(password):
    if not ((len(password) > 8) and ( oneUpper(password)) and (oneLower(password)) and (oneSpecial(password))):
        views.error.append("Password must contain atleast 8 digits. Must contain atleast 1 upper case letter, 1 lower case letter and a speciual character.")
        raise views.IncorrectInfoError()