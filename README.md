# Data Engineering w/ Google Cloud Platform(GCP)
* 무인으로 동작하는 실시간 데이터 파이프라인 만들기



## 사용할 도구
* Twitter Streaming Data
* Google Cloud Pub/Sub
* BigQuery
* Google Cloud Functions
* DataStudio
* Google Kubernetes Engine



## Twitter Streaming Data

* https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/overview
* https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/api-reference/post-statuses-filter
* 트위터에서는 스트리밍 데이터를 무료로 활용할 수 있는 API 제공



## Google Cloud Pub/Sub
* https://cloud.google.com/pubsub/docs/overview
* 완전관리형 실시간 메세징 서비스
* Kafka와 유사
* Publisher → Pub/Sub Topic → Subscriber
  * Kafka: Producer → Broker (Kafka Topic) → Consumer



## BigQuery
* 완전관리형 SQL 데이터 웨어하우스
* 매우 큰 데이터도 매우 저렴하게 저장, 빠른 속도로 처리 가능



## Google Cloud Functions
* 구글 클라우드의 서버리스 제품
* 트리거 조건과 코드를 설정해놓으면 원하는 동작을 자동으로 수행함



## DataStudio
* 다양한 소스를 연결할 수 있는 대시보드 서비스
* 이외에도 사용할 수 있는 서비스
* Tableau, Holistics, Redash, Metabase, Superset 등



## Google Kubernetes Engine(not easy)
* App? Service?
* Deployment? Operation?
* Container? Docker?
* Orchestration? Kubernetes?
* 무중단 배포, 자동 배포
