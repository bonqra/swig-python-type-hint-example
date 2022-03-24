# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.1.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info  # pyright: reportUnusedImport=false

from typing import Any, Callable, Iterator, Mapping, MutableMapping, TYPE_CHECKING, TypeVar, overload
from typing_extensions import Self

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _example
else:
    import _example

if TYPE_CHECKING:
    import builtins as __builtin__
else:
    try:
        import builtins as __builtin__
    except ImportError:
        import __builtin__


class SwigPyObject:
    def disown(self: Self) -> None:
        ...

    def acquire(self: Self) -> None:
        ...

    def own(self: Self, v: "SwigPyObject | None" = None) -> bool:
        ...


class SwigPyObjectHolder:
    this: SwigPyObject

    def __repr__(self: Self) -> str:
        ...


def _swig_repr(self: SwigPyObjectHolder) -> str:  # pyright: reportUnusedFunction=false
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (
        self.__class__.__module__,
        self.__class__.__name__,
        strthis,
    )


def _swig_setattr_nondynamic_instance_variable(
    set: Callable[[SwigPyObjectHolder, str, Any], None]
) -> Callable[
    [SwigPyObjectHolder, str, Any], None
]:  # pyright: reportUnusedFunction=false
    def set_instance_attr(self: SwigPyObjectHolder, name: str, value: Any):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)

    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(
    set: Callable[[type, str, Any], None]
) -> Callable[[type, str, Any], None]:  # pyright: reportUnusedFunction=false
    def set_class_attr(cls: type, name: str, value: Any):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)

    return set_class_attr


def _swig_add_metaclass(metaclass: type):  # pyright: reportUnusedFunction=false
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""

    def wrapper(cls: type):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())

    return wrapper


class _SwigNonDynamicMeta(type):  # pyright: reportUnusedClass=false
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""

    __setattr__: Callable[
        [type, str, Any], None
    ] = _swig_setattr_nondynamic_class_variable(type.__setattr__)


T = TypeVar("T")


class SwigPyIterator(SwigPyObjectHolder, Iterator[T]):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_destroy__ = _example.delete_SwigPyIterator

    def value(self: Self) -> T:
        return _example.SwigPyIterator_value(self)

    def incr(self: Self, n: int = 1) -> Self:
        return _example.SwigPyIterator_incr(self, n)

    def decr(self: Self, n: int = 1) -> Self:
        return _example.SwigPyIterator_decr(self, n)

    def distance(self: Self, x: Self) -> int:
        return _example.SwigPyIterator_distance(self, x)

    def equal(self: Self, x: Self) -> bool:
        return _example.SwigPyIterator_equal(self, x)

    def copy(self: Self) -> Self:
        return _example.SwigPyIterator_copy(self)

    def next(self: Self) -> T:
        return _example.SwigPyIterator_next(self)

    def __next__(self: Self) -> T:
        return _example.SwigPyIterator___next__(self)

    def previous(self: Self) -> T:
        return _example.SwigPyIterator_previous(self)

    def advance(self: Self, n: int):
        return _example.SwigPyIterator_advance(self, n)

    def __eq__(self: Self, x: Self) -> bool:
        return _example.SwigPyIterator___eq__(self, x)

    def __ne__(self: Self, x: Self) -> bool:
        return _example.SwigPyIterator___ne__(self, x)

    def __iadd__(self: Self, n: int) -> Self:
        return _example.SwigPyIterator___iadd__(self, n)

    def __isub__(self: Self, n: int) -> Self:
        return _example.SwigPyIterator___isub__(self, n)

    def __add__(self: Self, n: int) -> Self:
        return _example.SwigPyIterator___add__(self, n)

    @overload
    def __sub__(self: Self, x: Self, /) -> Self:
        ...

    @overload
    def __sub__(self: Self, n: int, x: Self, /) -> Self:
        ...

    def __sub__(self: Self, *args: Any) -> Self:
        return _example.SwigPyIterator___sub__(self, *args)

    def __iter__(self) -> Self:
        return self


# Register SwigPyIterator in _example:
_example.SwigPyIterator_swigregister(SwigPyIterator)


