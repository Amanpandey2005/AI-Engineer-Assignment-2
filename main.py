import pandas as pd
import os
from scraper import Scraper
from processor import DataProcessor
from llmservice import LLMService

def main():
    # Make sure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    url = input("Enter Product URL: ")
    # Initialize modules
    scraper = Scraper()
    processor = DataProcessor()
    llm = LLMService()

    # 1. Scrape
    print("Fetching reviews...")
    raw_reviews = scraper.fetch_reviews(url)

    if not raw_reviews:
        print("No reviews found. Check your URL or scraper selectors.")
        return

    # 2. Process & Analyze
    processed_data = []
    for review in raw_reviews:
        cleaned = processor.clean_text(review['text'])
        # Use the first chunk for analysis
        chunks = processor.chunk_text(cleaned)
        chunk = chunks[0] if chunks else ""
        
        if chunk:
            print(f"Analyzing review by {review['author']}...")
            review['analysis'] = llm.analyze_sentiment(chunk)
            processed_data.append(review)

    # 3. Store Results
    df = pd.DataFrame(processed_data)
    output_path = os.path.join("data", "processed_reviews.csv")
    df.to_csv(output_path, index=False)
    print(f"Success! Data saved to {output_path}")

if __name__ == "__main__":
    main()