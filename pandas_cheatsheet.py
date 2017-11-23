# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/42770379/pandas-change-order-of-crosstab-result
import pandas as pd
pd.crosstab().sort_values('column_name', ascending=False)
