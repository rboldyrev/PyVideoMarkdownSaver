from youtubesearchpython import *
import markdown
import os

#Метод, который возращает название, ссылку и дату выпуска видео в формате массива в котором есть словарь с трема соотвествующеми ключами 
def get_videos_link(channel_id):
    playlist = Playlist(playlist_from_channel_id(channel_id))
    videos = []
    for v in playlist.videos:
        video = {
            'title': v['title'],
            'link':  v['link'],
            'data':  v['accessibility']['title'].split('views', 1)[1].split('ago', 1)[0] + 'ago',
        }
        videos.append(video)
    return videos

#Фильтруем видео по тем, которые были выпущена не позже 10 дней назад
def filtred_videos(channel_id, name):
    full_text = ''
    videos = get_videos_link(channel_id)
    filtred_video = [video for video in videos if 'day' in video['data'] or 'sec' in video['data'] or 'min' in video['data'] or 'ho' in video['data']]
    for fv in filtred_video:
        full_text = full_text + f'- **{name}** [{fv['title' ]}]({fv['link']}): {fv['data']} \n'
    return full_text


#Сохраняем список актуальные видео в формате Markdown
def write_to_md(naz, channel_id, name):
    textt = ''
    for i in range(len(channel_id)):
        textt = textt + filtred_videos(channel_id[i], name[i])
    print(textt)

    file = open(f"{naz}.md", 'w', encoding="utf-8")
    file.write(textt)
    file.close()

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



