"""
main.py — простой CLI для работы с word2vec-google-news-300

Команды:
  similar  --word WORD [--topn N]
  analogy   --positive WORD [WORD ...] [--negative WORD [WORD ...]] [--topn N]
"""


import argparse
import sys

from word2vec_utils import load_model


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="CLI для word2vec-google-news-300")
    sub = p.add_subparsers(dest="cmd", required=True)

    s_sim = sub.add_parser("similar", help="Находит синонимы для введенного слова")
    s_sim.add_argument("--word", required=True, type=str, help="Слово к которому ищем синоним")
    s_sim.add_argument("--topn", type=int, default=10, help="Количество результатов для возврата")

    s_ana = sub.add_parser("analogy", help="Решает аналогию positive - negative")
    s_ana.add_argument("--positive", nargs="+", required=True, help="Позитивные слова для аналогии")
    s_ana.add_argument("--negative", nargs="*", default=[], help="Негативные слова для аналогии")
    s_ana.add_argument("--topn", type=int, default=10, help="Количество результатов для возврата")

    return p.parse_args(argv)


def print_results(pairs):
    for word, score in pairs:
        print(f"{word}\t{score:.6f}")


def main(argv=None):
    args = parse_args(argv)

    try:
        model = load_model()
    except Exception as e:
        print(f"Error loading model: {e}", file=sys.stderr)
        return 1

    try:
        if args.cmd == "similar":
            word = args.word
            if not isinstance(word, str) or not word.strip():
                raise ValueError("Слово не должно быть пустой строкой")
            if not isinstance(args.topn, int) or args.topn <= 0:
                raise ValueError("--topn должен быть положительным числом")

            results = model.most_similar(word, topn=args.topn)
            print_results(results)

        elif args.cmd == "analogy":
            pos = args.positive
            neg = args.negative or []
            if not pos or not all(isinstance(w, str) and w for w in pos):
                raise ValueError("--positive не должен быть пустым")
            if not all(isinstance(w, str) and w for w in neg):
                raise ValueError("--negative не должен быть пустой строкой")
            if not isinstance(args.topn, int) or args.topn <= 0:
                raise ValueError("--topn должен быть положительным числом")

            results = model.most_similar(positive=pos, negative=neg, topn=args.topn)
            print_results(results)

        else:
            print("Неизвестная команда", file=sys.stderr)
            return 2

    except KeyError as e:
        print(f"Vocabulary error: {e}", file=sys.stderr)
        return 3
    except ValueError as e:
        print(f"Invalid arguments: {e}", file=sys.stderr)
        return 4
    except Exception as e:
        print(f"Computation error: {e}", file=sys.stderr)
        return 5

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

