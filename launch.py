from get_messages import get_messages
from make_hist import make_hist


def launch():
    """ The function reads the user's inputs and starts program process and launches creating a histogram """
    user = input('Enter your name: ')
    target_username = input('Enter the username or phone number (+380XXXXXXXXXX — for Ukraine) of your target: ')
    number_of_messages = int(input("Maximum number of messages to analyze, to analyze all "
                                   "(may take longer) — enter '0': "))
    words = input('Enter words of your interest for analysis divided by space: ').split()
    if number_of_messages == 0:
        number_of_messages = None

    get_messages(target_username, user, number_of_messages)
    make_hist(words)


if __name__ == '__main__':
    launch()
