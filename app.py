import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel der Streamlit-App
st.title("Datensatz-Visualisierung")

# Eingabefeld für die URL des Datensatzes
st.info("Der Datensatz muss im CSV-Format vorliegen und mit einem Semikolon (;) getrennt sein. (https://www.web.statistik.zh.ch/awel/LoRa/data/AWEL_Sensors_LoRa_202303.csv)")
url = st.text_input("Geben Sie die URL des Datensatzes ein:")

# Eingabefelder für die Spaltennamen, die in der Grafik angezeigt werden sollen
st.info("z.B. starttime")
x_axis = st.text_input("Geben Sie den Namen der Spalte für die X-Achse ein:")
st.info("z.B. humidity")
y_axis = st.text_input("Geben Sie den Namen der Spalte für die Y-Achse ein:")

# Schaltfläche, um den Datensatz herunterzuladen und die Grafik anzuzeigen
if st.button("Lade Daten und zeige Grafik"):
    if url:
        try:
            # Laden des Datensatzes
            data = pd.read_csv(url, sep=";")
            st.write(data.head())

            # Grafik erstellen und anzeigen
            fig, ax = plt.subplots()
            ax.scatter(data[x_axis], data[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Fehler beim Laden des Datensatzes: {e}")
    else:
        st.warning("Bitte geben Sie eine gültige URL ein.")
