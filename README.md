# Описание
Простенький скрипт, который получает данные о новых видео (возрастом не более 10 дней) и записывает их в Markdown заметку. Использую его для своего **Obsidian**, чтобы всегда иметь актуальные новости. Скрипт у меня на компьютере запускает каждый час в фоновом режиме, так что я даже не замечаю его наличие.

# Использование
Скрипт можно подстроить под свои любимые youtube каналы. Достаточно прописать id каналов и их название в переменную словаря 'channel_id' и 'name' соответственно. Например, у меня выглядит следующим образом:
```python
if __name__ == "__main__":
    #Получить channel_id можно по сссылке https://seostudio.tools/ru/youtube-channel-id (если есть другие способы - напишите, или можно запарсить этот сайт)
    channel_id = [
        'UCrWWcscvUWaqdQJLQQGO6BA',
        'UCA9t0ucLQLDCELE0wbDSAyw',
        'UCP1JsJgeNs86oqLGnjfGo9Q',
        'UC7f5bVxWsm3jlZIPDzOMcAg',
        'UCZ26MoNJKaGXFQWKuGVzmAg',
        'UC0e3QhIYukixgh5VVpKHH9Q',
        'UCvjgXvBlbQiydffZU7m1_aw',
    ]
    #Название канала, соответствующее channel_id
    name = [
        'PythonToday',
        'ZProger',
        'foo52ru ТехноШаман',
        'Хауди Хо',
        'Чёрный Треугольник',
        'Code Bullet',
        'The Coding Train',
    ]
    write_to_md('Актуальные видео', channel_id, name)
```
