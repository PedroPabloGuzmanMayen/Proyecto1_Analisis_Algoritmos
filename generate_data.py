import yaml
import csv
from reader import Reader
from TM import TuringMachine
from convexion import *


def generar_data():
    yaml_path = "maquina_alteradora.yaml"
    
    with open(yaml_path, "r", encoding="utf-8") as file:
        content = yaml.safe_load(file)
    lector = Reader(content=content)
    
   
    with open("resultados.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Numero",  "Tiempo"])  # Encabezados
        
        for i in range(0, 25):
            maquina = TuringMachine(lector=lector)
            user_input = encode1s(i)
            maquina.procesar(user_input)
            maquina.procesar(user_input)
           
            tiempo = maquina.tiempo_segundos
            
            # Escribir en CSV
            writer.writerow([i,tiempo])
            
            print(f"Numero \"{i}\" |  \"{tiempo}\" seg")


if __name__ == "__main__":
    generar_data()
