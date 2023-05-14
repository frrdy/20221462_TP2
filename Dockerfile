# Utilise l'image Python officielle en tant que base
FROM python:3.9-slim-buster

#dossier de travail
WORKDIR /app

#copier le contenu de main dans l'image
COPY main.py /app

#les dependances
RUN pip3 install --no-cache-dir requests==2.28.2

# Définir la commande d'exécution par défaut de l'image
CMD [ "python3", "main.py" ]
