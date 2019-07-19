## Quitar warnings

 ```python
import warnings
warnings.filterwarnings("ignore")
```

## Ampliar notebook ancho pantalla
 ```python
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
```

## Mostrar todo el dataframe en PANDAS
 ```python
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
```

## Elegir formato de salida en dataframe en PANDAS
 ```python
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.3f' % x)
```
