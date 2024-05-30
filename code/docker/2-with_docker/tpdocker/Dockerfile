# Utiliser une image Python officielle comme image de base
FROM python:3.11-slim-bullseye
# Définir le répertoire de travail dans le conteneur
WORKDIR /projet

RUN pip3 install Django
# Copier le reste du code source de l'application dans le conteneur
COPY . .

CMD [ "python3", "manage.py", "runserver", "--bind", "0.0.0.0:8000" ]
# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000
# Définir la commande pour exécuter l'application



# FROM python:3.11-slim-bullseye

# LABEL org.opencontainers.image.authors="Team L1FASI-IG-24"
# LABEL "Vendor"="Team L1FASI-IG-24"
# LABEL version="0.1"

# ENV PYTHONUNBUFFERED=1
# WORKDIR /projet

# RUN apt-get update -y
# # Production config (https)
# RUN apt-get install apt-transport-https
# # Install necessary package for django runtime
# RUN apt-get install -y default-libmysqlclient-dev \
#         pkg-config \
#         libpango-1.0-0  \ 
#         libharfbuzz0b \
#         libpangoft2-1.0-0 \
#         libpangocairo-1.0-0 \
#         libxml2-dev \ 
#         libxslt-dev \
#         libffi-dev \
#         libcairo2-dev \
#         libpango1.0-dev --fix-missing

# # Install gcc
# RUN apt-get install -y build-essential

# RUN pip3 install Django

# COPY ./ ./

# CMD [ "python3", "manage.py", "migrate", "--bind", "0.0.0.0:8000" ]

# EXPOSE 8000
