# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 5/31/23
"""
import pathlib
p_str = 'oath_json'

p1 = pathlib.Path(p_str)

p2 = pathlib.Path(p1)

print(p1 == p2)

print(p1 is p2)

print(p1, p2)