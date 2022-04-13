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
    owner_id = 0
    activity_id = 0

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
        name = fake.name()
        owner_id += 1
        str_date = str(fake_date)
        producer.send(topic_name2, {'fitbit_owner': name, 'owner_id': owner_id, 'date': str_date})
        num_activities = fake.pyint(1,5)
        single_activity = 1
        while single_activity <= num_activities:
            activity_id += 1
            total_steps = fake.pyint(1500, 10000)
            exercise = fake.word(ext_word_list=modes_of_excercise)
            calories = fake.pyint(200, 875)
            active_minutes = fake.pyint(35, 100)
            sedentary_minutes = fake.pyint(5, 20)
            producer.send(topic_name1, {'date': str_date, 'total_steps': total_steps, 'exercise': exercise,
                                       'calories_burnt': calories, 'active_mins': active_minutes,
                                       'sedentary_mins': sedentary_minutes, 'owner_id': owner_id, 'activity_id': activity_id})
            single_activity += 1
        print(f"Inserted entry '{name}' to '{topic_name2}'")
        print(f"Inserted {num_activities} activities against '{name}' in '{topic_name1}'")
        sleep(10)


main()
