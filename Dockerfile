# Utilise l'image Python officielle en tant que base
FROM python:3.9-slim-buster

#dossier de travail
WORKDIR /app

#copier le contenu de TP1 dans l'image
COPY TP2.py /app

#les dependances
RUN pip3 install --no-cache-dir requests==2.28.2

# Définir la commande d'exécution par défaut de l'image
CMD [ "python3", "TP2.py" ]
