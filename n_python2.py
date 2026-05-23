import sys
print("Hello, World! My name is", sys.argv[1])

import cowsay
import sys 
if len(sys.argv)==2:
    cowsay.cow("Hello, "+sys.argv[1])
    
