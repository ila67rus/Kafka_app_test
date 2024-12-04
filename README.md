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
git clone https://github.com/yourusername/kafka-app.git
cd kafka-app
```
### 2. Создайте Kafka-топик вручную (до запуска контейнера kafka_app):
Перед запуском контейнера **kafka_app**, необходимо создать топик в Kafka.

Выполните следующую команду для создания топика hello_topic:
```bash
docker-compose exec kafka bash
kafka-topics --create --topic hello_topic --partitions 1 --replication-factor 1 --bootstrap-server kafka:9092
```
### 3. Запустите Docker-контейнеры:
Используйте следующую команду для запуска контейнеров, описанных в **docker-compose.yml**:
```bash
docker-compose up -d
```
### 4. Запустите команду для отправки сообщения (продюсер):
После того как контейнеры запущены, вы можете отправить сообщение в Kafka, используя следующую команду:
```bash
docker exec -it kafka_app_test-kafka_app-1 sh
python3 main.py produce --message "Hello World!" --topic "hello_topic" --kafka "kafka_app_test-kafka-1:9092"
```
Эта команда отправит сообщение `Hello World!` в Kafka-топик hello_topic.

### 5.Запустите команду для потребления сообщений (консумер):
Для начала потребления сообщений из Kafka, используйте следующую команду:
```bash
docker exec -it kafka_app_test-kafka_app-1 sh
python3 main.py consume --topic "hello_topic" --kafka "kafka_app_test-kafka-1:9092"
```
---
## Docker-образ
Вы можете найти Docker-образ для этого проекта на Docker Hub:
- Docker Hub: https://hub.docker.com/r/mekkuyaku/kafka_app