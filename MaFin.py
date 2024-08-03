import streamlit as st

def calcular_pagos_con_interes(monto_total, semanas, tasa_interes_anual):
    # Convertir la tasa de interés anual a una tasa efectiva semanal
    tasa_interes_semanal = (1 + tasa_interes_anual) ** (1 / 52) - 1
    
    # Calcular el monto total con interés compuesto semanal
    monto_con_interes = monto_total * (1 + tasa_interes_semanal) ** semanas
    
    # Calcular el pago semanal base
    pago_semanal = monto_con_interes // semanas
    pagos = [pago_semanal] * semanas

    # Calcular el residuo y distribuirlo
    residuo = monto_con_interes % semanas
    for i in range(int(residuo)):
        pagos[i] += 1

    return pagos

def main():
    st.title("Calculadora MaFin")
    
    monto_total = st.number_input("Monto Total", min_value=0.0, value=1000.0, step=100.0)
    semanas = st.number_input("Número de Semanas", min_value=1, value=7, step=1)
    tasa_interes_anual = st.number_input("Tasa de Interés Anual (%)", min_value=0.0, value=10.4, step=0.1) / 100

    if st.button("Calcular"):
        pagos = calcular_pagos_con_interes(monto_total, semanas, tasa_interes_anual)
        st.subheader("Pagos Semanales")
        for i, pago in enumerate(pagos, start=1):
            st.write(f"Pago {i}: {pago:.2f}")

if __name__ == "__main__":
    main()
