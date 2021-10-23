import requests


def show(url: str):
    """
    Function shows scraped webpage in terminal.

    :param url: (str)
    """
    try:
        data = requests.get(url, timeout=5)
    except Exception as e:
        print('Błąd połączenia')
        print(e)
    else:
        text = data.text
        print(text)
