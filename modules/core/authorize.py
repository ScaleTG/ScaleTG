from modules.core.auth import Auth

a = Auth()
try:
    uid = int(input('Enter a user id to authorize them:\n'))
    a.addAuthorized(uid)
except KeyboardInterrupt:
    quit()