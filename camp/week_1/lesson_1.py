def is_email_valid(email):
    result = (email.endswith('@gmail.com')
              or email.endswith('@mail.ru')
              or email.endswith('@outlook.com'))

    return result


def is_password_valid(password):
    result = len(password) > 8 and password[0].istitle()

    return result


accounts = {'username': [],
            'email': [],
            'password': []}

user_name = input('Введите имя пользователя: ')
email = input('Введите адрес электронной почты: ')
password = input('Введите пароль: ')

accounts['username'].append(user_name)

if is_email_valid(email) and is_password_valid(password):
    accounts['password'].append(password)
    accounts['email'].append(email)

print(accounts)
{}.setdefault(2)``~