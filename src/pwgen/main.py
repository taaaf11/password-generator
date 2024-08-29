from __future__ import annotations

import secrets
import sys
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from string import ascii_letters, digits, punctuation

PROG_NAME = "pwgen"
PROG_DESC = "A random password generator in your toolset."

BASE = ascii_letters + digits + punctuation


@dataclass(frozen=True)
class _Config:
    letters: bool = True
    digits: bool = True
    punct: bool = True
    length: int = 8

    def __post_init__(self):
        if not (self.letters or self.digits or self.punct):
            print("At least one of the three components (alphabets, numbers or symbols) must be allowed", file=sys.stderr)
            sys.exit(1)


def _gen_pass(config: _Config) -> str:
    while True:
        passwd = ""
        for _ in range(config.length):
            while (char := secrets.choice(BASE)) == "\\":
                continue
            passwd += char

        # contains
        cont_letters = any(c.isalpha() for c in passwd)
        cont_digits = any(c.isdigit() for c in passwd)
        cont_punct = any((c in punctuation) for c in passwd)

        if config.letters and not cont_letters:
            continue
        if config.digits and not cont_digits:
            continue
        if config.punct and not cont_punct:
            continue

        return passwd


def parse_opts() -> Namespace:
    """Parse command line options and return Namespace object."""

    o_parser = ArgumentParser(prog=PROG_NAME, description=PROG_DESC)
    add_opt = o_parser.add_argument

    add_opt("-a",
            "--alphabets",
            action="store_true",
            help="Don't include alphabets in the password. (Default is to include)"
            )
    add_opt("-n",
            "--numbers",
            action="store_true",
            help="Don't include numbers in the password. (Default is to include)"
            )
    add_opt("-p",
            "--punctuation",
            action="store_true",
            help="Don't include symbols in the password. (Default is to include)"
            )
    add_opt("-l",
            "--length",
            type=int,
            help="Length of the password. (Default is 8)"
            )

    return o_parser.parse_args()


def _gen_config(cmd_opts: Namespace) -> _Config:
    """Generate config from arguments."""

    incl_letters = True
    incl_digits = True
    incl_punct = True
    p_len = 8

    incl_letters = cmd_opts.alphabets
    incl_digits = cmd_opts.numbers
    incl_punct = cmd_opts.punctuation
    if cmd_opts.length:
        p_len = options.length

    config = _Config(incl_letters, incl_digits, incl_punct, p_len)
    return config

def gen_passwd():
    """Wrapper function for putting all things together."""
    
    options = parse_opts()
    config = _gen_config(options)
    passwd = _gen_pass(config)

    return config


def main():
    passwd = gen_passwd()
    print(f"Password: {passwd}")


if __name__ == "__main__":
    main()
