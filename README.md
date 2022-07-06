
# Using Materialize and Redpanda for real-time IoT data streaming

Learn how you can combine the power or Materialize and Redpanda to create a Fitbit-style activity tracking application.

Follow along with [this blog post tutorial](https://redpanda.com/blog/loT-streaming-data-materialize-redpanda) to put this demo into action. 

--------------

## Fitbit data generation
### The schema for the topics are

![image](https://user-images.githubusercontent.com/102608342/163138012-be11ad54-fb00-4c79-b225-ee594d3dfe6c.png)

### Steps to configure the code and get it working
1) Clone the workspace
2) cd to the directory when you have cloned the codebase
3) ```sudo apt-get update```
4) ```sudo apt-get install python3-pip python3-dev```
5) ```virtualenv myprojectenv```
6) ```source myprojectenv/bin/activate```
7) ```pip3 install -r requirements.txt```

### Update broker values
By default the code assumes that you have setup redpanda in your localhost. Incase you are setting up
redpanda in a docker/mac environment. You will need to update the parameter ```REDPANDA_BROKER_IP``` in the ```.env``` file

![image](https://user-images.githubusercontent.com/102608342/163139789-198faadf-6e65-4bdc-9c1a-10fc11a57d75.png)

### Running the code
```python redpanda_producer.py```

-----------
## About Redpanda 

Redpanda is Apache Kafka® API-compatible. Any client that works with Kafka will work with Redpanda, but we have tested the ones listed [here](https://docs.redpanda.com/docs/reference/faq/#what-clients-do-you-recommend-to-use-with-redpanda).

* You can find our main project repo here: [Redpanda](https://github.com/redpanda-data/redpanda)
* Join the [Redpanda Community on Slack](https://redpanda.com/slack)
* [Sign up for Redpanda University](https://university.redpanda.com/) for free courses on data streaming and working with Redpanda
