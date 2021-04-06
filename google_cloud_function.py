"""
아래 코드는 로컬 파일이 아닌 Google Cloud Function 페이지에서 작성해야 함
"""

import base64
import json
from google.cloud import bigquery


def tweets_to_bq(tweet):
    client = bigquery.Client()
    # BigQuery에 만든 데이터셋
    dataset_ref = client.dataset('tweet_data')
    # BigQuery에 만든 테이블
    table_ref = dataset_ref.table('tweets')
    table = client.get_table(table_ref)

    tweet_dict = json.loads(tweet)
    # 넣기
    rows_to_insert = [
        (tweet_dict['id'], tweet_dict['created_at'], tweet_dict['text'])
    ]

    error = client.insert_rows(table, rows_to_insert)
    print(error)


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    tweets_to_bq(pubsub_message)


"""
requirements.txt 에 아래 추가

google-cloud-bigquery
"""