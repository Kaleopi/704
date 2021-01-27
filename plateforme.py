#!/usr/bin/python3
import pika
import datetime
import json
import githubAPI as git
import os

services = ["GRAPHVIZ", "PANDOC", "IMAGEMAGICK"]

def callback(ch, method, properties, body):
        recu = body.decode('utf-8')
        obj = json.loads(recu)
        jobID = obj['jobID']

        # channel.basic_publish(exchange='', routing_key='worker', body=recu)

creds = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=creds))
channel = connection.channel()

channel.queue_declare(queue="client")
channel.queue_declare(queue="worker")

print("En attente de message...")

channel.basic_consume(queue="client", on_message_callback=callback, auto_ack=True)
# channel_worker.basic_consume(queue="worker", on_message_callback=callback, auto_ack=True)

channel.start_consuming()
# channel_worker.start_consuming()