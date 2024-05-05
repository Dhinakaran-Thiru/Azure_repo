# Databricks notebook source
# MAGIC %run ./utils

# COMMAND ----------

raw_sales_df = spark.read.csv('dbfs:/mnt/Bronze/salesview/sales/20240105_sales_data.csv', header=True, inferSchema=True)

# COMMAND ----------

renamed_sales_df = toSnakeCase(raw_sales_df)

# COMMAND ----------

writeTo = f'dbfs:/mnt/Silver/sales_view/sales'
write_delta_upsert(renamed_sales_df, writeTo)

# COMMAND ----------

