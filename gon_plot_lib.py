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
