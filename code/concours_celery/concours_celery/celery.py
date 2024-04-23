from celery import Celery
import time

app = Celery('concours_celery',
             broker='amqp://guest:guest@127.0.0.1/',
             backend='redis://localhost:6379')

@app.task
def calculer_pourcentage(ligne):
  # NomNotes = [int(note) for note in ligne[1:]]
  notes = [int(note) for note in ligne[1:]]
  pourcentage = (sum(notes) / (len(notes) * 20)) * 100
 
  return (ligne[0], round(pourcentage, 2))

@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print('long time task finished')
    return x + y


