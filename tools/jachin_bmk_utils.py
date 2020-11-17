from models.jachin_bmk import BmkTable
from models.config import my_session
from datetime import date

today = date.today()

google = BmkTable('Google', 'www.google.com', 'Search engine', today)
youtube = BmkTable('Youtube', 'www.youtube.com', 'Online video sharing site', today)
wikipedia = BmkTable('Wikipedia', 'www.wikipedia.com', 'Online open source encyclopedia', today)
bing = BmkTable('Bing', 'www.bing.com', 'Microsoft search engine', today)

bookmark_names = [google, youtube, wikipedia, bing]


def add_bookmark():
    """
    This function will add the bookmarks to the database by iterating
    over each bookmark in the list which are instances of the BmkTable containing the 'bookmark name',
    'bookmark url', 'bookmark description' and 'Date'. The data with be added to the database using the
    my_session.add() method then the my_session.commit() will save the changes to the database.
    """
    for bookmark in bookmark_names:
        my_session.add(bookmark)
        my_session.commit()
    my_session.close()


add_bookmark()
print("Operation Completed")
