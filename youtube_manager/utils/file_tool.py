# coding: utf-8
"""
Author: Jet C.
GitHub: https://github.com/jet-c-21
Create Date: 5/31/23
"""
import json
import pathlib
from argparse import Namespace
from typing import Union, Dict, List

def read_json(fp: Union[str, pathlib.Path]) -> Dict:
    return json.load(open(fp, 'r', encoding='utf-8'))


def to_json(data: Union[Dict, Namespace, List], fp: Union[str, pathlib.Path], has_numpy=False):
    if isinstance(data, Namespace):
        data = vars(data)

    if has_numpy:
        json.dump(data, open(fp, 'w', encoding='utf-8'), indent=4, ensure_ascii=False, cls=NumpyEncoder)
        return

    json.dump(data, open(fp, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
