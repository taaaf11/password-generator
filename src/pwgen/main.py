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
    """The main password generator."""

    passwd_len = config.length
    # string to get password characters from
    base = ""
    # the password
    passwd = ""

    if config.letters:
        base += "".join(c for c in BASE if c in ascii_letters)
    if config.digits:
        base += "".join(c for c in BASE if c in digits)
    if config.punct:
        base += "".join(c for c in BASE if c in punctuation)

    for _ in range(passwd_len):
        while (char := secrets.choice(base)) == "\\":
            continue
        passwd += char

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

    incl_letters = not cmd_opts.alphabets
    incl_digits = not cmd_opts.numbers
    incl_punct = not cmd_opts.punctuation
    p_len = options.length or 8

    config = _Config(incl_letters, incl_digits, incl_punct, p_len)
    return config

def gen_passwd() -> str:
    """Wrapper function for putting all things together."""

    options = parse_opts()
    config = _gen_config(options)
    passwd: str = _gen_pass(config)

    return passwd


def main():
    passwd = gen_passwd()
    print(f"Password: {passwd}")


if __name__ == "__main__":
    main()
