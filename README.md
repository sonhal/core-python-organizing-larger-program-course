# core-python-organizing-larger-program-course

### Notes

Modules most often correspond to a single file

Packages are special modules: Modules that can contain other modules

Package modules have a __path__ attribute


sys.path
 - list of directies
 - when python imports a module it checks sys.path in order.
 - ImportError is raised if the module is not found
 
 
PYTHONPATH
 - environment variable
 - list of paths added to sys.path
 
 Windows
 set PYTHONPATH=path1;path2;path3
 
 Linux/Mac
 export PYTHONPATH=path1:path2:path3
 

```
python -m demo_reader.compressed.gzipped test.gzip data compressed with gzip
```


### Relative vs absolute imports

..module_name import name

## __all__

- module level attribute
- Controls form module import * behavior
- if not specified import all public names
- must be a list of strings
- each entry is a module to import