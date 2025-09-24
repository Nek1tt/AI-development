# Word2Vec Utils

---

Набор файлов для работы с предобученной моделью Word2Vec через `gensim`:
- `word2vec_utils.py` — две функции: `most_similar`, `analogy`.
- `main.py` — CLI для удобного запуска.
- `requirements.txt` — зависимости.

## Обзор возможностей
- Найти похожие слова (`most_similar`).
- Решать аналогии вида `king - man + woman` (`analogy`).

---

---

## Установка (рекомендовано: виртуальное окружение)

### Linux / macOS
```bash
# создать venv и активировать
python3 -m venv .venv
source .venv/bin/activate

# обновить pip и установить зависимости
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### Windows

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

---

## Примеры использования

```bash
# самый простой: похожие слова
python main.py similar --word king --topn 5
```

```bash
# пример аналогии
python main.py --positive king woman --negative man --topn 5
```




