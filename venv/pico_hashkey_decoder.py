import hashlib

def get_key(user_bytes):
    key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
    key_part_static2_trial = "}"
    key = []
    sequence = [4,5,3,6,2,7,1,8]
    j = 0
    while j < len(sequence):
        key.append(hashlib.sha256(user_bytes).hexdigest()[sequence[j]])
        j +=1
    print(key_part_static1_trial+''.join(key)+key_part_static2_trial)

user_bytes = b"SCHOFIELD"
get_key(user_bytes)

'''
Answer is picoCTF{1n_7h3_|<3y_of_e584b363}
'''