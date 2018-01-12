#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.compatible import version
from core.alert import __input_msg


def __input(msg, default):
    if version() is 2:
        try:
            data = raw_input(__input_msg(msg))
            if data == '':
                data = default
        except:
            data = default
    else:
        try:
            data = input(__input_msg(msg))
            if data == '':
                data = default
        except:
            data = default
    return data