from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, count
from pyspark.sql.types import IntegerType

# 1. Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("Pipeline de Data Engineering con Spark") \
    .getOrCreate()

# 2. Cargar un archivo CSV
df = spark.read.csv("data/empleados.csv", header=True, inferSchema=True)

# 3. Mostrar el esquema del DataFrame
print("Esquema del DataFrame:")
df.printSchema()

# 4. Manejo de valores nulos
# Reemplazar nulos en la columna 'Edad' con la media
media_edad = df.select(avg(col("Edad"))).first()[0]
df = df.withColumn("Edad", when(col("Edad").isNull(), media_edad).otherwise(col("Edad")))

# Reemplazar valores nulos en la columna 'Salario' con 0
df = df.fillna({'Salario': 0})

# 5. Convertir la columna 'Edad' a IntegerType
df = df.withColumn("Edad", col("Edad").cast(IntegerType()))

# 6. Filtrar los datos (ejemplo: empleados con salario mayor a 50,000)
print("Empleados con salario mayor a 50,000:")
df.filter(col("Salario") > 50000).show()

# 7. Añadir una nueva columna (ejemplo: clasificar el rango de salario)
print("Añadir columna 'Rango Salarial':")
df = df.withColumn("Rango Salarial", 
                   when(col("Salario") < 30000, "Bajo")
                   .when((col("Salario") >= 30000) & (col("Salario") < 70000), "Medio")
                   .otherwise("Alto"))

df.show()

# 8. Agrupar datos (ejemplo: contar empleados por departamento)
print("Conteo de empleados por departamento:")
df.groupBy("Departamento").agg(count("*").alias("Número de empleados")).show()

# 9. Ordenar por salario en orden descendente
print("Ordenar empleados por salario (descendente):")
df.orderBy(col("Salario").desc()).show()

# 10. Guardar el DataFrame transformado en formato Parquet
df.write.parquet("data/empleados_transformados.parquet", mode="overwrite")

# 11. Parar la sesión de Spark
spark.stop()
