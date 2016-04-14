# -*- coding: utf-8 -*-
import re
import os

_pattern_html = re.compile('<[^<]+?>')
_pattern_tag = re.compile('#.+#')
_pattern_at = re.compile('@.+')
_pattern_symbol = re.compile('[_.]+')


def _remove_html(s):
    return _pattern_html.sub('', s)


def _remove_tag(s):
    return _pattern_tag.sub('', s)


def _remove_at(s):
    return _pattern_at.sub('', s)


def _remove_symbol(s):
    return _pattern_symbol.sub('', s)


def clean(s):
    s = _remove_html(s)
    s = _remove_tag(s)
    s = _remove_at(s)
    s = _remove_symbol(s)
    return s
