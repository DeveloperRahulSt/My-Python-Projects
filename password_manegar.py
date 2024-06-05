from cryptography.fernet import Fernet

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Encryption key not found! Please generate a key using the generate_key.py script.")
        exit()

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                try:
                    print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())
                except Exception as e:
                    print(f"An error occurred while decrypting the password for {user}: {e}")
    except FileNotFoundError:
        print("Password file not found! Please add a password first.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Do you want to add or view passwords? Type 'add' to add a password, 'view' to view passwords, or 'q' to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode! Please enter 'add', 'view', or 'q'.")
