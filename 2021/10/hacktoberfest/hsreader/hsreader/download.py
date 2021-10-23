import requests


def download(url: str, filename: str):
    """
    Function stores scraped webpage as HTML

    :param url: (str),
    :param filename: (str)
    """
    try:
        data = requests.get(url, timeout=5)
    except Exception as e:
        print('Błąd połączenia')
        print(e)
    else:
        with open(filename, 'w') as f:
            f.write(data.text)
            print(f'File {filename} stored sucessfully')
