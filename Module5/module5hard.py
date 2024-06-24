from time import sleep


class UrTube():
    def __init__(self):
        self.users = set()
        self.videos = set()
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and hash(user.password) == hash(password):
                self.current_user = user
                return print(f'Пользователь {user.nickname} вошел на сайт')
        return print('Вход не выполнен, проверьте логин или пароль')


    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                return print(f'Пользователь {nickname} уже существует')

        new_user = User(nickname, password, age)
        self.users.add(new_user)
        self.current_user = new_user

    def log_out(self):
        print(f'{self.current_user} покинул страницу')
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.add(i)

    def get_videos(self, key_word):
        checklist = list()
        for some_video in self.videos:
            if self.search_of_key_word(key_word, some_video.title):
                checklist.append(some_video)
        return checklist

    def get_video(self, key_word):
        for some_video in self.videos:
            if self.search_of_key_word(key_word, some_video.title):
                return some_video

    def watch_video(self, key_word):
        if self.current_user == None:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        current_video = self.get_video(key_word)
        if current_video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for timer in range(current_video.duration):
                current_video.time_now = timer
                print(timer + 1, end=" ")
                sleep(1)
            print('Конец видео сынок')
            current_video.time_now = 0

    def search_of_key_word(self, key_word, text):
        key_word_l = key_word.lower()
        text_l = text.lower()
        bingo = False
        for i in range(len(text_l)):
            if key_word_l[0] == text_l[i] and key_word_l == text_l[i:i + len(key_word)]:
                bingo = True
        return bingo


class Video():
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Title: {self.title}, Duration: {self.duration}, Adult_mode: {self.adult_mode}'

    def __repr__(self):
        return f'Video: {self.title}'


class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        print(f'New user! {nickname}')

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.log_out()
ur.log_in('urban_pythonist','iScX4vIJClb9YQavjAgF')
