from pyspark.sql import SparkSession

def aggregate_data(input_path="/app/silver/breweries.parquet", output_path="/app/gold/aggregated_breweries.parquet"):
    spark = SparkSession.builder.appName("BreweryDataAggregation").getOrCreate()

    df = spark.read.parquet(input_path)

    # Agregação por tipo e localização
    aggregated_df = df.groupby(['state', 'brewery_type']).size().reset_index(name='brewery_count')
    
    aggregated_df.write.parquet(output_path)
    print(f"Aggregated data saved at {output_path}")
