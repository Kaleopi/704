#!/usr/bin/python3
import pika
import random as rand
import json
from git import Repo
# import githubAPI as git

def setIdJob():
    newrand = None
    f = open("ids_job.txt", "r+")
    liste = f.readlines()
    while True:
        newrand = str(rand.randint(100000,999999))+'\n'
        if newrand not in liste:
            break
    f.write(newrand)
    f.close()
    return int(newrand)

def setIdCdt():
    newrand = None
    f = open("ids_cdt.txt", "r+")
    liste = f.readlines()
    while True:
        newrand = str(rand.randint(100000,999999))+'\n'
        if newrand not in liste:
            break
    f.write(newrand)
    f.close()
    return int(newrand)


id_cdt = setIdCdt()
id_job = setIdJob()

services = ["GRAPHVIZ", "PANDOC", "IMAGEMAGICK"]
filename = "sw.jpg"
commande = "magick convert "+filename+" resultat.png"

repo = Repo()

message = {"jobID": id_job, "cdtID": id_cdt, "service": services[2], "file": filename, "commande": commande}
message = json.dumps(message)

creds = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=creds))
channel = connection.channel()
# channel.queue_declare(queue='client')
channel.basic_publish(exchange='', routing_key='client', body=message)

print("Message parti")
connection.close()


