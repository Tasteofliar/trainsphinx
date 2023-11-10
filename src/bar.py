import getpass

def get_current_user():
    user = getpass.getuser()
    return user