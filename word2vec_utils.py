"""
Модуль для работы с моделью word2vec-google-news-300 из библиотеки Gensim.

Функционал:
- Поиск синонимов для заданного слова
- Поиск аналогий вида "king - man + woman"
"""

import gensim.downloader as api


def load_model():
    """
    Загружает модель word2vec-google-news-300.

    Returns:
        model (gensim.models.KeyedVectors): предобученная модель
    Raises:
        RuntimeError: если модель не загружена
    """
    try:
        model = api.load("word2vec-google-news-300")
        return model
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке модели: {e}")


def find_synonyms(word: str, topn: int = 10):
    """
    Находит синонимы для заданного слова.

    Args:
        word (str): слово для поиска
        topn (int): количество синонимов (по умолчанию 10)

    Returns:
        list: список синонимов с коэффициентами близости
    """
    if not isinstance(word, str) or not word.strip():
        raise ValueError("Слово должно быть непустой строкой")

    model = load_model()
    try:
        return model.most_similar(word, topn=topn)
    except KeyError:
        raise ValueError(f"Слово '{word}' отсутствует в словаре модели")
    except Exception as e:
        raise RuntimeError(f"Ошибка при поиске синонимов: {e}")


def find_analogy(positive: list, negative: list, topn: int = 10):
    """
    Находит аналогию (пример: king - man + woman = queen).

    Args:
        positive (list): список положительных слов
        negative (list): список отрицательных слов
        topn (int): количество результатов (по умолчанию 10)

    Returns:
        list: список слов-результатов с коэффициентами близости
    """
    if not isinstance(positive, list) or not isinstance(negative, list):
        raise ValueError("Аргументы positive и negative должны быть списками")

    model = load_model()
    try:
        return model.most_similar(positive=positive, negative=negative, topn=topn)
    except KeyError as e:
        raise ValueError(f"Некоторых слов нет в словаре модели: {e}")
    except Exception as e:
        raise RuntimeError(f"Ошибка при поиске аналогий: {e}")
