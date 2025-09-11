# 🏡 Análisis de Datos de Airbnb

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre un dataset abierto de **Airbnb** utilizando **Python**.  
El flujo incluye **limpieza de datos** y **visualización** para identificar patrones de precios, distribución geográfica de alojamientos y detección de outliers.

---

## 📊 Análisis Ejecutivo
El análisis busca responder preguntas clave:
- ¿Cómo varían los precios según el tipo de habitación y el barrio?
- ¿Existen patrones entre precios, número de reseñas y verificación del host?
- ¿Qué zonas concentran alojamientos más caros?
- ¿Hay outliers que distorsionen la visión general del mercado?

---

## 📌 Conclusiones Generales
- Los **departamentos completos** presentan precios más altos, mientras que las **habitaciones privadas** son la opción más accesible.  
- Existen **diferencias de precio significativas entre barrios**.  
- Se detectaron **outliers en precios**, que afectan la media y deben filtrarse para modelos más robustos.  
- La **verificación de anfitrión** muestra relación con el precio, aunque no siempre es determinante.  
- Los mapas revelan la **segmentación geográfica** de alojamientos económicos vs premium.  

---

## 🔧 Trabajo Realizado
1. **Limpieza de datos** (`limpieza_airbnb.py`):
   - Eliminación de columnas irrelevantes.
   - Tratamiento de valores nulos y duplicados.
   - Conversión de variables (ej. `price` a numérico).
   - Exportación de un dataset limpio (`Airbnb_Limpio.csv`).

2. **Análisis EDA** (`analisis_eda_airbnb.py`):
   - Distribución de precios por tipo de habitación.
   - Precio promedio por barrio (ordenado).
   - Relación entre precio, número de reviews y políticas de cancelación.
   - Detección y visualización de outliers (Z-Score y MAD).
   - Mapas de calor de correlación.
   - Visualización geográfica de precios con latitud/longitud.

---

## 📈 Business Case
A partir del análisis:
- Se recomienda **segmentar estrategias de precios** por barrio y tipo de alojamiento.  
- Se debe **controlar y filtrar outliers** para obtener estadísticas confiables.  
- Incentivar la **verificación de anfitriones** podría generar confianza en los usuarios.  
- Zonas con alta concentración de alojamientos premium muestran **potencial de diferenciación de mercado**.  

---

## 🚀 Cómo ejecutar
1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/airbnb-analysis.git
   cd airbnb-analysis

---

## 📌 Autor
Proyecto realizado por *AnVales* como práctica de **Análisis de Datos**.
