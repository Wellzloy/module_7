class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, encoding='utf-8') as f:
                content = f.read().lower()
                # Убираем знаки препинания
                punctuation = r'[.,=!?;:-]'
                content = ''.join(c for c in content if c not in punctuation)
                words = content.split()
                all_words[filename] = words
        return all_words

    def find(self, word):
        positions = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            try:
                index = words.index(word)
                positions[filename] = index + 1  # Индекс начинается с 1
            except ValueError:
                pass  # Слово не найдено, просто продолжаем
        return positions

    def count(self, word):
        counts = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            counts[filename] = words.count(word)
        return counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего