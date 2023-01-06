"""A Pygments lexer for SR Linux configuration snippets."""
import re
from pygments.lexer import RegexLexer
from pygments.token import *
from .parsers import (
    srl_prompt,
    comments,
    strings,
    keywords,
    pos_words,
    neg_words,
    sys_lo_if,
    eth_if,
    ipv4,
    ipv6,
    nums,
)

__all__ = ("SRLinuxLexer",)


class SRLinuxLexer(RegexLexer):

    """
    A lexer to highlight SR Linux CLI snippets.
    """

    name = "SR Linux"
    aliases = ["srl"]
    flags = re.MULTILINE | re.IGNORECASE

    tokens = {"root": []}

    tokens["root"].extend(srl_prompt)
    tokens["root"].extend(comments)
    tokens["root"].extend(strings)
    tokens["root"].extend(keywords)
    tokens["root"].extend(pos_words)
    tokens["root"].extend(neg_words)
    tokens["root"].extend(eth_if)
    tokens["root"].extend(sys_lo_if)
    tokens["root"].extend(ipv4)
    tokens["root"].extend(ipv6)
    tokens["root"].extend(nums)
