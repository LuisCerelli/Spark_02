### Pipeline de Data Engineering con PySpark

---

## Descripción

Este proyecto consiste en la implementación de un pipeline de procesamiento de datos utilizando PySpark, una herramienta clave en el ecosistema Big Data. El pipeline tiene como objetivo la limpieza, transformación y análisis de datos provenientes de un archivo CSV con información de empleados. El proceso involucra desde la carga de los datos hasta su procesamiento y almacenamiento en un formato optimizado (Parquet).

## Funcionalidades

El script realiza las siguientes operaciones:

1. **Carga de datos**: Se importa un archivo CSV con los datos de empleados. El archivo debe contener información relevante como el nombre, edad, salario, y departamento de cada empleado.
   
2. **Exploración de datos**: Se visualiza la estructura del DataFrame para comprender los tipos de datos de cada columna, lo que permite un mejor entendimiento del dataset.

3. **Limpieza de datos**:
   - Se manejan los valores nulos en las columnas más importantes:
     - La columna "Edad" reemplaza los valores nulos por la media de las edades.
     - La columna "Salario" reemplaza los valores nulos con un valor predeterminado de 0.

4. **Transformaciones**:
   - Se realiza una conversión de tipos, asegurando que la columna "Edad" sea del tipo `Integer`.
   - Se filtran los empleados que tienen un salario superior a 50,000.
   - Se agrega una nueva columna que clasifica el rango salarial en "Bajo", "Medio" o "Alto", basado en valores predefinidos.

5. **Análisis de datos**:
   - Se agrupan los empleados por departamento para contar cuántos empleados hay en cada uno.
   - Se ordena la información de los empleados por su salario de mayor a menor.

6. **Almacenamiento**: Una vez transformados y procesados, los datos se almacenan en formato Parquet, que es eficiente para grandes volúmenes de información.

## Ejemplo de uso

El código puede aplicarse en un contexto donde se necesiten realizar análisis sobre grandes volúmenes de datos de empleados, como:

- Identificar a los empleados con los salarios más altos dentro de la empresa.
- Clasificar los salarios de los empleados en rangos para realizar estudios o políticas de compensación.
- Contar el número de empleados por departamento, facilitando el análisis de recursos humanos.

Por ejemplo, en una empresa multinacional con miles de empleados, el uso de este código permitiría obtener estadísticas clave para la toma de decisiones sobre remuneraciones, promociones y asignación de personal.

## Requisitos

- Tener instalado **PySpark** y un entorno de Python 3. 
- El archivo CSV debe estar ubicado en la ruta `data/empleados.csv` o cambiar la ruta en el código según corresponda.
- Spark debe estar configurado adecuadamente en el entorno donde se ejecutará el script.

## **Utilidad para la ingeniería de datos**

**Este código es altamente útil en el contexto de la ingeniería de datos, ya que permite automatizar procesos de transformación de datos de una manera escalable y eficiente.** Al emplear PySpark, es posible manejar grandes volúmenes de información que no podrían ser procesados con herramientas tradicionales debido a limitaciones de memoria. Además, el uso de formatos como Parquet facilita la integración con otros sistemas Big Data y garantiza un rendimiento óptimo en las consultas posteriores.

En el día a día de un Data Engineer, este pipeline sería esencial para procesar datos crudos de manera eficiente, asegurando que los datos estén limpios y estructurados para análisis más profundos o modelos de Machine Learning. Además, al ser capaz de manejar errores comunes como los valores nulos y realizar transformaciones de datos en paralelo, permite que las operaciones se realicen en tiempos mucho más rápidos que con métodos tradicionales.

## Consideraciones

- Asegúrate de que los datos en el archivo CSV estén correctamente formateados para evitar problemas al momento de la carga del archivo.
- La columna "Edad" debe contener valores numéricos para que la media pueda calcularse correctamente.
- Este código está diseñado para datasets de tamaño considerable, pero su ejecución podría requerir un entorno distribuido en caso de manejar millones de registros.
  
## Licencia

Este proyecto está bajo la licencia MIT.
