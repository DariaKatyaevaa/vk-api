# примеры запуска
from api import *
from api_main import get_info_from_file

app_id, token = get_info_from_file()
api = API(token)

api.get_user_name(1)
api.get_albums(1)

print()

api.get_user_name(53083705)
api.get_friends(53083705)
print()
api.get_albums(53083705)
