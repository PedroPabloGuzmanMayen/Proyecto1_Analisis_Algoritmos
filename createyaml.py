import json
import yaml
from collections import OrderedDict

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Carga el JSON como un diccionario
            return data
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except json.JSONDecodeError:
        print("Error: El archivo no es un JSON válido.")
    return None

def convert_transitions_to_yaml(transitions, output_file):
    yaml_transitions = []
    for state, symbols in transitions.items():
        for symbol, (next_state, write_symbol, direction) in symbols.items():
            transition = OrderedDict([
                ("params", OrderedDict([
                    ("initial_state", state),
                    ("mem_cache_value", ""),
                    ("tape_input", symbol)
                ])),
                ("output", OrderedDict([
                    ("final_state", next_state),
                    ("mem_cache_value", ""),
                    ("tape_output", write_symbol),
                    ("tape_displacement", "R" if direction == 1 else "L")
                ]))
            ])
            yaml_transitions.append(transition)

    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.dump(yaml_transitions, file, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"Archivo YAML guardado en {output_file}")

if __name__ == "__main__":
    file_path = "configuration.json"  # Cambia esto por la ruta de tu archivo JSON
    output_yaml = "turing_machine.yaml"  # Ruta para el archivo YAML
    data = read_json(file_path)
    
    if data:
        print("Estados (Q):", data.get("Q", []))
        print("Alfabeto de entrada (Σ):", data.get("Σ", []))
        print("Alfabeto de cinta (Γ):", data.get("Γ", []))
        print("Estado inicial (S):", data.get("S", []))
        print("Símbolo en blanco (b):", data.get("b", []))
        print("Estados finales (F):", data.get("F", []))
        
        convert_transitions_to_yaml(data.get("transitions", {}), output_yaml)
