from Crypto.Cipher import AES

key = b"Sixteen byte key"
iv = b"Initialization v"


def load_image(filename):
    """Read the BMP, split off the 54-byte header, and trim the data to 16-byte blocks."""
    with open(filename, "rb") as f:
        plaintext = f.read()

    print("Total file size:", len(plaintext))

    header = plaintext[:54]
    image_data = plaintext[54:]

    print("Image data size:", len(image_data))
    print("Leftover bytes:", len(image_data) % 16)

    remainder = len(image_data) % 16
    if remainder != 0:
        image_data = image_data[:-remainder]

    print("Leftover after trimming:", len(image_data) % 16)
    return header, image_data


def encrypt_ecb(header, image_data):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(image_data)

    with open("test_ecb.bmp", "wb") as f:
        f.write(header + ciphertext)

    print("ECB done: test_ecb.bmp created")


def encrypt_cbc(header, image_data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(image_data)

    with open("test_cbc.bmp", "wb") as f:
        f.write(header + ciphertext)

    print("CBC done: test_cbc.bmp created")


# ---- Run everything ----
header, image_data = load_image("test.bmp")
encrypt_ecb(header, image_data)
encrypt_cbc(header, image_data)