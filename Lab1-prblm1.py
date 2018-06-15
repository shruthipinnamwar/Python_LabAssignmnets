
def passwd_check(passwd):
   
    SpecialSym=['$','@','#','%','!']
    return_val=True
    if len(passwd) < 6:
        print('the length of password must be at least 6 chars long')
        return_val=False
    if len(passwd) >16:
        print('the length of password must be not be greater than 8')
        return_val=False
    if not any(char.isdigit() for char in passwd):
        print('Password should contain at least one number')
        return_val=False
    if not any(char.isupper() for char in passwd):
        print('Password should contain at least one uppercase letter')
        return_val=False
    if not any(char.islower() for char in passwd):
        print('Password should contain at least one lowercase letter')
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        print('the password should have at least one special character')
        return_val=False
    if return_val:
        print('Ok')
    return return_val
username = input('Enter Username : ')
passwd = input('Enter Password : ')
print(passwd_check(passwd))






