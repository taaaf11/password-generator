#####################################################

# Name: passwd-gen
# Author: Muhammad Altaaf <taafuuu@gmail.com>
# Description: A random password generator in your
# toolset.

#####################################################

from __future__ import annotations

import secrets
import string
import sys
import typing
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from dataclasses import dataclass

if typing.TYPE_CHECKING:
    from argparse import Namespace

PROG_NAME = "passwd-gen"
PROG_DESC = """
██████╗  █████╗ ███████╗███████╗██╗    ██╗██████╗        ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔══██╗      ██╔════╝ ██╔════╝
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║  ██║█████╗██║  ███╗█████╗  
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║  ██║╚════╝██║   ██║██╔══╝  
██║     ██║  ██║███████║███████║╚███╔███╔╝██████╔╝      ╚██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═════╝        ╚═════╝ ╚══════╝
                                                                         
███╗   ██╗                                                               
████╗  ██║                                                               
██╔██╗ ██║                                                               
██║╚██╗██║                                                               
██║ ╚████║                                                               
╚═╝  ╚═══╝                                                               

A random password generator in your toolset.
"""

PROG_VERSION = "1.1.0"
PROG_AUTHOR = "Muhammad Altaaf"
PROG_AUTHOR_CONTACT = "taafuuu@gmail.com"
PROG_EPILOG = f"""\
Version {PROG_VERSION}.
Written by {PROG_AUTHOR} <{PROG_AUTHOR_CONTACT}>.
"""


@dataclass(frozen=True)
class _Config:
    letters: bool = True
    digits: bool = True
    punct: bool = True
    length: int = 8

    def __post_init__(self):
        if not (self.letters or self.digits or self.punct):
            print(
                "At least one of the three components (alphabets, numbers or \
                symbols) must be allowed",
                file=sys.stderr,
            )
            sys.exit(1)


def _gen_passwd(config: _Config) -> str:
    """The main password generator."""

    passwd_len = config.length
    # string to get password characters from
    base = ""
    # the password
    passwd = ""

    if config.letters:
        base += string.ascii_letters
    if config.digits:
        base += string.digits
    if config.punct:
        base += string.punctuation

    for _ in range(passwd_len):
        while (char := secrets.choice(base)) == "\\":
            continue
        passwd += char

    return passwd


def parse_opts() -> Namespace:
    """Parse command line options and return Namespace object."""

    o_parser = ArgumentParser(
        prog=PROG_NAME,
        description=PROG_DESC,
        epilog=PROG_EPILOG,
        formatter_class=RawDescriptionHelpFormatter,
    )
    add_opt = o_parser.add_argument

    add_opt(
        "-a",
        "--alphabets",
        action="store_true",
        help="Don't include alphabets in the password. (Default is to include)",
    )
    add_opt(
        "-n",
        "--numbers",
        action="store_true",
        help="Don't include numbers in the password. (Default is to include)",
    )
    add_opt(
        "-p",
        "--punctuation",
        action="store_true",
        help="Don't include symbols in the password. (Default is to include)",
    )
    add_opt("-l",
            "--length",
            type=int,
            help="Length of the password. (Default is 8)",
            )

    return o_parser.parse_args()


def gen_config(cmd_opts: Namespace) -> _Config:
    """Generate config from arguments."""

    incl_letters = not cmd_opts.alphabets
    incl_digits = not cmd_opts.numbers
    incl_punct = not cmd_opts.punctuation
    p_len = cmd_opts.length or 8

    config = _Config(incl_letters, incl_digits, incl_punct, p_len)
    return config


def gen_passwd() -> str:
    """Wrapper function for putting all things together."""

    options = parse_opts()
    config = gen_config(options)
    passwd: str = _gen_passwd(config)

    return passwd


def main():
    passwd = gen_passwd()
    print(f"Password: {passwd}")


if __name__ == "__main__":
    main()
