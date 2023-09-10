def check_password(password: str):
    with open('/Users/anshuljagtap/Desktop/30python projects/Starter Projects/Password Checker/password.text','r') as file:
        common_passwords: list[str] = file.read().splitlines()
    
    for i, common_passwords in enumerate(common_passwords, start=1):
        if password == common_passwords or password == '':
            print(f'{password}: ❌ (#{i})')
            return     

    print(f'{password}: ✅(Strong password)')

def main():
    user_password: str = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main()
