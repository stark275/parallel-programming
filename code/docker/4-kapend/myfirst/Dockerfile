# Dockerfile

# Utiliser l'image officielle de Python comme image de base
FROM python:3.8-slim

# Installer les dépendances système nécessaires
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    python3-dev \
    gcc libpq-dev\
    default-libmysqlclient-dev \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
RUN mkdir /code
WORKDIR /code

# Copier les fichiers requirements.txt
COPY requis.txt /code/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requis.txt

# Copier le reste de l'application
COPY . /code/

# Exposer le port de l'application
EXPOSE 8000

# Commande par défaut pour exécuter l'application
CMD ["sh", "-c", "python manage.py migrate --no-input && python manage.py runserver 0.0.0.0:8000"]