class DoubleMap(SwigPyObjectHolder, MutableMapping[str, float]):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )
    __repr__ = _swig_repr

    def iterator(self: Self) -> SwigPyIterator[str]:
        return _example.DoubleMap_iterator(self)

    def __iter__(self: Self) -> SwigPyIterator[str]:
        return self.iterator()

    def __nonzero__(self: Self) -> bool:
        return _example.DoubleMap___nonzero__(self)

    def __bool__(self: Self) -> bool:
        return _example.DoubleMap___bool__(self)

    def __len__(self: Self) -> int:
        return _example.DoubleMap___len__(self)

    def __iter__(self: Self) -> SwigPyIterator[str]:
        return self.key_iterator()

    def iterkeys(self: Self) -> SwigPyIterator[str]:
        return self.key_iterator()

    def itervalues(self: Self) -> SwigPyIterator[float]:
        return self.value_iterator()

    def iteritems(self: Self) -> SwigPyIterator[str]:
        return self.iterator()

    def __getitem__(self: Self, key: str) -> float:
        return _example.DoubleMap___getitem__(self, key)

    def __delitem__(self: Self, key: str) -> None:
        return _example.DoubleMap___delitem__(self, key)

    def has_key(self: Self, key: str) -> bool:
        return _example.DoubleMap_has_key(self, key)

    def keys(self: Self) -> list[str]:
        return _example.DoubleMap_keys(self)

    def values(self: Self) -> list[float]:
        return _example.DoubleMap_values(self)

    def items(self: Self) -> list[tuple[str, float]]:
        return _example.DoubleMap_items(self)

    def __contains__(self: Self, key: str) -> bool:
        return _example.DoubleMap___contains__(self, key)

    def key_iterator(self: Self) -> SwigPyIterator[str]:
        return _example.DoubleMap_key_iterator(self)

    def value_iterator(self: Self) -> SwigPyIterator[float]:
        return _example.DoubleMap_value_iterator(self)

    @overload
    def __setitem__(self: Self, key: str, /) -> None:
        ...

    @overload
    def __setitem__(self: Self, key: str, value: float, /) -> None:
        ...

    def __setitem__(self: Self, *args: Any) -> None:
        return _example.DoubleMap___setitem__(self, *args)

    def asdict(self: Self) -> dict[str, float]:
        return _example.DoubleMap_asdict(self)

    @overload
    def __init__(self: Self) -> None:
        ...

    # @overload
    # def __init__(self: DoubleMap, comparator: ?, /) -> None:
    #     ...

    @overload
    def __init__(self: Self, map: Mapping[str, float], /) -> None:
        ...

    def __init__(self: Self, *args: Any) -> None:
        _example.DoubleMap_swiginit(self, _example.new_DoubleMap(*args))

    def empty(self: Self) -> bool:
        return _example.DoubleMap_empty(self)

    def size(self: Self) -> int:
        return _example.DoubleMap_size(self)

    def swap(self: Self, v: Self) -> None:
        return _example.DoubleMap_swap(self, v)

    def begin(self: Self) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_begin(self)

    def end(self: Self) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_end(self)

    def rbegin(self: Self) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_rbegin(self)

    def rend(self: Self) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_rend(self)

    def clear(self: Self) -> None:
        return _example.DoubleMap_clear(self)

    def get_allocator(self: Self) -> SwigPyObject:
        return _example.DoubleMap_get_allocator(self)

    def count(self: Self, x: str) -> int:
        return _example.DoubleMap_count(self, x)

    @overload
    def erase(self: Self, key: str, /) -> int:
        ...

    @overload
    def erase(self: Self, pos: SwigPyIterator[tuple[str, float]], /) -> None:
        ...

    @overload
    def erase(self: Self, first: SwigPyIterator[tuple[str, float]], last: SwigPyIterator[tuple[str, float]], /) -> None:
        ...

    def erase(self: Self, *args: Any) -> int | None:
        return _example.DoubleMap_erase(self, *args)

    def find(self: Self, x: str) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_find(self, x)

    def lower_bound(self: Self, x: str) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_lower_bound(self, x)

    def upper_bound(self: Self, x: str) -> SwigPyIterator[tuple[str, float]]:
        return _example.DoubleMap_upper_bound(self, x)

    __swig_destroy__ = _example.delete_DoubleMap


# Register DoubleMap in _example:
_example.DoubleMap_swigregister(DoubleMap)

def halfd(v: Mapping[str, float]) -> DoubleMap:
    return _example.halfd(v)


