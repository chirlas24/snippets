# Altair Visualization Snippets

## Web And Documentation
https://altair-viz.github.io/index.html

### Times series with filter of times series with bar chart for month and dinamic and filtered bar chart 
```python
width = 1200
height = 300
alt.data_transformers.disable_max_rows()

scheme = alt.Scale(scheme='tableau10')

brush = alt.selection(type="interval", encodings=["x"])
brush1 = alt.selection(type="interval", encodings=["x"])

t = alt.Chart(vta_plot).mark_line(point=True).encode(
    x=alt.X('Fecha:T'),
    y=alt.Y('valor:Q', title='Venta Terminada', axis=alt.Axis(grid=True)),
    color = alt.Color('tipo dato',
                      scale=scheme,
                      legend=alt.Legend(title='Leyenda',
                                        orient="top",
                                        direction="horizontal",
                                        labelFont='Calibri',
                                        labelFontSize=12,
                                        titleFont='Calibri',
                                        titleFontSize=15,
                                        titleFontWeight=900)),
    tooltip=['Fecha:T','tipo dato','valor:Q']
).properties(width=width,
             height=height,
             title = "Serie completa de Venta Terminada para filtrado en grafico inferior"
).add_selection(brush)

t2 = alt.Chart(vta_plot).mark_line(point=True).encode(
    x=alt.X('Fecha:T'),
    y=alt.Y('valor:Q', title='Venta Terminada', axis=alt.Axis(grid=True)),
    color = alt.Color('tipo dato',
                      scale=scheme,
                      legend=None),
    tooltip=['Fecha:T','tipo dato','valor:Q']
).properties(width=width,
            height=height,
            title = "Serie de Venta Terminada en periodo seleccionado"
).transform_filter(brush
).add_selection(brush1)


bar_m = alt.Chart(vta_plot).mark_bar(opacity=0.3).encode(
    x=alt.X('yearmonth(month):O', title='Mes y Año'),
    y=alt.Y('sum(valor):Q', title='Venta Terminada', stack=None),
    color = alt.Color('tipo dato',
                      scale=scheme,
                      legend=None)
).transform_timeunit(month='yearmonth(Fecha)'
).properties(width=width/2,
             height=height,
             title = "Acumulado por MES"
)

bar_w = alt.Chart(vta_plot).mark_bar(opacity=0.3,
                                     size=50).encode(
    x=alt.X('day(month):O', title='Dia Semana'),
    y=alt.Y('mean(valor):Q', title='Venta Terminada', stack=None),
    color = alt.Color('tipo dato',
                      scale=scheme,
                      legend=None)
).transform_timeunit(month='day(Fecha)'
).transform_filter(brush1
).properties(width=width/2,
             height=height,
             title = "Media por DIA SEMANA en periodo seleccionado"
)

source_ticks = vta_plot[vta_plot['tipo dato'] == 'Real']
source_ticks['leyenda'] = 'Valor medio por dia'

ticks_mean = alt.Chart(source_ticks).mark_tick(
    opacity=0.7,
    thickness=3,
    size=50
).encode(
    x=alt.X('day(Fecha):O', title='Dia Semana'),
    y=alt.Y('mean(valor):Q'),
    color = alt.Color('leyenda',
                      scale=alt.Scale(scheme='set1'),
                      legend=alt.Legend(title=None,
                                        orient='top-left')))

bar_week = (bar_w + ticks_mean).properties(resolve=alt.Resolve(scale=alt.LegendResolveMap(color=alt.ResolveMode("independent"))))
   
final_1 = (t | bar_m).properties(title="Centro de Analitica Avanzada en Retail (C.A.A.R.) - BigData Analytics") 
           
final = (final_1 & (t2 | bar_week)).properties(title = "DASHBOARD - Estimacion Venta Terminada - EL CORTE INGLES",
                                                   resolve=alt.Resolve(scale=alt.LegendResolveMap(color=alt.ResolveMode("independent")))
).configure_title(
    fontSize=15,
    font='Calibri',
    anchor='middle',
    color='black'
)

final
```

