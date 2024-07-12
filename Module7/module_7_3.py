class WordsFinder:
    def __init__(self, *files):
        self.file_names = list()
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        exception_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i_names in self.file_names:
            with open(i_names, 'r', encoding='utf-8') as file:
                word_temp = file.read().lower()
                for i in exception_symbols:
                    word_temp = word_temp.replace(i, ' ')
                all_words[i_names] = word_temp.split()
        return all_words

    def find(self, word):
        all_words_finder = {}
        for name, words in self.get_all_words().items():
            counter = 1
            for i in words:
                if i == word.lower():
                    all_words_finder[name] = counter
                    break
                else:
                    counter += 1
        return all_words_finder
        #метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.

    def count(self, word):
        all_words_counter = {}
        for name, words in self.get_all_words().items():
            counter = 0
            for i in words:
                if i == word.lower():
                    counter += 1
            if counter > 0:
                all_words_counter[name] = counter
        return all_words_counter


word = ("It's a text for task Найти везде,"
        "Используйте его для самопроверки."
        "Успехов в решении задачи!"
        "text text text")


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))