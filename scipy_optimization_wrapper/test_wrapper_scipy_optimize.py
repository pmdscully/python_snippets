from __future__ import division
from wrapper_scipy_optimize import *


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
    test_fixed_function()
    test_std_sample()
