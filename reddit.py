import praw
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

nltk.download("vader_lexicon")

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Reddit API Credentials
reddit = praw.Reddit(
    client_id="MjcKgRkBTLTgJOsA5WGT5Q",
    client_secret="XpcHl3ZPWFDL3JxRIPvg4ocSldlh1A",
    user_agent="Scraper",
    username="Afraid-Activity-334"
)

# Choose subreddit
subreddit = reddit.subreddit("StockMarket")

# Fetch Top 10 Posts
posts_data = []
for post in subreddit.hot(limit=10):
    posts_data.append([post.title, post.score, post.url])

posts_df = pd.DataFrame(posts_data, columns=["Title", "Upvotes", "URL"])
print(posts_df)  # Display the top posts

# Fetch Comments from the Top Post
top_post = next(subreddit.hot(limit=1))
top_post.comments.replace_more(limit=0)  # Remove "More comments"

comments_data = []
print(f"\n📌 Post: {top_post.title}")
print("\n💬 Top Comments with Sentiment:")

for comment in top_post.comments[:10]:  # Analyze first 10 comments
    sentiment_score = sia.polarity_scores(comment.body)["compound"]
    sentiment = "Neutral"

    if sentiment_score > 0.05:
        sentiment = "Positive ✅"
    elif sentiment_score < -0.05:
        sentiment = "Negative ❌"

    print(f"- {comment.body} \n  Sentiment: {sentiment}\n")
    comments_data.append([comment.body, sentiment, sentiment_score, len(comment.body)])

# Save results in DataFrame
comments_df = pd.DataFrame(comments_data, columns=["Comment", "Sentiment", "Sentiment Score", "Comment Length"])
print(comments_df)

# Sentiment Count for Visualization
sentiment_counts = comments_df["Sentiment"].value_counts()

# Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=["red", "green", "gray"])
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Distribution of Reddit Comments")
plt.savefig("sentiment_bar_chart.png")
plt.close()

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=["red", "green", "gray"])
plt.title("Sentiment Distribution")
plt.savefig("sentiment_pie_chart.png")
plt.close()

# Word Cloud
text = " ".join(comments_df["Comment"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Frequent Words in Comments")
plt.savefig("wordcloud.png")
plt.close()

# Sentiment Trend Over Comments
plt.figure(figsize=(10, 5))
plt.plot(range(len(comments_df)), comments_df["Sentiment Score"], marker="o", linestyle="-", color="blue")
plt.xlabel("Comment Index")
plt.ylabel("Sentiment Score")
plt.title("Sentiment Trend Over Comments")
plt.axhline(0, color="gray", linestyle="--")
plt.savefig("sentiment_trend.png")
plt.close()

# Scatter Plot: Comment Length vs. Sentiment Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x=comments_df["Comment Length"], y=comments_df["Sentiment Score"], hue=comments_df["Sentiment"], palette={"Positive ✅": "green", "Negative ❌": "red", "Neutral": "gray"})
plt.xlabel("Comment Length")
plt.ylabel("Sentiment Score")
plt.title("Comment Length vs. Sentiment")
plt.savefig("comment_length_vs_sentiment.png")
plt.close()

# Separate positive and negative comments
positive_text = " ".join(comments_df[comments_df["Sentiment"] == "Positive ✅"]["Comment"])
negative_text = " ".join(comments_df[comments_df["Sentiment"] == "Negative ❌"]["Comment"])

# Word Clouds for Positive & Negative Comments
fig, ax = plt.subplots(1, 2, figsize=(15, 5))

# Positive Word Cloud
wordcloud_pos = WordCloud(width=400, height=300, background_color="white").generate(positive_text)
ax[0].imshow(wordcloud_pos, interpolation="bilinear")
ax[0].axis("off")
ax[0].set_title("Positive Comments Word Cloud")

# Negative Word Cloud
wordcloud_neg = WordCloud(width=400, height=300, background_color="white").generate(negative_text)
ax[1].imshow(wordcloud_neg, interpolation="bilinear")
ax[1].axis("off")
ax[1].set_title("Negative Comments Word Cloud")

plt.savefig("wordclouds.png")
plt.close()

# Sentiment Score Histogram
plt.figure(figsize=(8, 5))
sns.histplot(comments_df["Sentiment Score"], bins=10, kde=True, color="purple")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.title("Sentiment Score Distribution")
plt.savefig("sentiment_histogram.png")
plt.close()

print("✅ All visualizations saved successfully!")
