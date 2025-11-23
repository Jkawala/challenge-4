import string
from base64 import b64decode

# Load the intercepted file
with open("/mnt/data/intercepted.txt", "r") as f:
    s = f.read().strip()


def inv_step1(t):
    a = "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
    b = "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON"
    return t.translate(str.maketrans(a, b))

# (base64 decode)
def inv_step2(t):
    try:
        return b64decode(t).decode("utf-8", "ignore")
    except:
        return ""
    
def inv_step3(t, shift=4):
    lower = string.ascii_lowercase
    shifted = lower[shift:] + lower[:shift]
    return t.translate(str.maketrans(shifted, lower))

# Main decoding loop
def decode(cipher):
    s = cipher
    while s and s[0] in "123":
        step = int(s[0])
        s = s[1:]

        if step == 1:
            s = inv_step1(s)
        elif step == 2:
            s = inv_step2(s)
        elif step == 3:
            s = inv_step3(s)

    return s

# Decode and print the result
decoded_message = decode(s)
print(decoded_message)
