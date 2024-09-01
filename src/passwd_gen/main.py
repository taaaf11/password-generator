#####################################################

# Name: passwd-gen
# Author: Muhammad Altaaf <taafuuu@gmail.com>
# Description: A random password generator in your
# toolset.

#####################################################

from __future__ import annotations

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from dataclasses import dataclass

from .passwd_gen import gen_password

PROG_NAME = "passwd-gen"
PROG_DESC = """
┌─┐┌─┐┌─┐┌─┐┬ ┬┌┬┐   ┌─┐┌─┐┌┐┌
├─┘├─┤└─┐└─┐│││ ││───│ ┬├┤ │││
┴  ┴ ┴└─┘└─┘└┴┘─┴┘   └─┘└─┘┘└┘

A random password generator in your toolset.
"""

PROG_VERSION = "2.0.0"
PROG_AUTHOR = "Muhammad Altaaf"
PROG_AUTHOR_CONTACT = "taafuuu@gmail.com"
PROG_EPILOG = f"""\
Version {PROG_VERSION}.
Written by {PROG_AUTHOR} <{PROG_AUTHOR_CONTACT}>.
"""


@dataclass(frozen=True)
class _Config:
    wlist_filename: str
    join_char: str
    word_count: int


def parse_opts() -> _Config:
    """Parse command line options and return _Config object."""

    o_parser = ArgumentParser(
        prog=PROG_NAME,
        description=PROG_DESC,
        epilog=PROG_EPILOG,
        formatter_class=RawDescriptionHelpFormatter,
    )
    add_opt = o_parser.add_argument

    add_opt(
        "WORDLIST",
        type=str,
        help="Name of wordlist file.",
    )
    add_opt(
        "-j",
        "--join",
        type=str,
        default="-",
        help="Characters to join password's words with."
                " Default is \"-\"."
    )
    add_opt(
        "-c",
        "--count",
        type=int,
        default=5,
        help="Number of words to include in the generated password."
                " Default is 5.",
    )

    options = o_parser.parse_args()

    if options.count <= 0:
        o_parser.error("Word count is invalid.")

    config = _Config(options.WORDLIST, options.join, options.count)
    return config


def main():
    config: _Config = parse_opts()
    passwd: str = gen_password(
        filename=config.wlist_filename,
        join_char=config.join_char,
        word_count=config.word_count,
    )
    print(f"Password: {passwd}")


if __name__ == "__main__":
    main()
