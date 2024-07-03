import os

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу

CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE  ) # получаем абсолютный путь к текущей директории где находится файл с которым работаем
print(CURRENT_FILE)

TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'tmp') # делаем склейку пути к текущей директории и папки tmp
print(TMP_DIR)