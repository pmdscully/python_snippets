# Python Snippets

Various bits of useful code ..

# Matplotlib Grouped Boxplots

Box and Whisker Plots or boxplots, are a hugely useful data visualisation tool to clearly compare algorithm configuration performance results (or experiment data with multiple dimensions). However, using Python’s Matplotlib library to implement them suitably for comparisons by groups used to be tough. To make them attractive and clear you had to stitch together documentation and examples and more examples and grids and line colours and axis labels and some very hacky legend use case, etc.. each taken from across the matplotlib site and beyond. So I wrote a couple of scripts to simplify grouped boxplots that can be directly reused..


# Recipe: Circular Nested Imports in Non-OOP Python Programs.
Circular imports are not handled cleanly in Python 2.7x. The best solution is to avoid them. In this example, a structural problem-case is shown and the solution-case is presented by moving the shared code outside of the two code imports.

In object oriented programming (OOP) cases, there are a number of dependency patterns against which to match in order to find a solution. A reference to these can be found here: http://www.oodesign.com/

### Understanding Python 2.7's import management: 
The sys.modules dict variable is used by Python to store imported module objects (i.e. read and parsed from .py files) and the current execution state of the imported module. The module name is the dict's key lookup and value is its corresponding module object. 

'import' and 'from xxx import yyy' are executable statements. Upon execution of the line, if a module is not in sys.modules, then an import creates the new module entry in sys.modules and then executes the code in the module. It does not return control to the calling module until the execution has completed. If a module does exist in sys.modules then an import simply returns that module whether or not it has completed executing. That is the reason why cyclic imports may return modules which appear to be partly empty.

Details of sys.modules adapted from source:
http://stackoverflow.com/a/744403/1910555/
https://groups.google.com/forum/#!topic/comp.lang.python/HYChxtsrhnw

More Python import pitfalls and recipes at: 
http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html
