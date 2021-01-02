import telegram
import sys
import os

#token that can be generated talking with @BotFather on telegram
my_token = '1413548062:AAEv6GXm5q6fqlIh29Ch6DmUtsBJsVVBwR8'
# '1413548062:AAEv6GXm5q6fqlIh29Ch6DmUtsBJsVVBwR8'
# '1268945897:AAHqgDQ7Pf7cjOb76V-8jM9WqZK_1NdXTvw'
# Get camera name
camera_name=sys.argv[1]
# Get camera id
camera_id=sys.argv[2]

# Get latest camera picture (motion detected)
all_subdirs = os.listdir("/var/lib/motioneye/Camera" + str(camera_id))
latest_subdir = max(all_subdirs)

all_files = os.listdir("/var/lib/motioneye/Camera" + str(camera_id) + "/" + latest_subdir)
latest_file = "/var/lib/motioneye/Camera" + str(camera_id) + "/" + latest_subdir + "/" + max(all_files)

bot = telegram.Bot(token=my_token)
bot.sendMessage(-328785105, "Beweging gedetecteerd op de " + camera_name)
# bot.sendPhoto(-328785105, photo=open(latest_file, 'rb'))
