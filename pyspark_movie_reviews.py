from pyspark.sql import SparkSession
from pyspark.sql import functions as F

DATA_PATH = "data/IMDB Dataset.csv"
OUTPUT_PATH = "output/cleaned_reviews"

spark = (
    SparkSession.builder.appName("pyspark-movie-reviews")
    .master("local[*]")
    .config("spark.ui.showConsoleProgress", "false")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

print("== 1. Load the dataset ==")
df = (
    spark.read
    .option("header", True)
    .option("multiLine", True)
    .option("quote", '"')
    .option("escape", '"')
    .csv(DATA_PATH)
)
print(f"Rows loaded: {df.count()}")

print("\n== 2. Explore the data ==")
df.printSchema()
df.show(5, truncate=80)

print("== 3. Clean the data ==")
clean_df = df.filter(F.col("review").isNotNull() & (F.trim(F.col("review")) != ""))
print(f"Rows before cleaning: {df.count()}")
print(f"Rows after cleaning:  {clean_df.count()}")

print("\n== 4. Analyze the data ==")
print(f"Total reviews: {clean_df.count()}")
clean_df.groupBy("sentiment").count().orderBy("sentiment").show()

print("== 5. Transform the data ==")
transformed_df = clean_df.withColumn("review_length", F.length("review"))
transformed_df.select("sentiment", "review_length").show(5)

long_df = transformed_df.filter(F.col("review_length") > 500)
print(f"Reviews longer than 500 characters: {long_df.count()}")
long_df.select("sentiment", "review_length", "review").show(5, truncate=80)

print("== 6. Save the results ==")
(
    transformed_df.coalesce(1).write.mode("overwrite")
    .option("header", True)
    .option("escape", '"')
    .csv(OUTPUT_PATH)
)
print(f"Saved cleaned and transformed data to {OUTPUT_PATH}/")

spark.stop()
