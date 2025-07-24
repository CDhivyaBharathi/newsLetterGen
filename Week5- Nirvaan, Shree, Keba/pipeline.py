#keba
import requests
from textblob import TextBlob

def fetch_news(ticker): #ticker - the company's name
    """
    Fetches the 5 most recent news articles about the given keyword (ticker).
    Returns a list of dictionaries with 'title' and 'summary'.
    """
    api_key = '75a092aeecb34c0dbdcb7216919b4bff'  
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': ticker,
        'sortBy': 'publishedAt',
        'pageSize': 5,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return [{"title": a.get("title", ""), "summary": a.get("description", "")} for a in articles[:5]]

#samir
# Step 1: Import the TextBlob library



def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using TextBlob.

    Args:
        text (str): The text to analyze

    Returns:
        str: "Positive", "Negative", or "Neutral"
    """

    # Step 2: Create a TextBlob object from the input text
    # TextBlob will process the text and prepare it for analysis
    blob = TextBlob(text)

    # Step 3: Get the polarity score
    # The polarity property returns a float between -1 and 1
    polarity = blob.sentiment.polarity

    # Step 4: Classify the sentiment based on polarity thresholds
    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"
   

#amir
def detect_signal(price_change, sentiment):
    # If the price went up more than 2% AND the sentiment is Positive
    if price_change > 2 and sentiment == "Positive":
        return "Buy Signal"

    # If the price dropped more than 2% AND the sentiment is Negative
    elif price_change < -2 and sentiment == "Negative":
        return "Sell Signal"

    # For everything else, just Hold
    else:
        return "Hold"
    

#nirvaan
def generate_newsletter(news_list, signals):
    newsletter = "*** Daily Financial Newsletter ***\n\n"

    # Add news section
    newsletter += "Top News Headlines:\n"
    for i, news_item in enumerate(news_list, start=1):
        newsletter += f"{i}. {news_item['title']}\n"
        newsletter += f"   {news_item['summary']}\n\n"

    # Add trading signals section
    newsletter += "Trading Signals:\n"
    for signal in signals:
        newsletter += f"- {signal}\n"

    return newsletter


#shree
def run_pipeline(ticker: str, price_change: float) -> str:
    # Step 1: Fetch news articles for the given ticker
    news_articles = fetch_news(ticker)

    # Step 2: Analyze sentiment for each news article title
    sentiments = []
    for article in news_articles:
        sentiment = analyze_sentiment(article["title"])
        sentiments.append(sentiment)

    # Step 3: Generate trading signals based on price change and sentiment
    signals = []
    for sentiment in sentiments:
        signal = detect_signal(price_change, sentiment)
        signals.append(signal)

    # Step 4: Generate the newsletter using the news articles and signals
    newsletter = generate_newsletter(news_articles, signals)

    # Step 5: Print and return the newsletter
    print(newsletter)
    return newsletter

if __name__ == "__main__":
    run_pipeline("TCS", 2.5)