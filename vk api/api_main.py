from api import *
import argparse


def get_info_from_file(file='info'):
    with open(file, 'r') as f:
        app_id = f.readline()
        access_token = f.readline()
    return app_id, access_token


def main(arg):
    app_id, token = get_info_from_file()
    api = API(token)
    if arg.friends:
        api.get_friends(arg.friends)
    if arg.albums:
        api.get_albums(arg.albums)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program "
                                                 "send request to vk api "
                                                 "Arguments: method with arguments")
    parser.add_argument("-friends", type=str, help="input user id")
    parser.add_argument("-albums", type=str, help="input user id")
    args = parser.parse_args()
    main(args)
