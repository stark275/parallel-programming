import csv
import multiprocessing
from itertools import islice 
import time
import json
from concours_celery.celery import longtime_add, calculer_pourcentage

def traiter_ligne(ligne): 
    # Calculer le pourcentage de manère distribuée avec celery
    return calculer_pourcentage.delay(ligne)

# Fonction pour traiter un lot d'étudiants
def traiter_lot(fichier_csv, debut, fin):
  t0 = time.time()
  results = []

  with open(fichier_csv, "r", newline="") as fichier:
    lecteur_csv = csv.reader(fichier)
    # Sauter l'en-tête
    lecteur_csv = islice(lecteur_csv, 1, None)
    pourcentages_lot =  map(lambda ligne: traiter_ligne(ligne), islice(lecteur_csv, debut, fin + 1))
    results = list(pourcentages_lot)

  t1 = time.time()

  print(f'\n temps d\'execution {t1 - t0} s')

  while(True):
    time.sleep(0.2)
    for res in results:
      if res.ready() :
        print(res.result)
         
# Fonction principale
def main():
  # Ouvrir le fichier CSV des étudiants en lecture
  with open("../../etudiants_rabbitMQ.csv", "r", newline="") as fichier_csv:
    lecteur_csv = islice(csv.reader(fichier_csv), 1, None)
    nbr_candidats = 10000
   
  nb_processus = 4
  taille_lot = nbr_candidats // nb_processus
  debuts = [(i * taille_lot)  for i in range(nb_processus)]
  fins = [debut + taille_lot - 1 for debut in debuts]
  fins[-1] = nbr_candidats

  # print(debuts)
  # print(fins)

  # Créer et démarrer les processus
  processus = []
  for i in range(nb_processus):
    processus.append(multiprocessing.Process(
      target=traiter_lot,
      args=("../../etudiants_rabbitMQ.csv", debuts[i], fins[i]))
    )
    processus[i].start()

  # Attendre la fin de tous les processus
  for processus in processus:
    processus.join()

  
if __name__ == '__main__':
    main()