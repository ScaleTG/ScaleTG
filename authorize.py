from modules.auth import Auth

if __name__ == '__main__':
    a = Auth()
    try:
        uid = int(input('Enter a user id to authorize them:\n'))
        a.addAuthorized(uid)
    except KeyboardInterrupt:
        quit()