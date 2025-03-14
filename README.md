```md
# 📊 Stock Market Reddit Sentiment Analysis  

## 🚀 Project Overview  
This project analyzes sentiment from Reddit discussions about the stock market, extracting insights from user comments on the **r/StockMarket** subreddit. Using NLP-based sentiment analysis, it identifies whether discussions are **positive, negative, or neutral** and visualizes sentiment trends.  

## 📂 Dataset  
### ✅ Reddit Data:  
- **Source:** Reddit API (PRAW)  
- **Data Collected:**  
  - Top 10 trending posts from r/StockMarket  
  - Comments from the most upvoted post  
  - Sentiment Scores (Positive, Neutral, Negative)  

## 📊 Key Insights  
- **Negative sentiment increases** during market dips  
- **Bullish discussions** often indicate upcoming stock rallies  
- **Common words in negative sentiment:** “crash,” “sell,” “loss”  
- **Positive sentiment is frequent in AI, Tech, and EV stocks discussions**  

## 🔍 Visualizations  

### 📌 Sentiment Distribution  
![Sentiment Bar Chart](sentiment_bar_chart.png)  

### 📌 Sentiment Pie Chart  
![Sentiment Pie](sentiment_pie_chart.png)  

### 📌 Word Cloud of Frequent Stock Discussion Words  
![Word Cloud](wordcloud.png)  

### 📌 Sentiment Score Trend Over Comments  
![Sentiment Trend](sentiment_trend.png)  

### 📌 Comment Length vs Sentiment  
![Scatter Plot](comment_length_vs_sentiment.png)  

## 📌 Technologies Used  
- **Python** (Pandas, Matplotlib, Seaborn, NLTK, WordCloud)  
- **Reddit API (PRAW)**  
- **NLTK (VADER) for sentiment analysis**  
- **Jupyter Notebook / PyCharm**  
- **Git & GitHub for Version Control**  

## 💻 How to Run  

### 1️⃣ Clone the repository  
```sh
git clone https://github.com/your-username/Reddit-StockMarket-Sentiment.git
```

### 2️⃣ Install dependencies  
```sh
pip install praw pandas matplotlib seaborn nltk wordcloud
```

### 3️⃣ Configure Reddit API Credentials  
Update the script with your **client ID** and **secret key**:  
```python
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="your_user_agent",
    username="your_username"
)
```

### 4️⃣ Run the script  
```sh
python reddit_stock_sentiment.py
```

### 5️⃣ View Saved Plots  
All visualizations are saved as **.png** files in the project folder.  

## 📌 Potential Improvements  
✅ Expand to multiple subreddits (r/Investing, r/WallStreetBets)  
✅ Combine with live stock price data for deeper insights  
✅ Implement AI models (LSTM, BERT) for more accurate sentiment prediction  

## 📢 Contact  
💼 **Author:** Charan Kumar G  
📩 **Email:** [charankumar.career@gmail.com](mailto:charankumar.career@gmail.com)  
🔗 **LinkedIn:** [linkedin.com/in/charankumar-g](https://www.linkedin.com/in/charankumar-g)  

⭐ If you found this project useful, please give it a star! ⭐  
```
