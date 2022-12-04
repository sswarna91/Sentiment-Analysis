pip install -q transformers
from transformers import pipeline
sentiment_pipeline = pipeline("model=distilbert-base-uncased-finetuned-sst-2-english")
data = ["This product is awesome", "The product is not worth the price"]
sentiment_pipeline(data)
