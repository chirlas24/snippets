# Import libraries

import statsmodels.api as sm

# SARIMAX model

```python
mod = sm.tsa.statespace.SARIMAX( output
                                , trend='n'
                                , order=(1,1,0)
                                , seasonal_order=(0,1,1,12)
                                , enforce_invertibility=False
                                , freq='M'  )
```
