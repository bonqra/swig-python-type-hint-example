from typing import Final, Literal

ICONST: Final[Literal[42]]
CCONST: Final[Literal["x"]]
CCONST2: Final[Literal["\n"]]
SCONST: Final[Literal["Hello World"]]
SCONST2: Final[Literal['"Hello World"']]
iconst: Final[Literal[37]]

# float literals are not supported (yet?)
# see https://peps.python.org/pep-0586/#illegal-parameters-for-literal-at-type-check-time

# FCONST: Final[Literal[2.1828]]
# EXPR: Final[Literal[48.5484]]
# fconst: Final[Literal[3.14]]

FCONST: Final[float]
EXPR: Final[float]
fconst: Final[float]
