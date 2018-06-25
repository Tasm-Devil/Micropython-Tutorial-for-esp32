from lib.umqtt.robust import MQTTClient
from time import sleep_ms
from machine import unique_id
from ubinascii import hexlify
from gc import mem_free

client_id   = hexlify(unique_id())
mqtt_server = "enterYourMqttServerHere.de"

client = MQTTClient(client_id, mqtt_server, 0)

def connect():
    client.connect()

def disconnect():
    try:
        client.disconnect()
    except OSError:
        print("Error! Please (re-)connect first!")
    except AttributeError:
        print("Error! call connect first!")

def publish(temp, hum, pres):
    try:
        #ask the garbage collector for the num of free bytes on the Heap and publish
        mem = mem_free()
        client.publish("deneaux/temp", str(temp))
        client.publish("deneaux/hum", str(hum))
        client.publish("deneaux/pres", str(pres))
        client.publish("deneaux/freeheap", str(mem))
    except AttributeError:
        print("Error! call connect first!")

def sub_cb(topic, msg):
    print((topic, msg))

def subscribe():
    try:
        client.set_callback(sub_cb)
        client.subscribe(b"deneaux/#")
        while True:
            client.check_msg()
            sleep_ms(1000)
    except KeyboardInterrupt:
        print("subscribe() says Bye Bye! ")
        client.disconnect()
    except OSError:
        print("Error! Please (re-)connect first!")
    except AttributeError:
        print("Error! call connect first!")

