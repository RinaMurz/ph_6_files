from zipfile import ZipFile


with ZipFile("tmp/hello.zip") as zip_file: # открываем архив
    print(zip_file.namelist()) # печатаем названия файлов в архиве
    text = zip_file.read('hello') # читаем содержимое файла
    print(text)
    zip_file.extract("hello", path="tmp")

    #zip_file.extract('Python Testing with Pytest (Brian Okken).pdf', path="tmp2") # извлекаем файл из архива с указанием директории
    #zip_file.extractall('tmp2') # извлекаем все файлы из архива в директорию tmp2
# если нужно создать архив

#with ZipFile("tmp/hello.zip", 'w') as zip_file: # создаем архив
    #zip_file.write("путь к файлу", arcname='название файла в архиве') # добавляем файл в архив
   # zip_file.close() # закрываем архив