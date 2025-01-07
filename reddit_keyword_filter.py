import praw
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Reddit API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
USER_AGENT = os.getenv("USER_AGENT")

# Authenticate with Reddit
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT,
)

# Function to search for keywords in a subreddit
def search_subreddit(subreddit_name, keyword):
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.new(limit=50):  # Fetch latest 50 posts
        if keyword.lower() in post.title.lower() or keyword.lower() in post.selftext.lower():
            print(f"Title: {post.title}")
            print(f"Link: {post.url}\n")

# Example usage
subreddit_name = input("Enter the subreddit name: ")
keyword = input("Enter the keyword to search for: ")
search_subreddit(subreddit_name, keyword)

