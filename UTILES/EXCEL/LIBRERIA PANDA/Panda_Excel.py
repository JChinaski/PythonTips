
#crea y escribe un excel - Depende de libreria Panda
#pip install pandas

import pandas as pd
from pandas import ExcelWriter


df = pd.DataFrame({'Id': [1, 3, 2, 4],
                   'Nombre': ['Juan', 'Poto', 'María', 'Pablo'],
                   'Apellido': ['Méndez', 'López', 'Tito', 'Hernández']})
df = df[['Id', 'Nombre', 'Apellido']]
writer = ExcelWriter('EJ_EXCEL_CON_PANDA.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()



