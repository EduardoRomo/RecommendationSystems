# -*- coding: utf-8 -*-

import numpy as np
from utils import *
from descent import *

def main():
    np.set_printoptions(precision=2, threshold=np.inf, linewidth=np.inf, suppress=False)

    use_netflix_data = True
    rank = 50

    if use_netflix_data:
        M = read_netflix_data()
        M_original = M.copy()
        M = low_rank_approximation(M, rank)
        mask = (M != 0)
    else:
        m, n = 400, 100
        density = 0.7
        mask = np.random.choice([True, False], (m, n), p=[density, 1-density])
        M = np.random.randint(1, 6, (m, n))
        M_original = M.copy()
        M = low_rank_approximation(M, rank)
        M = mask*M

    m, n = M.shape
    V0 = np.random.rand(n, rank)

    M_approx = optimize(M, V0, mask)

    if M_approx is not None:
        rmse_value = rmse(M_original, M_approx, mask)
        print("RMSE", rmse_value)

if __name__ == '__main__':
    main()
