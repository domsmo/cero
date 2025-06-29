import pandas as pd
import json
from datetime import date, datetime, timedelta

today = date.today()

def read_file(file_name):
    with open(file_name, 'r') as f:
        datos = json.load(f)
    return datos


def filtro_dias(reglas, citas):
    filtro = []
    dias_antes = [regla['dias_antes'] for regla in reglas if regla['dias_antes'] is not None]
    for dia in dias_antes:
        for cita in citas:
            if datetime.strptime(cita['fecha_cita'], "%Y-%m-%d") == datetime.strptime(str(today + timedelta(days=dia)), "%Y-%m-%d"):
                filtro.append(cita['id_cita'])
    filtro = set(filtro)
    return [citas_filtradas for citas_filtradas in citas if citas_filtradas['id_cita'] in filtro]


def edad_paciente(citas):
    for cita in citas:
        edad = cita['edad_paciente']
        if edad >=60:
            cita['grupo_etario'] = "tercera edad"
        elif edad < 60 and edad >= 18:
            cita['grupo_etario'] = "adulto"
        else:
            cita['grupo_etario'] = "niño"
    return citas

def filtrado_citas (reglas, citas):
    citas_filtradas = []
    for cita in edad_paciente(citas):
        for regla in reglas:
            if regla['condiciones']:
                for clave, valor in regla['condiciones'].items():
                    if clave not in cita or cita[clave] != valor:
                        continue
                    else:
                        if regla['exclusiones']:
                            for clave, valor in regla['exclusiones'].items():
                                if clave in cita and cita[clave] == valor:
                                    continue
                                else:
                                    citas_filtradas.append(cita)  
                            break
                else:
                    if regla['exclusiones']:
                        for clave, valor in regla['exclusiones'].items():
                            if clave in cita and cita[clave] == valor:
                                break
    return citas_filtradas


data = read_file("citas_simuladas.json")
reglas = read_file("reglas.json")
hoy = filtro_dias(reglas, data)

listado_final = filtrado_citas(reglas, edad_paciente(data))

