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



# -------------------------------------------------------------------------------
# --- Evaluator Function Classes:
# -------------------------------------------------------------------------------    

class Search_Evaluator_Stdev_Sample(Evaluator):
    """
    Evaluator based on standard deviation, with small random deviations.
    """
    def __init__(self, seed=None):
        super(Evaluator, self).__init__()    #call super
        self.abc = 0.1
        import random as r
        self.r = r.Random()
        self.r.seed(seed)
        
    def evaluate(self, x):
        x[self.r.randint(0,len(x)-1)] += self.abc
        return np.std(x)


        
class Search_Evaluator_Fixed_Sample(Evaluator):
    """
    Evaluator based on a fixed function.
    """
    def __init__(self):
        super(Evaluator, self).__init__()    #call super
        
    def evaluate(self, x):
        return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
    
    
# -------------------------------------------------------------------------------
# --- Tests:
# -------------------------------------------------------------------------------
    
def test_std_sample():
    """
    Run a search to minimize standard deviation, while the function is randomly affecting some values.
    """
    # the starting point
    x0 = [10., 10.,9.,2.0,8.0]
    obj = Search_Evaluator_Stdev_Sample( seed=2 )                      
    minimise = Search( obj.evaluate )
    
    res = minimise.start( x0 )
    print res
    # Note: can't make assertions on result or final function evaluation of result, because Scipy shares, uses and reseeds the random object.

def test_fixed_function():
    """
    Run a search to minimize a sample polynomial function.
    """
    # the starting point
    x0 = [10., 10.,9.,2.0,8.0]
    obj = Search_Evaluator_Fixed_Sample() 
    minimise = Search( obj.evaluate )
    
    res = minimise.start( x0 )
    print res


if __name__ == "__main__":
    #test_std_sample()
    test_fixed_function()
