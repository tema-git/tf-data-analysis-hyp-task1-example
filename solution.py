import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
chat_id = 401141478

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    sl = 0.01
    zstat, pval = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='smaller')

    return pval <= sl
