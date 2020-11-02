#login3

import bcrypt


def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')

def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf8')
    return bcrypt.checkpw(pw.encode('utf8'), expected_hash)


USERS = {'admin': hash_password('admin'),
         'users': hash_password('users')}
GROUPS = {'admin': ['group:admin']}


def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])