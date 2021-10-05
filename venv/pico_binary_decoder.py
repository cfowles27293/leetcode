from chardet import detect

def get_encoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        encoding = detect(data)['encoding']
        d_data = data.decode(encoding)
        print(reverse(d_data))

def reverse(enc_flag):
    flag = ''
    for b in enc_flag:
        int_b = (ord(b))
        int_j = int_b % 256
        int_a = int_b - int_j
        int_i = round(int_a/256)
        flag += chr(int_i)
        flag += chr(int_j)
    return flag


get_encoding('C://Users//craig//Downloads//enc')