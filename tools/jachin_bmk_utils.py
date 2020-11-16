from models.jachin_bmk import BmkTable
from models.config import my_session


google = BmkTable('Google', 'www.google.com', 'Search engine')
youtube = BmkTable('Youtube', 'www.youtube.com', 'Online video sharing site')
wikipedia = BmkTable('Wikipedia', 'www.wikipedia.com', 'Online open source encyclopedia')
bing = BmkTable('Bing', 'www.bing.com', 'Microsoft search engine')

bookmark_names = [google, youtube, wikipedia, bing]


def add_bookmark():
    for bookmark in bookmark_names:
        my_session.add(bookmark)
    my_session.commit()
    my_session.close()


add_bookmark()
print("Operation Completed")
