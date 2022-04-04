# This codebase contains the files which create 2 redpanda topics and push data to them in a json format
### The schema for the topics are

![Screenshot 2022-03-29 213712](https://user-images.githubusercontent.com/102608342/160656364-0be1c2a6-79af-43a0-8093-64d5f4a0c240.png)

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
redpanda in a docker/mac environment you will need to update the ```admin``` and ```producer``` values
in the code to match the broker values (choose any single one) on your environment. The following are the
locations where the values would need to be updated.

![image](https://user-images.githubusercontent.com/102608342/161502626-fc464ca1-5ea6-44ac-8fa1-748adebfc467.png)

### Running the code
```python redpanda_producer.py```

The code creates 100000 records with 1 record every 0.5 seconds. You can stop the execution anytime by hitting ```ctrl + c```
