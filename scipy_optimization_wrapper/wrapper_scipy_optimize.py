from __future__ import division
from abc import ABCMeta
from numbers import Number
from scipy.optimize import basinhopping
import numpy as np




# -------------------------------------------------------------------------------
# --- Search Execuation Class:
# -------------------------------------------------------------------------------    


class Search():
    """
    Handler class for searches using scipy.optimize.
    """
    def __init__(self, search_evaluation_function):
        """
        @param: evaluation function object:
        """
        self.f = search_evaluation_function
        
    def start(self, seq_to_optimize):
        """
        @param: The starting list of values to be optimised.
        Note that the value bounds per element are fixed.
        """
        x0 = seq_to_optimize
        assert isinstance(x0, list) and len(x0) > 0 and all([isinstance(x, Number) for x in x0]),  \
            "Input sequence should be a list of type numbers.Number."
            
        # the bounds
        xmin = [1.0]*len(x0)
        xmax = [2.0]*len(x0)

        # rewrite the bounds in the way required by L-BFGS-B
        bounds = [(low, high) for low, high in zip(xmin, xmax)]

        # use method L-BFGS-B because the problem is smooth and bounded
        minimizer_kwargs = dict(method="L-BFGS-B", bounds=bounds)
        res = basinhopping(self.f, x0, minimizer_kwargs=minimizer_kwargs)
        return res


# -------------------------------------------------------------------------------
# --- Evaluator Function Base Class:
# -------------------------------------------------------------------------------
    

class Evaluator():
    """
    Abstract Base Class (ABC) for search evaluators.
    """
    __metaclass__ = ABCMeta
    def __init__(self):
        """
        constructor
        """
        
    def evaluate(self, x): 
        """
        
        """
        return 0.0

