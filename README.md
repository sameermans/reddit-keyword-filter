# reddit-keyword-filter
A Reddit keyword monitoring script


This project allows you to filter Reddit posts based on specified keywords using the Reddit API. It filters out posts containing certain keywords from the Reddit feed.

## Prerequisites

- Python 3.7+
- `pip` (Python package installer)
- A Reddit account and API credentials 

## Installation

### 1. Clone the Repository

git clone https://github.com/sameermans/reddit-keyword-filter.git
cd reddit-keyword-filter

 ### Install Dependencies
You will need to install the project dependencies listed in requirements.txt.
pip install -r requirements.txt

 ### Configure Your Credentials
Create a .env file in the project root directory, and copy the contents of .env.example into it. Replace the placeholder values with your credentials.

Example of .env file:
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
USERNAME=your_reddit_username
PASSWORD=your_reddit_password

### Run the Project
Now you can run the script to start filtering posts:
python3 reddit_keyword_filter.p
