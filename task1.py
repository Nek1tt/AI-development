import gensim.downloader as api

model = api.load("word2vec-google-news-300") # загрузка модели (шаг 1)

print(model.most_similar('king')) # вывод синонимов для слова king
 
print(model.most_similar(positive=['king', 'woman'], negative=['man'])) # вывод аналогии для king - man + woman
