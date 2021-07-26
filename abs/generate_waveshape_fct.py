'''

Part of EMEHG project.
Date : 17/07/2019
Author : Loïc Reboursière based on Alexandre Antoine's draft
Run with python generate_waveshape_fct.py 24 > generation.txt

'''

import numpy as np
import sys

def generate( fct = "cubic", size = 16 ) :

    x = np.random.rand( size )
    x = ( x * 2 ) - 1
    y = np.zeros( size )
    
    if( fct == "cubic" ) :
        y = x**3
    elif( fct == "clipped" ) :
        y = x / ( 1 + np.abs( x ) )
    elif( fct == "easycompute" ) :
        y = 1.5 * x + 0.5 * x**3

    return y
	
def main ( ) :

	if( len( sys.argv ) == 2 ) :
		print( "cubic", generate( size = int( sys.argv[ 1 ] ) ) )
		print( "clipped", generate( fct = "clipped", size = int( sys.argv[ 1 ] ) ) )
		print( "easycompute", generate( fct = "easycompute", size = int( sys.argv[ 1 ] ) ) )
	
	elif( len( sys.argv ) == 2 ) :
		print( "cubic", generate( ) )
		print( "clipped", generate( fct = "clipped" ) )
		print( "easycompute", generate( fct = "easycompute" ) )


if __name__ == '__main__':   
    main()
