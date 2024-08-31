from __future__ import annotations

import secrets


def parse_wordlist(filename: str) -> dict[str, str]:
    """Returns word number to word mapping from file
    having name filename."""

    word_dict = {}
    last_key = int(get_last_key(filename))
    first_key = int("1" * len(str(last_key)))
    with open(filename) as f:
        lines = f.readlines()
    for count, key in enumerate(range(first_key, last_key + 1)):
        word_dict[str(key)] = lines[count].strip()
    return word_dict


def get_last_key(filename: str) -> str:
    """Returns the last key to be in the words dictionary.
    For example, if wordlist file contains 1500 words
    (with each word on its own line) words, this function
    would return 999. Tightly coupled with parse_wordlist
    function."""

    with open(filename) as f:
        lines = f.readlines()
    lcount = len(lines)
    # length of key
    lkey = len(str(lcount)[:-1])
    return "9" * lkey


def get_keys(word_dict: dict, word_count: int) -> tuple[str]:
    """Get keys of words from dictionry."""

    keys = []
    avail_keys = list(word_dict)
    for _ in range(word_count):
        key = secrets.choice(avail_keys)
        keys.append(key)
    return keys


def _get_pass_words(word_dict: dict, join_char: str, word_count: int) -> tuple[str]:
    """Get random words which would constitute password."""

    pass_words = []
    keys = get_keys(word_dict, word_count)
    words = [word_dict[key] for key in keys]
    for word in words:
        if len(pass_words) == word_count:
            return pass_words
        if "-" in word:
            pass_words.extend(word.split("-"))
        elif join_char in word:
            pass_words.extend(word.split("-"))
        else:
            pass_words.append(word)
    return pass_words


def gen_password(filename: str, join_char: str, word_count: int) -> str:
    """Wrapper function for putting all things together."""

    word_dict = parse_wordlist(filename)
    words: tuple[str] = _get_pass_words(word_dict, join_char, word_count)
    passwd = join_char.join(words)
    return passwd
