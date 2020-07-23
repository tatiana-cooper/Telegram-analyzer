from telethon.sync import TelegramClient

API_ID = 'YOUR-TELEGRAM-API-ID (int)'
API_HASH = 'YOUR-TELEGRAM-API-HASH (str)'


def get_messages(target_user, username, n=None):
    """
    The function gets messages from user's Telegram account and stores it in 'data.txt' using Telegram API.
    :param username: user's username in Telegram
    :param target_user: user with whom you want to check your message history
    :param n: amount of last messages you want to check (default None — all messages)
    :return: None
    """

    with TelegramClient(f'{username}', API_ID, API_HASH) as client:
        with open('data.txt', 'w', encoding='UTF-8') as f:
            for message in client.iter_messages(target_user, limit=n):
                if message.message:
                    if message.get_sender().username:
                        f.write(message.get_sender().username + ':\t' + message.message + ' \n')
                    elif message.get_sender().first_name:
                        f.write(message.get_sender().first_name + ':\t' + message.message + ' \n')
                    else:
                        f.write(target_user + ':\t' + message.message + ' \n')
        print('Please, wait a few more seconds..')
        client.log_out()
