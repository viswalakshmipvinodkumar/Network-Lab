import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(ciphertext, key):
    iv = ciphertext[:16]  # Extract the IV from the beginning
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return pt

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    encrypted_msg = client_socket.recv(1024)
    print(f"Encrypted message from server: {encrypted_msg}")

    key = b'my-key-123456789'  # AES key must be either 16, 24, or 32 bytes

    decrypted_msg = decrypt(encrypted_msg, key)
    print(f"Decrypted message: {decrypted_msg.decode()}")

    client_socket.close()

if __name__ == '__main__':
    main()