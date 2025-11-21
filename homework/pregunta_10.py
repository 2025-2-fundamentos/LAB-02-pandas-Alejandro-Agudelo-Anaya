import pandas as pd
from pathlib import Path

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.
    """
    
    # Define la ruta relativa al archivo. 
    # **Asegúrate de que esta ruta sea la correcta para tu entorno de prueba.**
    filepath = Path("files/input/tbl0.tsv")
    
    # 1. Leer el archivo tbl0.tsv
    df = pd.read_csv(filepath, sep="\t")

    # 2. Agrupar por 'c1', ordenar los valores de 'c2' y unirlos con ':'
    # .apply(lambda x: ':'.join(map(str, sorted(x)))) genera una Serie.
    resultado_series = df.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x))))
    
    df_resultado = resultado_series.to_frame(name='c2')
    
    df_resultado = df_resultado.rename_axis('_c1')

    return df_resultado
