import time

from selene import browser
from selenium import webdriver

def test_text_in_downloaded_file_by_click():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": r"C:\Users\parsh\PycharmProjects\ph_6_files\tmp",  # пример пути указан для windows, если нужно для mac или linux, то путь будет другой, а именно /Users/имя пользователя/путь к папке
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()
    time.sleep(4)

with open("tmp/readme2.rst") as file: #сохранения файла
    file_content_str = file.read()
    assert "test_answer" in file_content_str




