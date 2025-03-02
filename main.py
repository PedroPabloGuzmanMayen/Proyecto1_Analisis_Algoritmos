import streamlit as st
import yaml
from reader import Reader
from TM import TuringMachine
from convexion import *
st.set_page_config(page_title="Fibonnacci Maquina de Turing", page_icon="🧠")
st.title('Maquina de Turing Fibonnaci')

with st.container():
    yaml_path = "maquina_alteradora.yaml"
    
    with open(yaml_path, "r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    st.write("Archivo cargado exitosamente:")
    try:
        lector = Reader(content=content)
        maquina = TuringMachine(lector=lector)
        st.subheader('Digrama de la Maquina de Turing')
        maquina.generar_grafico()
        st.image('./graficas/maquina_turing.png')
        
        # Input de texto y botón
        mynumber = st.number_input("Ingrese un número entero:", min_value=0, step=1, value=0)

        
        user_input = encode1s(mynumber)
        
        if st.button("Procesar cadena"):
            if user_input:
                result, historial, cinta = maquina.procesar(user_input)
                resultado = replaced(cinta)
                re = f"Del numero \"{mynumber}\" se obtuvo en la secuencia fibonnaci el numero: \"{resultado}\""
                st.subheader('Resultado cadena')
                if result == "aceptada":
                    st.success(re)
                
                pasos = ''
                pasos_show = ''
                for p in historial:
                    pasos += f'{p}<br>'
                    pasos_show += f'{p}\n'
                
                txt_content = (f"CONFIGURACIONES MAQUINA DE TURING\nCadena: {user_input}\n\n"
                               f"Estado: {result}\nCinta: {cinta}\nConfiguraciones:\n" + pasos_show)
                
                st.download_button(
                    label="Descargar archivo de configuraciones para esta cadena",
                    data=txt_content,
                    file_name=f"configuraciones_TM_cadena_{user_input}.txt",
                    mime="text/plain"
                )
                
                st.subheader('Configuraciones de la cinta')
                st.write(f"<span style='font-size:11px; font-style:italic;'>{pasos}</span>", unsafe_allow_html=True)
            else:
                st.warning("Por favor, ingrese una cadena antes de procesar.")
    
    except yaml.YAMLError as e:
        st.error(f"Error al leer el archivo YAML: {e}")
