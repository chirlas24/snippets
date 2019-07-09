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
prediction = results.get_prediction(start=pd.to_datetime('2019-06-30'),end=pd.to_datetime('2020-02-29'))
#Intervalos de confianza
prediction_ci = prediction.conf_int()
#Media
prediciton_mean = prediction.predicted_mean
```

## How to use the model:
https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3

## Little help for the times series hyperparameters understanding
https://towardsdatascience.com/understanding-the-hyperparameters-of-a-simple-time-series-model-631f26c46c9

## Manually grid search (EXAMPLE):
```python
# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

arnings.filterwarnings("ignore") # specify to ignore warning messages

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue
            
Output
SARIMAX(0, 0, 0)x(0, 0, 1, 12) - AIC:6787.3436240402125
SARIMAX(0, 0, 0)x(0, 1, 1, 12) - AIC:1596.711172764114
SARIMAX(0, 0, 0)x(1, 0, 0, 12) - AIC:1058.9388921320026
SARIMAX(0, 0, 0)x(1, 0, 1, 12) - AIC:1056.2878315690562
SARIMAX(0, 0, 0)x(1, 1, 0, 12) - AIC:1361.6578978064144
SARIMAX(0, 0, 0)x(1, 1, 1, 12) - AIC:1044.7647912940095
...
...
...
SARIMAX(1, 1, 1)x(1, 0, 0, 12) - AIC:576.8647112294245
SARIMAX(1, 1, 1)x(1, 0, 1, 12) - AIC:327.9049123596742
SARIMAX(1, 1, 1)x(1, 1, 0, 12) - AIC:444.12436865161305
SARIMAX(1, 1, 1)x(1, 1, 1, 12) - AIC:277.7801413828764 
```
**The output of our code suggests that SARIMAX(1, 1, 1)x(1, 1, 1, 12) yields the lowest AIC value of 277.78. We should therefore consider this to be optimal option out of all the models we have considered.**

## Best way to approach hyperparameters:
Gridsearch -> https://github.com/chirlas24/snippets/blob/master/machine_learning.md
