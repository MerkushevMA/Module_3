def send_email(message, recipient, sender = 'university.help@gmail.com'):
    list_end = ('.com', '.ru', '.net')

    if recipient.find("@") == -1 or sender.find("@") == -1:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    elif not recipient.lower().endswith(list_end) and sender.lower().endswith(list_end):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Привет растение', 'www.muxa@mail.net', 'muxa@gmail.nefjisd')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')