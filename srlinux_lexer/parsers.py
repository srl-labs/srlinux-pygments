import re
from pygments.lexer import bygroups, words
from pygments.token import *
from .words import KEYWORD_LIST, POSITIVE_LIST, NEGATIVE_LIST

srl_prompt = [
    # prompt 1st line
    (r"^--.+--$", Comment),
    # prompt 2nd line. https://regex101.com/r/602F7B/1
    (
        r"^([A-Z]{1}\S+#)(\s+)(.+)$",
        bygroups(Text, Text, Name),
    ),
]

comments = [
    # comments in the CLI snippets `#`. https://regex101.com/r/dtR80f/1
    (
        r"^\s*#.*$",
        Comment,
    ),
]

strings = [
    # String
    (
        r"\s\".+\"\s",
        Literal,
    ),
]

keywords = [(words(KEYWORD_LIST, prefix=r"\b", suffix=r"\b"), Keyword.Reserved)]

pos_words = [(words(POSITIVE_LIST, prefix=r"\b", suffix=r"\b"), Literal)]

neg_words = [(words(NEGATIVE_LIST, prefix=r"\b", suffix=r"\b"), String.Escape)]

eth_if = [
    # ethernet-x/y/z.xxx interfaces. https://regex101.com/r/1mxxaA/1
    (
        r"ethernet-\d+\/\d+(\/\d+)?(\.\d+)?",
        Name.Constant,
    )
]

sys_lo_if = [
    # systemX.Y and loX.Y interfaces. https://regex101.com/r/T7UlHK/1
    (
        r"(system|lo)\d+(\.\d+)?",
        Name.Constant,
    )
]

ipv4 = [
    # IPv4 prefix. https://regex101.com/r/ZmksYg/1
    (
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,3})?\s",
        Name.Constant,
    )
]

ipv6 = [  # IPv6 addr and CIDR. https://regex101.com/r/U1jrZ9/1
    (
        r"(((?:[0-9A-Fa-f]{1,4}))*((?::[0-9A-Fa-f]{1,4}))*::((?:[0-9A-Fa-f]{1,4}))*((?::[0-9A-Fa-f]{1,4}))*|((?:[0-9A-Fa-f]{1,4}))((?::[0-9A-Fa-f]{1,4})){7})(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[1-9])){0,1}",
        Name.Constant,
    )
]

nums = [
    # Numbers https://regex101.com/r/qxQWER/1
    (
        r"(?:(\d+)(,)\s*(\d+))|(?:(\s)(\d+)(\s))|(?:([\[(,])(\d+))|(?:(\/)(\d+))",
        bygroups(
            Name.Constant,
            Text,
            Name.Constant,
            Text,
            Name.Constant,
            Text,
            Text,
            Name.Constant,
            Text,
            Name.Constant,
        ),
    )
]
