
def finalGuarantee(eps, gnorm = 1, q=1,T=10):
"""
Function that computes final privacy guarantee 
for an iterative composition (as in gradient descent)
Args:
    eps: list of potential epsilons, e.g. eps = np.array([0.001,0.01,0.1])
    gnorm: bound on gradient norm
    q: sparsity+communication rate. Proportion of entries received 
    T: total iterations

  Returns:
    A `tff.templates.IterativeProcess`.
"""
	eps = np.array([0.001,0.01,0.1,1])
    c = np.sqrt(sigma)*eps/gnorm
    delta = 1.25*np.exp((-c*c)/2)
    print('DP guarantees \n :')
    print('  epsilon    -    delta  ')
    for j in range(len(eps)):
        print('  {}    -    {}  '.format(eps[j]*T*q, delta[j]*T*q))
