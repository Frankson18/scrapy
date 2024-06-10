from itemadapter import ItemAdapter
import os
from scrapy.exceptions import DropItem
from google.cloud import bigquery


class ArticlescraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        titles = adapter.get('title')
        for title in titles: 
            adapter['title'] = title.replace('\n', '').strip()
        
        authors = adapter.get('author')
        
        adapter['author'] = ''.join(authors).replace(' ,', ',').replace(' and', 'and').strip()

        published_at = adapter.get('published_at')
        if isinstance(published_at, list):
            adapter['published_at'] = published_at[0] if published_at else None

        return item
    
class BigQueryPipeline:
    def __init__(self, project_id, dataset_id, table_id, key_file):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file
        self.client = bigquery.Client()

    @classmethod
    def from_crawler(cls, crawler):
        project_id = crawler.settings.get('BIGQUERY_PROJECT_ID')
        dataset_id = crawler.settings.get('BIGQUERY_DATASET_ID')
        table_id = crawler.settings.get('BIGQUERY_TABLE_ID')
        key_file = crawler.settings.get('GOOGLE_APPLICATION_CREDENTIALS')
        return cls(project_id, dataset_id, table_id, key_file)

    def process_item(self, item, spider):
        if not item.get('title'):
            raise DropItem("Missing title in item")

        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)
        table = self.client.get_table(table_ref)
        rows_to_insert = [{
            "author": item.get('author'),
            "title": item.get('title'),
            "subtitle": item.get('subtitle'),
            "content": item.get('content'),
            "published_at": item.get('published_at'),
            "url": item.get('url')
        }]
        errors = self.client.insert_rows_json(table, rows_to_insert)

        if errors:
            raise DropItem(f"Error inserting item into BigQuery: {errors}")

        return item
