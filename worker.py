#!/usr/bin/python3
import pika
import json
from datetime import datetime

def callback(ch, method, properties, body):
        recu = body.decode('utf-8')
        recu = json.dumps(recu)
        print(recu)
        # channel.basic_publish(exchange='', routing_key='worker', body=recu)

def send_amqp(message):
        creds = pika.PlainCredentials('guest','guest')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=creds)) #localhost ici nan ? ou l'ip 172.18.10.77
        channel = connection.channel()
        # channel.queue_declare(queue='worker')
        channel.basic_publish(exchange='', routing_key='worker', body=message) # y as pas un soucis de quote là ?

        print("Message parti")
        connection.close()

creds = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=creds))
channel = connection.channel()

print("En attente de message...")

channel.basic_consume(queue="worker", on_message_callback=callback, auto_ack=True)
# channel_worker.basic_consume(queue="worker", on_message_callback=callback, auto_ack=True)

channel.start_consuming()
# channel_worker.start_consuming()
