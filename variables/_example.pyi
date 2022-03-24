from example import SwigPyObject

class CvarInterface:
    ivar: int
    svar: int
    lvar: int
    uivar: int
    usvar: int
    ulvar: int
    scvar: int
    ucvar: int
    cvar: str
    fvar: float
    dvar: float
    strvar: str
    cstrvar: str
    iptrvar: SwigPyObject
    name: str
    ptptr: SwigPyObject
    pt: SwigPyObject
    status: int
    path: str

cvar: CvarInterface

def print_vars() -> None: ...
def new_int(value: int) -> SwigPyObject: ...
def new_Point(x: int, y: int) -> SwigPyObject: ...
def Point_print(p: SwigPyObject) -> str: ...
def pt_print() -> None: ...
