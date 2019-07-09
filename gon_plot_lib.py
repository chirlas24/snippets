############################ 
#        LIBRARIES
############################

import altair as alt
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

alt.renderers.enable('notebook')
alt.data_transformers.disable_max_rows()

############################ 
#        TIMES SERIES
############################

def plot_simple_times_series(df_entry, col_values=None, width=800, height=150):
    '''Pintado de la serie temporal para su estudio'''
    df = df_entry.copy()

    #Comprobacion de las columnas y datos
    if col_values not in df.columns:
        raise Exception('La columna %s no se encuentra en el dataframe' % col_values) 
    elif not isinstance(output.index.dtype.type(), np.datetime64):
        raise Exception('El indice no es del tipo DateTime') 
    elif not isinstance(output['y'].dtype.type(), np.number):
        raise Exception('La columna %s no es del tipo numero'  % col_values)
        
    #Creamos columna para el pintado
    df['Fecha'] = df.index
    df.reset_index(inplace=True, drop=True)
         
    #Filtrado de las serie para el zoom
    brush = alt.selection(type="interval", encodings=["x"])
    
    main_times_series_plot = alt.Chart(df).mark_line(point=False,
                                                     opacity=1
    ).encode(
        x=alt.X('Fecha:T'),
        y=alt.Y(col_values + ':Q', title=col_values, axis=alt.Axis(grid=True))
    ).properties(width=width,
                 height=height,
                 title='Serie completa para el filtrado'
    ).add_selection(brush)
    
    second_times_series_plot = alt.Chart(df).mark_line(point=True,
                                                     opacity=1
    ).encode(
        x=alt.X('Fecha:T'),
        y=alt.Y(col_values + ':Q', title=col_values, axis=alt.Axis(grid=True)),
        tooltip=['Fecha:T', col_values + ':Q']
    ).properties(width=width,
                 height=height,
                 title='Serie ampliada'
    ).transform_filter(brush)
    
    return (main_times_series_plot & second_times_series_plot)

def plot_times_series_prediction(df_, prediciton_mean_, prediction_ci_=None, width=800, height=150):
    '''Dibuja la prediccion con el intervalo de confianza si es proporcionado
        df_ = dataframe con la serie temporal (fechas en el indice)
        prediciton_mean_ = Salida del modelo con la media de la prediccion (fechas en el indice)
        prediction_ci_ = Intercalos de confianza ('upper y' y 'lower y')(fechas en el indice)
        '''
    if prediction_ci_ is not None:
        prediction_ci = prediction_ci_.copy()
    prediciton_mean_ = prediciton_mean_.copy()
    df = df_.copy()
    
    #Creacion del data frame para pintado
    prediciton_mean_df = pd.DataFrame(prediciton_mean, columns=['prediction'])
    if prediction_ci_ is not None:
        prediction_ci_df = pd.DataFrame(prediction_ci)
        prediction_df = prediction_ci_df.merge(prediciton_mean_df, left_index=True, right_index=True )
    else:
        prediction_df = prediciton_mean_df
    
    df_plot = df.merge(prediction_df, left_index=True, right_index=True, how='outer')
    df_plot.reset_index(inplace=True, )
    df_plot = df_plot.melt(id_vars=['index'])
    df_plot.dropna(inplace=True)

    #Tema para el plot
    scheme = alt.Scale(scheme='tableau10')

    #Filtrado por barrido
    brush = alt.selection(type="interval", encodings=["x"])

    #Plot times series principal
    main_times_series_plot = alt.Chart(df_plot
                                    ).mark_line(point=False,
                                                     opacity=0.7
    ).encode(
        x=alt.X('index:T'),
        y=alt.Y('value:Q', axis=alt.Axis(grid=True)),
        color = alt.Color('variable',
                  scale=scheme,
                  legend=alt.Legend(title='Leyenda',
                                    symbolSize=30,
                                    symbolType='circle',
                                    symbolStrokeWidth=5,
                                    orient="top",
                                    direction="horizontal",
                                    labelFont='Calibri',
                                    labelFontSize=12,
                                    titleFont='Calibri',
                                    titleFontSize=15,
                                    titleFontWeight=900))

    ).properties(width=width,
                 height=height,
                 title='Serie completa para el filtrado'
    ).transform_filter(
        alt.FieldOneOfPredicate(field='variable', oneOf=['y', 'prediction'])
    )

    #Plot de la banda de confianza si hay
    if prediction_ci_ is not None:
        band = alt.Chart(df_plot).mark_errorband(extent='ci', color='red').encode(
            x=alt.X('index:T'),
            y=alt.Y('value:Q')
        ).transform_filter(
            alt.FieldOneOfPredicate(field='variable', oneOf=['lower y', 'upper y'])
        )
    
    
    #Plot del segundo grafico con tooltip y puntos
    second_times_series_plot = alt.Chart(df_plot
                                    ).mark_line(point=True,
                                                     opacity=0.7
    ).encode(
        x=alt.X('index:T'),
        y=alt.Y('value:Q', axis=alt.Axis(grid=True)),
        color = alt.Color('variable',
                  scale=scheme,
                  legend=alt.Legend(title='Leyenda',
                                    symbolSize=30,
                                    symbolType='circle',
                                    symbolStrokeWidth=5,
                                    orient="top",
                                    direction="horizontal",
                                    labelFont='Calibri',
                                    labelFontSize=12,
                                    titleFont='Calibri',
                                    titleFontSize=15,
                                    titleFontWeight=900)),
        tooltip=['index:T', 'value:Q', 'variable']

    ).properties(width=width,
                 height=height,
                 title='Serie ampliada'
    ).transform_filter(
        alt.FieldOneOfPredicate(field='variable', oneOf=['y', 'prediction'])
    )
    
    if prediction_ci_ is not None:
        t1 = band + main_times_series_plot.add_selection(brush)
        t2 = (band + second_times_series_plot).transform_filter(brush)
        return (t1 & t2)
    else:
        t1 = main_times_series_plot.add_selection(brush)
        t2 = (second_times_series_plot).transform_filter(brush)
        return (t1 & t2)
