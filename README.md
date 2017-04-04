# Python Snippets

Various bits of useful code ..

## Matplotlib Grouped Boxplots

## Recipe: Circular Nested Imports in Non-OOP Python Programs.
In this module-function program (without objects/classes) the solution shown is to the move the shared code to separate
module. For the OOP case, you should match the problem one of the OO dependency patterns, there are many (e.g. http://www.oodesign.com/)..

How Python imports are managed: -- The sys.modules dict variable contains the imported module objects (read and parsed
python files) and the current state of the module. The key lookup is on the module name and value is a module object.
'import' and 'from xxx import yyy' are executable statements. If a module is not in sys.modules, then an import creates
the new module entry in sys.modules and then executes the code in the module. It does not return control to the calling
module until the execution has completed. If a module does exist in sys.modules then an import simply returns that
module whether or not it has completed executing. That is the reason why cyclic imports may return modules which appear
to be partly empty.

Adapted from source:
http://stackoverflow.com/a/744403/1910555/
https://groups.google.com/forum/#!topic/comp.lang.python/HYChxtsrhnw

More Python import pitfalls and recipes at: http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html

