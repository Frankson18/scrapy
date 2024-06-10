from flask import Flask, request, jsonify
from google.cloud import bigquery
import os

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =  'C:/Users/frank/OneDrive/Documentos/scrapy/articlescraper/articlescraper/scrapy-articles-c1c64565f67b.json'
client = bigquery.Client()

BIGQUERY_PROJECT_ID = 'scrapy-articles'
BIGQUERY_DATASET_ID = 'the_guardian_articles'
BIGQUERY_TABLE_ID = 'articles'

@app.route('/search', methods=['GET'])
def search():
    query_word = request.args.get('q')
    if not query_word:
        return jsonify({'error': 'Query parameter q is required'}), 400

    query =  f"""
        SELECT url
        FROM `{BIGQUERY_PROJECT_ID}.{BIGQUERY_DATASET_ID}.{BIGQUERY_TABLE_ID}`
        WHERE LOWER(title) LIKE '%{query_word}%'
        OR LOWER(subtitle) LIKE '%{query_word}%'
        OR LOWER(content) LIKE '%{query_word}%'
    """

    query_job = client.query(query)
    results = query_job.result()

    urls = [row.url for row in results]

    return jsonify({'urls': urls})

if __name__ == '__main__':
    app.run(debug=True)