from models import User
from models import my_session


# create some entries
#
# user = User('chris', 'SADJKFHNSJKFNVJKFNV')
#
# my_session.add(user)
# my_session.commit()

# All users
all_users = my_session.query(User).all()
for user in all_users:
    print(f'ID: {user.id} Username: {user.username}, With password: {user.password}')

