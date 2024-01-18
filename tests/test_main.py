import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("s,esperado", [
    ("  Hola   Mundo ", "hola mundo"),
    ("\nLinea\t  doble  ", "linea doble"),
    (None, ""),
    ("ÁRBOL   ", "árbol"),
])
def test_normalizar(s, esperado):
    assert mod.normalizar(s) == esperado
