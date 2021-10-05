from chardet import detect

def get_encoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        encoding = detect(data)['encoding']
        print(encoding)


get_encoding('C://Users//craig//Downloads//tunn3l_v1s10n')