# Caesar Cipher Encryption and Decryption
def caesar_cipher(text, key, mode='encrypt'):
    result = []
    for char in text:
        if char.isalpha():
            shift = key if mode == 'encrypt' else -key
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


# Vigenère Cipher Encryption and Decryption
def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'decrypt':
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


def main():
    print("Cipher Encryption and Decryption")

    # Get user inputs
    cipher_type = input("Choose a Cipher (caesar/vigenere): ").strip().lower()
    text = input("Enter your message: ").strip()
    key = input("Enter the key: ").strip()

    # Encrypt or Decrypt
    action = input("Do you want to Encrypt or Decrypt? (e/d): ").strip().lower()

    if cipher_type == 'caesar':
        key = int(key)  # Caesar Cipher key is an integer
        if action == 'e':
            result = caesar_cipher(text, key, mode='encrypt')
        elif action == 'd':
            result = caesar_cipher(text, key, mode='decrypt')
        else:
            print("Invalid action!")
            return
    elif cipher_type == 'vigenere':
        if action == 'e':
            result = vigenere_cipher(text, key, mode='encrypt')
        elif action == 'd':
            result = vigenere_cipher(text, key, mode='decrypt')
        else:
            print("Invalid action!")
            return
    else:
        print("Invalid cipher type!")
        return

    # Output the result
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
