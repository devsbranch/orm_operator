from models.jachin_bmk import BmkTable
from models.config import my_session
from datetime import date
from tools import data_utils

today = date.today()


def user_menu():
    """This presents the user with options available for selection.
    :argument None
    :parameter None
    """
    user_options = {
        'C': 'Create new bookmark',
        'Q': 'Quit program'
    }
    return user_options


def user_options():
    print('\nPlease select an option amongst the letters on the left')
    for action, descr in user_menu().items():
        print(f'{action} : {descr}')
    while True:
        user_choice = input('Select an option listed below:  ')
        if user_choice == list(user_menu().keys())[0]:
            bmk_name = input('Enter a name for your bookmark:  ')
            bmk_url = input('Enter bookmark url:  ')
            bmk_desc = input('Enter bookmark description:  ')
            bmk_info = [bmk_name, bmk_url, bmk_desc]
            bookmark = BmkTable(bmk_info[0], bmk_info[1], bmk_info[2], today)
            my_session.add(bookmark)
            my_session.commit()
            my_session.close()
            print('Bookmark Added')
            data_utils.csv_file_read_write(bmk_name, bmk_url, bmk_desc, today)
            break
        elif user_choice == list(user_menu().keys())[1]:
            print('Program stopped.')
            break
        else:
            print('Invalid option selected.')
            continue


user_options()

print("Operation Completed")
