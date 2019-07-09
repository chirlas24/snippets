# SARIMAX MODEL

## Import libraries
```python
import statsmodels.api as sm
```

## WEB
https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html

## CODE
```python
mod = sm.tsa.statespace.SARIMAX( y
                                , trend='n'
                                , order=(p,d,q)
                                , seasonal_order=(P,D,Q,S)
                                , enforce_invertibility=False
                                , freq='M'  )
                                
results = mod.fit()

#Resultados de la estimacion:
print(results.summary().tables[1])

#Diagnostico de la estimacion:
results.plot_diagnostics(figsize=(15, 12))
plt.show()

#Prediction
pred = results.get_prediction(start=pd.to_datetime('1998-01-01'), dynamic=False)
```

## How to use the model:
https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3

## Little help for the times series hyperparameters understanding
https://towardsdatascience.com/understanding-the-hyperparameters-of-a-simple-time-series-model-631f26c46c9

## Best way to approach hyperparameters:
Gridsearch -> https://github.com/chirlas24/snippets/blob/master/machine_learning.md
