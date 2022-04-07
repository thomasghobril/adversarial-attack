import numpy as np
from math import pi


# PROCEDURE : X_normalised = (X - X_mean)/X_range
# X = [rho, theta, psi, v_own, v_int] (in that order)

X_mean = np.array( [1.9791091*10e4, 0.0, 0.0, 650.0, 600.0] )
X_range = np.array( [60261.0, 6.28318530718, 6.28318530718, 1100.0, 1200.0] )

X_dom = np.array([ [0.0,    -pi, -pi, 100.0,     0.0],
                   [60760.0, pi,  pi, 1200.0, 1200.0] ])

# u = np.true_divide(x - X_mean, X_range) # element-wise division


# PROPERTY 1

IP1_dom = [np.array( [ [55947.691, None, None, 1145, None],
                       [None     , None, None, None, 60] ])]

def IP1(x):
    """ Check if inputs of property 1 are satisfied. """
    return( (x[0] >= 55947.691) and (x[3] >= 1145) and (x[4] <= 60) )
    
def OP1(x, coc_mean=7.5188840201005975, coc_range=373.94992):
    """ Check if outputs of property 1 are satisfied. """
    coc = (x[0] - coc_mean)/coc_range
    return(coc <= 1500)


# PROPERTY 2

IP2_dom = [np.array( [ [55947.691, None, None, 1145, None],
                       [None     , None, None, None, 60] ])]

def IP2(x):
    return( (x[0] >= 55947.691) and (x[3] >= 1145) and (x[4] <= 60) )

def OP2(x):
    """ COC score is not the maximal score. """
    return(np.argmax(x) != 0)


# PROPERTY 3

IP3_dom = [np.array( [ [1500.0, -0.06, 3.10, 980.0, 960.0],
                       [1800.0,  0.06, None,  None,  None] ])]

def IP3(x):
    return( (1500.0 <= x[0] <= 1800.0) and (-0.06 <= x[1] <= 0.06) and (3.10 <= x[2]) and (980.0 <= x[3]) and (960.0 <= x[4]) )

def OP3(x):
    """ COC score is not the minimal score. """
    return(np.argmin(x) != 0)


# PROPERTY 4

def IP4(x):
    return( (1500.0 <= x[0] <= 1800.0) and (-0.06 <= x[1] <= 0.06) and (x[2] == 0) and (1000.0 <= x[3]) and (700.0 <= x[4] <= 800.0) )

def OP4(x):
    """ COC score is not the minimal score. """
    return(np.argmin(x) != 0)


# PROPERTY 5

def IP5(x):
    return( (250.0 <= x[0] <= 400.0) and (0.2 <= x[1] <= 0.4) and (-3.141592 <= x[2] <= -3.141592 + 0.005) and (100.0 <= x[3] <= 400.0) and (0.0 <= x[4] <= 400.0) )

def OP5(x):
    """ SRC score is the minimal score. """
    return(np.argmin(x) == 3)


# PROPERTY 6

def IP6(x):
    return( (12000.0 <= x[0] <= 62000.0) and ((0.7 <= x[1] <= 3.141592) or (-3.141592 <= x[1] <= -0.7)) and (-3.141592 <= x[2] <= -3.141592+0.005) and (100.0 <= x[3] <= 1200.0) and (0.0 <= x[4] <= 1200.0) )

def OP6(x):
    """ COC score is the minimal score. """
    return(np.argmin(x) == 0)


# PROPERTY 7

def IP7(x):
    return( (12000.0 <= x[0] <= 60760.0) and (-3.141592 <= x[1] <= 3.141592) and (-3.141592 <= x[2] <= 3.141592) and (100.0 <= x[3] <= 1200.0) and (0.0 <= x[4] <= 1200.0) )

def OP7(x):
    """ SR score and SL score are not the minimal scores. """
    min_score_ind = np.argmin(x)
    return( (min_score_ind != 3) and (min_score_ind != 4) )


# PROPERTY 8

def IP8(x):
    return( (0.0 <= x[0] <= 60760.0) and (-3.141592 <= x[1] <= -0.75*3.141592) and (-0.1 <= x[2] <= 0.1) and (600.0 <= x[3] <= 1200.0) and (600.0 <= x[4] <= 1200.0) )

def OP8(x):
    """ COC score or WL score is the minimal score. """
    min_score_ind = np.argmin(x)
    return( (min_score_ind == 0) and (min_score_ind == 2) )


# PROPERTY 9

def IP9(x):
    return( (2000.0 <= x[0] <= 7000.0) and (-0.4 <= x[1] <= -0.14) and (-3.141592 <= x[2] <= -3.141592+0.01) and (100.0 <= x[3] <= 150.0) and (0.0 <= x[4] <= 150.0) )

def OP9(x):
    """ SL score is the minimal score. """
    return(np.argmin(x) == 4)


# PROPERTY 10

def IP10(x):
    return( (36000.0 <= x[0] <= 60760.0) and (0.7 <= x[1] <= 3.141592) and (-3.141592 <= x[2] <= -3.141592+0.01) and (900.0 <= x[3] <= 1200.0) and (600.0 <= x[4] <= 1200.0) )

def OP10(x):
    """ COC score is the minimal score. """
    return(np.argmin(x) == 0)
