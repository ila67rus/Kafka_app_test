# Kafka-приложение с Docker

## Описание
Этот проект представляет собой Python-приложение, которое взаимодействует с Apache Kafka. В нем реализованы как продюсер, так и консумер для работы с топиками Kafka, которые можно запускать через командную строку. Проект упакован в Docker-контейнер, а окружение настроено с использованием Docker Compose.

## Требования
Перед тем как начать, убедитесь, что у вас установлены следующие инструменты:

- Docker
- Docker Compose

---
## Настройка

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/ila67rus/Kafka_app_test.git
cd Kafka_app_test
```
### 2. Запустите Docker-контейнеры:
Используйте следующую команду для создания и запуска контейнеров, описанных в **docker-compose.yml**:
```bash
docker-compose up --build
```
### 3. Запустите команду для отправки сообщения (продюсер):
После того как контейнеры запущены, вы можете отправить сообщение в Kafka, используя следующую команду:
```bash
docker exec -it kafka_app_test-kafka_app-1 sh
python3 main.py produce --message "Hello World!" --topic "hello_topic" --kafka "kafka_app_test-kafka-1:9092"
```
Эта команда отправит сообщение `Hello World!` в Kafka-топик hello_topic.

### 4. Запустите команду для потребления сообщений (консумер):
Для начала потребления сообщений из Kafka, используйте следующую команду:
```bash
docker exec -it kafka_app_test-kafka_app-1 sh
python3 main.py consume --topic "hello_topic" --kafka "kafka_app_test-kafka-1:9092"
```
---
## Docker-образ
Вы можете найти Docker-образ для этого проекта на Docker Hub:
- Docker Hub: https://hub.docker.com/r/mekkuyaku/kafka_app_test