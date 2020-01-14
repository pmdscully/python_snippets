# What:
#   - Building custom 'with' blocks is good for handling Reliable Acquistion / Release Pairs (RA/RP)
#   - PEP doc: https://www.python.org/dev/peps/pep-0343/
# Why:
#   - Useful for handling of custom resources such as file, network, mutex locks.
#   - For example, when security audit reports are required for file interactions.
# How:
#   - Implement __enter__ and __exit__ custom blocks in a context manager, then use 'with Obj as o:'


import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

class LoggingFileManager(): 
    """
        Adapted from: https://www.geeksforgeeks.org/context-manager-in-python/
    """
    def __init__(self, filename, mode): 
        self.filename = filename 
        self.mode = mode 
        self.file = None
          
    def __enter__(self): 
        logging.info(f'Attempt to open filename:{self.filename} in mode:{self.mode}.')
        self.file = open(self.filename, self.mode) 
        logging.info(f'Opened filename:{self.filename} in mode:{self.mode}.')
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        logging.info(f'Attempt to close filename:{self.filename} in mode:{self.mode}.')
        self.file.close() 
        logging.info(f'Closed filename:{self.filename} in mode:{self.mode}.')
  
# loading a file  
with LoggingFileManager('test.txt', 'w') as f: 
    f.write('Test') 
  
print(f.closed) 