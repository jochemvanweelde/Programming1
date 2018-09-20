def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return any(char.isdigit() for char in newpassword)
    else:
        return False
print(new_password('oude', 'Hetbestewachtwoordooit'))
#False
print(new_password('oude', 'Hetbestewachtwoordooit69'))
#True
