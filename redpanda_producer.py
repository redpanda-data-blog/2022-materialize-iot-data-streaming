# DB MODEL HAS Date, step_count, mode_of_exercise, calories_burnt, Very Active minutes, Sedantary minutes
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from time import sleep
from faker import Faker
import json


def main():
    topic_name1 = "fitbit_activity_tracker"
    topic_name2 = 'fitbit_owner'
    modes_of_excercise = ['cycling', 'skiing', 'walking', 'jogging', 'running', 'swimming', 'climbing',
                          'football', 'basketball', 'tennis', 'badminton', 'volleyball', 'rugby', 'cricket', 'baseball']
    fake = Faker()

    try:
        # Create Kafka topic
        topic1 = NewTopic(name=topic_name1, num_partitions=1, replication_factor=1)
        topic2 = NewTopic(name=topic_name2, num_partitions=1, replication_factor=1)
        admin = KafkaAdminClient(bootstrap_servers="localhost:9092")
        admin.create_topics([topic1, topic2])
    except Exception:
        print(f"Topic {topic_name1, topic_name2} is already created")

    producer = KafkaProducer(bootstrap_servers=["localhost:9092"],
                             value_serializer=lambda m: json.dumps(m).encode('ascii'))
    for i in range(100000):
        fake_date = fake.date_this_year(True, True)
        total_steps = fake.pyint(1500, 10000)
        exercise = fake.word(ext_word_list=modes_of_excercise)
        calories = fake.pyint(200, 875)
        active_minutes = fake.pyint(35, 100)
        sedantary_minutes = fake.pyint(5, 20)
        name = fake.name()
        str_date = str(fake_date)
        producer.send(topic_name1, {'date': str_date, 'total_steps': total_steps, 'exercise': exercise,
                                   'calories_burnt': calories, 'active_mins': active_minutes,
                                   'sedantary_mins': sedantary_minutes})
        producer.send(topic_name2, {'calories': calories, 'owner': name})
        print("Inserted entry ", i, " to both topics")
        sleep(0.5)


main()