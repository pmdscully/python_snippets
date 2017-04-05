# Python Snippets

`Various bits of useful code` ..

# Matplotlib Grouped Boxplots - (July 2016)

Box and Whisker Plots or boxplots, are a hugely useful data visualisation tool to clearly compare algorithm configuration performance results (or experiment data with multiple dimensions). However, using Python’s Matplotlib library to implement them suitably for comparisons by groups used to be tough. To make them attractive and clear you had to stitch together documentation and examples and more examples and grids and line colours and axis labels and some very hacky legend use case, etc.. each taken from across the matplotlib site and beyond. So I wrote a couple of scripts to simplify grouped boxplots that can be directly reused..

Further details here: https://pmdscully.wordpress.com/2016/06/30/boxplots-data-visualisation/

# Recipe: Circular Nested Imports in Non-OOP Python Programs (Apr 2017)
Circular imports are not handled cleanly in Python 2.7x. The best solution is to avoid them. In this example, a structural problem-case is shown and the solution-case is presented by moving the shared code outside of the two code imports.

In object oriented programming (OOP) cases, there are a number of dependency patterns against which to match in order to find a solution. A reference to these can be found here: http://www.oodesign.com/

### Understanding Python 2.7's import management: 
The `sys.modules` dict variable is used by Python to store imported module objects (i.e. read and parsed from .py files) and the current execution state of the imported module. The module name is the dict's `key` lookup and `value` is its corresponding `module object`. 

`import xxx` and `from xxx import yyy` are executable statements. Upon execution of the line, if a module is not in `sys.modules`, then an import creates the new module dict entry in `sys.modules` and then executes the code in the module. It does not return control to the calling module until the execution has completed. If a module does exist in `sys.modules` then an import simply returns that module whether or not it has completed executing. That is the reason why cyclic imports may return modules which appear to be partly empty.

Details of sys.modules adapted from source:
http://stackoverflow.com/a/744403/1910555/
https://groups.google.com/forum/#!topic/comp.lang.python/HYChxtsrhnw

More Python import pitfalls and recipes at: 
http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html

# Unit Testing with `unittest` and `mock`: (Feb 2017)
    
Mock exists to remove the need to create stub classes to replace functionality in your unit tests. It captures method calls and enables assertions about those calls, enabling sub-system and unit testing to remain separated. 

More on Mock: https://mock.readthedocs.io/en/latest/
More on Py unit testing: https://docs.python.org/dev/library/unittest.mock.html

Install mock with: `pip install mock`
Run as: `python mock_unit_test.py`


# SciPy optimization wrapper (Apr 2017)

A wrapper to simplify use cases of global search with scipy.optimize, where inputs are a list of values and a function. Fixed input sequence element value `bounds` for lower/upper are set at `1.0` and `2.0` and the global search type is `scipy.optimize.basinhopping`.

Usage: 
- Extend the `Evaluator()` base class, and replace the `evaluate(x)` function.
- Extend the `Search()` base class wrapper to update the search method.


# Python Formal Method Validators via Added Decorators(Apr 2017)

A module of function (arg/return type) validation decorators written by Jackson Cooper at [pythoncentral.io](http://pythoncentral.io/validate-python-function-parameters-and-return-types-with-decorators/) that is so useful it should be a built-in.

Module provides function argument type and return type validators for @accept(a,b,c) and @returns(x,y,z) function decorators.

This simplifies the formalisation all function validation and is particularly useful for API interfaces definition.

Usage:
- `from function_validators import *`
- Then put `@accepts(type, type, ...)` and `@returns(type, type, ...)` above each of your functions; especially in Base/ABC classes.

Code Example:
- See `test_function_validators.py`



