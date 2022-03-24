# SWIG Python Type Hints Example

This is a demonstration of the Python type hints discussed in [swig/swig#735](https://github.com/swig/swig/issues/735).

It is based on the following SWIG Python examples:

- [class example](https://github.com/swig/swig/tree/master/Examples/python/class)
- [constants example](https://github.com/swig/swig/tree/master/Examples/python/constants)
- [std_map example](https://github.com/swig/swig/tree/master/Examples/python/std_map)
- [std_vector example](https://github.com/swig/swig/tree/master/Examples/python/std_vector)
- [variables example](https://github.com/swig/swig/tree/master/Examples/python/variables)

All Python code has been formatted with black.

## Setup

- Clone
- Build extension with `make`
- Open in VSCode
  - Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (Ctrl+P then `ext install ms-python.python`)
  - The Python analysis type checking mode has been set to "strict" for this workspace in [.vscode/settings.json](.vscode/settings.json)
- Open the `runme.py` files to see the type checking in action
  - "Go to definition" default key is F12
- The compiled modules are typed in the `_example.pyi` files
- Everything else is typed inline in the `example.py` files
