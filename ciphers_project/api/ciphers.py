def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if(ord(c) >= 65 and ord(c) <= 90):
            if((ord(c) + shift) > 90):
                c_encoded = ord(c) + shift - 26
            else:
                c_encoded = ord(c) + shift
            c_encoded = chr(c_encoded)
            cipher_text += c_encoded

        elif(ord(c) >= 97 and ord(c) <= 122):
            if((ord(c) + shift) > 122):
                c_encoded = ord(c) + shift - 26
            else:
                c_encoded = ord(c) + shift
            c_encoded = chr(c_encoded)
            cipher_text += c_encoded
        
    return cipher_text