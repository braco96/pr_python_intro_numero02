# -*- coding: utf-8 -*-
import re
def normalizar(s):
    if s is None:
        return ""
    return " ".join(str(s).strip().split()).lower()

