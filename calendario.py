import calendar #importa 
from pathlib import Path

#CREATE MULTIPLE FOLDERS

month_year = list(calendar.month_name[1:])
day_week = ['Dia 1', 'Dia 10', 'Dia 20', 'Dia 30']#array con los dias de la semana

for i, month in enumerate(month_year):
    for day in day_week:
        Path(f'2024/{i+1}.{month}/{day}').mkdir(parents=True, exist_ok=True) #mkdir crea un nuevo direcctorio
        #2024es el nombre de la carpeta principal