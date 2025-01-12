import numpy as np


def online_lasso(yn: float, Xn: np.ndarray, xy: np.ndarray, xx: np.ndarray, theta: np.ndarray, all_but_j: list, P: int, var_y: float):
    
    ''' This function is the update step of the proposed online lasso for each data arrival

        yn: n(th) data label
        Xn: n(th) Input feature
        xy, xx: Update terms - corresponding to v and d in the paper
        theta: The parameter to be estimated - of size P x 1
        all_but_j: An auxiliary variable where each element is a list that stores all indices except the j(th)
        P: Total avaliable features
        var_y: variance of observation noise - corresponding to sigma^2 in the paper
    '''
    # Update top
    xy = xy + Xn*yn

    # Update denominators for each feature
    xx[0] = xx[0] + Xn.T**2

    # Lambda - the penalty parameter
    penalty = np.sqrt(np.sum(xx)*var_y)


    for j in range(P):
    
        # Data term
        xy[j] = xy[j] - Xn[j]*np.sum(Xn[all_but_j[j]]*theta[all_but_j[j]])
      
        theta[j] = np.sign(xy[j])*max(abs(xy[j]) - penalty, 0)/ xx[0][j]

    
    return theta, xy, xx