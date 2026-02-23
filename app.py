import streamlit as st

st.sidebar.title("Menú")
opcion = st.sidebar.selectbox(
    "Selecciona una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if opcion == "Home":
    st.title("Proyecto Módulo 1 – Fundamentos de Python")
    st.write("Nombre del estudiante: TU NOMBRE AQUÍ")
    st.write("Curso: Especialización Python for Analytics - Módulo 1")
    st.write("Año: 2026")
    st.write("Objetivo: Desarrollar una app en Streamlit usando conceptos básicos de Python.")
    st.write("Tecnologías: Python, Streamlit")

elif opcion == "Ejercicio 1":
    st.title("Ejercicio 1 – Presupuesto")
    st.image("Presupuesto.png", width=250)

    presupuesto = st.number_input("Ingresa tu presupuesto:", min_value=0.0)
    gasto = st.number_input("Ingresa tu gasto:", min_value=0.0)

    st.latex(r"Diferencia = Presupuesto - Gasto")

    if st.button("Evaluar"):
        diferencia = presupuesto - gasto
        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto")
        else:
            st.warning("El gasto excede el presupuesto")

        st.write("Diferencia:", diferencia)

elif opcion == "Ejercicio 2":
    st.title("Ejercicio 2 – Registro de Actividades")
    st.image("financieras.png", width=250)

    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.text_input("Tipo de actividad")
    presupuesto = st.number_input("Presupuesto", min_value=0.0, key="p2")
    gasto_real = st.number_input("Gasto real", min_value=0.0, key="g2")

    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state.actividades.append(actividad)

    st.write("Lista de actividades:")
    st.write(st.session_state.actividades)

    for act in st.session_state.actividades:
        if act["gasto_real"] <= act["presupuesto"]:
            st.success(f"{act['nombre']} está dentro del presupuesto")
        else:
            st.warning(f"{act['nombre']} excede el presupuesto")

elif opcion == "Ejercicio 3":
    st.title("Ejercicio 3 – Retorno esperado")
    st.image("Retorno.png", width=250)

    st.latex(r"Retorno = Presupuesto \times Tasa \times Meses")

    if "actividades" not in st.session_state:
        st.warning("Primero registra actividades en el Ejercicio 2")
    else:
        tasa = st.number_input("Tasa (ejemplo: 0.05 para 5%)", min_value=0.0)
        meses = st.number_input("Meses", min_value=1, step=1)

        def calcular_retorno(actividad, tasa, meses):
            return actividad["presupuesto"] * tasa * meses

        if st.button("Calcular retorno"):
            retornos = list(map(lambda act: calcular_retorno(act, tasa, meses), st.session_state.actividades))
            for i, retorno in enumerate(retornos):
                st.write(f"Retorno de {st.session_state.actividades[i]['nombre']}: {retorno}")

elif opcion == "Ejercicio 4":
    st.title("Ejercicio 4 – Programación Orientada a Objetos")
    st.image("actividad.png", width=250)

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return f"Actividad: {self.nombre}, Tipo: {self.tipo}, Presupuesto: {self.presupuesto}, Gasto: {self.gasto_real}"

    if "actividades" not in st.session_state:
        st.warning("Primero registra actividades en el Ejercicio 2")
    else:
        objetos = []
        for act in st.session_state.actividades:
            obj = Actividad(act["nombre"], act["tipo"], act["presupuesto"], act["gasto_real"])
            objetos.append(obj)

        for obj in objetos:
            st.write(obj.mostrar_info())
            if obj.esta_en_presupuesto():
                st.success("Está dentro del presupuesto")
            else:
                st.warning("Excede el presupuesto")