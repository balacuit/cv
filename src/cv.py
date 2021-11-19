#!/usr/bin/env python
from textwrap import TextWrapper
import textwrap
from datetime import datetime
from utils import (CV, coalesce, dump, read_yaml,
   tab_indent, resolve_ref)


if __name__ == "__main__":
    data = read_yaml("cv.yaml")

    for k,v in data.items():
        if "$ref" in v:
            data[k] = resolve_ref("../" + v['$ref'])
            print(dump(data))
