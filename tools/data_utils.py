import csv
import os.path


def csv_file_read_write(title, url, description, date):
    """
    The os.path is used to check if the file exists. If not the file will be created because file is open in 'a' mode.
    Then the writer.writehead() function will write the headers(title, url, description, date) first followed by the
    actual values of a bookmark to a csv file. Otherwise the function will just write/append the bookmark values
    to the file since the headers exist.
    """
    check_file_exist = os.path.isfile('fixture_data.csv')

    with open('fixture_data.csv', 'a', newline='') as csv_file:
        headers = ['Title', 'URL', 'Description', 'Date']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=headers)

        if not check_file_exist:
            writer.writeheader()

        writer.writerow({'Title': title,
                         'Url': url,
                         'Description': description,
                         'Date': date})
        print('Bookmark added to csv')
