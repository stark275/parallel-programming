import pika
import time
import json

credentials = pika.PlainCredentials('guest', 'guest')
connexion = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/',
        credentials=credentials
    )
)
channel = connexion.channel()

def var_dump(var):
  json_data = json.dumps(var, indent=4)
  print(json_data)

def myCallback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Fonction pour calculer le pourcentage d'un étudiant
def calculer_pourcentage(ch, method, properties, body):
    print("---------------------------------------------")
    notes =  eval(str(body)[1:].strip("'"))
    print(notes)
    total = sum(notes)
    pourcentage = (total / (len(notes) * 20)) * 100

    # return round(pourcentage, 2)

    print("[x-] Pourcentage %r" % round(pourcentage, 2))

    print("---------------------------------------------")



channel.queue_declare(queue='l1fasi_queue')

channel.basic_consume(queue='l1fasi_queue', on_message_callback=calculer_pourcentage, auto_ack=True)

print(" [*] Waiting for messages. To exit, press CTRL+C")
channel.start_consuming()