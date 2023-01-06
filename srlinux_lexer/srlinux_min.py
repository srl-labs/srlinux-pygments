"""A Pygments lexer for SR Linux configuration snippets."""
import re
from pygments.lexer import RegexLexer
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
)

__all__ = ("SRLinuxLexerMin",)


class SRLinuxLexerMin(RegexLexer):

    """
    A minimilized lexer to highlight SR Linux CLI snippets.
    The differences with the full fledged lexer is that minimal version doesn't highlight numbers
    """

    name = "SR Linux Minimal"
    aliases = ["srlmin"]
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
