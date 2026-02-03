from bot.main import start_bot
import os


if __name__ == '__main__':
    os.system('git reset --hard')
    os.system('git pull origin master')
    start_bot()
