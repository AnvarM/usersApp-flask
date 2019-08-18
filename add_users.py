from models import *

db.create_all()

role_adm = Role('admin')
role_usr = Role('user')

db.session.add(role_adm)
db.session.commit()

db.session.add(role_usr)
db.session.commit()

with open('names.txt', 'r') as f:
    for line in f:
        line = line.strip()
        user_name = line
        user_email = line + '@tst.prp'
        passw = 'tttest'
        role = 2

        user = User(user_name, user_email, passw, role)
        db.session.add(user)
        db.session.commit()