def halfi(v: Mapping[str, int]) -> Mapping[str, int]:
    return _example.halfi(v)


class pymap(SwigPyObjectHolder, MutableMapping[Any, Any]):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )
    __repr__ = _swig_repr

    def iterator(self: Self) -> SwigPyIterator[Any]:
        return _example.pymap_iterator(self)

    def __iter__(self: Self) -> SwigPyIterator[Any]:
        return self.iterator()

    def __nonzero__(self: Self) -> bool:
        return _example.pymap___nonzero__(self)

    def __bool__(self: Self) -> bool:
        return _example.pymap___bool__(self)

    def __len__(self: Self) -> int:
        return _example.pymap___len__(self)

    def __iter__(self: Self) -> SwigPyIterator[Any]:
        return self.key_iterator()

    def iterkeys(self: Self) -> SwigPyIterator[Any]:
        return self.key_iterator()

    def itervalues(self: Self) -> SwigPyIterator[Any]:
        return self.value_iterator()

    def iteritems(self: Self) -> SwigPyIterator[Any]:
        return self.iterator()

    def __getitem__(self: Self, key: Any) -> Any:
        return _example.pymap___getitem__(self, key)

    def __delitem__(self: Self, key: Any) -> None:
        return _example.pymap___delitem__(self, key)

    def has_key(self: Self, key: Any) -> bool:
        return _example.pymap_has_key(self, key)

    def keys(self: Self) -> list[Any]:
        return _example.pymap_keys(self)

    def values(self: Self) -> list[Any]:
        return _example.pymap_values(self)

    def items(self: Self) -> list[tuple[Any, Any]]:
        return _example.pymap_items(self)

    def __contains__(self: Self, key: Any) -> bool:
        return _example.pymap___contains__(self, key)

    def key_iterator(self: Self) -> SwigPyIterator[Any]:
        return _example.pymap_key_iterator(self)

    def value_iterator(self: Self) -> SwigPyIterator[Any]:
        return _example.pymap_value_iterator(self)

    @overload
    def __setitem__(self: Self, key: Any, /) -> None:
        ...

    @overload
    def __setitem__(self: Self, key: Any, value: Any, /) -> None:
        ...

    def __setitem__(self: Self, *args: Any) -> None:
        return _example.pymap___setitem__(self, *args)

    def asdict(self: Self) -> dict[Any, Any]:
        return _example.pymap_asdict(self)

    @overload
    def __init__(self: Self) -> None:
        ...

    # @overload
    # def __init__(self: pymap, comparator: ?, /) -> None:
    #     ...

    @overload
    def __init__(self: Self, map: Mapping[Any, Any], /) -> None:
        ...

    def __init__(self: Self, *args: Any) -> None:
        _example.pymap_swiginit(self, _example.new_pymap(*args))

    def empty(self: Self) -> bool:
        return _example.pymap_empty(self)

    def size(self: Self) -> int:
        return _example.pymap_size(self)

    def swap(self: Self, v: Self) -> None:
        return _example.pymap_swap(self, v)

    def begin(self: Self) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_begin(self)

    def end(self: Self) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_end(self)

    def rbegin(self: Self) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_rbegin(self)

    def rend(self: Self) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_rend(self)

    def clear(self: Self) -> None:
        return _example.pymap_clear(self)

    def get_allocator(self: Self) -> SwigPyObject:
        return _example.pymap_get_allocator(self)

    def count(self: Self, x: Any) -> int:
        return _example.pymap_count(self, x)

    @overload
    def erase(self: Self, key: Any, /) -> int:
        ...

    @overload
    def erase(self: Self, pos: SwigPyIterator[tuple[Any, Any]], /) -> None:
        ...

    @overload
    def erase(self: Self, first: SwigPyIterator[tuple[Any, Any]], last: SwigPyIterator[tuple[Any, Any]], /) -> None:
        ...

    def erase(self: Self, *args: Any) -> int | None:
        return _example.pymap_erase(self, *args)

    def find(self: Self, x: Any) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_find(self, x)

    def lower_bound(self: Self, x: Any) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_lower_bound(self, x)

    def upper_bound(self: Self, x: Any) -> SwigPyIterator[tuple[Any, Any]]:
        return _example.pymap_upper_bound(self, x)

    __swig_destroy__ = _example.delete_pymap


# Register pymap in _example:
_example.pymap_swigregister(pymap)