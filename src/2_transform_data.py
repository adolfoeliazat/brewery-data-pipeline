from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def transform_data(input_path="/app/bronze/raw_breweries.json", output_path="/app/silver/breweries.parquet"):
    spark = SparkSession.builder.appName("BreweryDataTransformation").getOrCreate()
    
    df = spark.read.json(input_path)
    transformed_df = df.select("id", "name", "brewery_type", "city", "state") \
                       .withColumnRenamed("state", "location") \
                       .withColumn("location", col("location").cast("string"))

    transformed_df.write.partitionBy("location").parquet(output_path)
    print(f"Transformed data saved at {output_path}")
