import pika

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

def myCallback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.queue_declare(queue='l1fasi_queue')

channel.basic_consume(queue='l1fasi_queue', on_message_callback=myCallback, auto_ack=True)

print(" [*] Waiting for messages. To exit, press CTRL+C")
channel.start_consuming()