# Scrapy Articles and Flask Integration Project with BigQuery

This project integrates a Scrapy spider with a Flask API to scrape articles, store them in Google BigQuery, and provide a search functionality through a REST API.

## Prerequisites

- Python 3.x
- Google Cloud SDK (with BigQuery API enabled)
- Create a project/dataset/table in BigQuery
- Google Cloud credentials JSON file

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Frankson18/scrapy_articles
   cd scrapy_articles
2. **Create and activate a virtual environment:**
    ```python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the dependencies:**
    ```
    pip install -r requirements.txt
4. **Configure environment variables:**
Update the following variables in settings.py and app.py with your actual Google Cloud project details:
    - BIGQUERY_PROJECT_ID
    - BIGQUERY_DATASET_ID
    - BIGQUERY_TABLE_ID
    - GOOGLE_APPLICATION_CREDENTIALS (path to your JSON key file)
## Running the Scrapy Spider
1. **Navigate to the project directory:**
    ```
    cd articlescraper
2. **Run the Scrapy spider:**
    ```
    scrapy crawl newsscrapper
## Running the Flask API
1. **Set environment variables and run the Flask app:**
    ```
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
2. **On Windows (Command Prompt):**
    ```
    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run
3. **Access the API:**
    ```
     http://127.0.0.1:5000/search?q=exemple

## Results
![Scrapy results](img/table_bq.png)
![Api results](img/flask_api.png)