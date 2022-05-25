import webbrowser
import csv
from datetime import datetime, timedelta


def string_to_bool(statement):
    if statement == "True":
        return True
    return False


def open_url(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)


def find_url(filename, url):
    with open(filename) as file_obj:

        reader_obj = csv.reader(file_obj)

        for row in reader_obj:
            if row[1].strip() == url:
                return string_to_bool(row[2].strip()), string_to_bool(row[3].strip())

    return False
