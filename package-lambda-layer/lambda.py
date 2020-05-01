import numpy as np
import pandas as pd
from scipy.stats import norm

def handler(event, context):
    dates = pd.date_range('20181201', periods=6)
    values = norm.rvs(size=6)
    df = pd.DataFrame(values, index=dates, columns=['A'])
    print(df)