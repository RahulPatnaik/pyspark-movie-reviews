# pyspark-movie-reviews

Basic PySpark processing of the IMDb 50K Movie Review dataset (Homework 1.2).

## Dataset

[IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) (Kaggle). Download `IMDB Dataset.csv` and place it in `data/`.

## Run

```bash
pip install -r requirements.txt
python pyspark_movie_reviews.py
```

## Steps

1. Load the CSV into a DataFrame
2. Print the schema and the first 5 rows
3. Remove rows with null or empty reviews
4. Count all reviews, and positive vs negative reviews
5. Add a `review_length` column and show reviews longer than 500 characters
6. Save the result as CSV in `output/cleaned_reviews/`

## Results

| | Count |
|---|---|
| Reviews loaded | 50,000 |
| After cleaning | 50,000 |
| Positive | 25,000 |
| Negative | 25,000 |
| Longer than 500 characters | 45,017 |
