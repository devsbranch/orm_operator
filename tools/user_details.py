# coding: utf-8
__author__ = "Alison Mukoma"
__copyright__  = "DevsBranch"
__date__ = "14/11/2020"
"""
welcome to the python expert series compilation
The joys of live coding.

The code in here was initialized from a live pybootcamp coding session. 
But we feel ambitious to grow it into a fancy bookmarking application 
or better that we can then find useful  for keeping track of online content 
whilst on a path to sharpen our python expertize. 
Welcome aboard ship Nebuchadnezzar in the city of zion (^__^)
"""

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
