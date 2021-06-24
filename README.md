# Projet TeoSchool David Espinel 'Docker coins'


Master status: [![Build Status](https://dev.azure.com/pasdethunes/teoschool-david-projet/_apis/build/status/teolia.teoSchool-david-projet?branchName=master)](https://dev.azure.com/pasdethunes/teoschool-david-projet/_build/latest?definitionId=3&branchName=master)

Develop status: [![Build Status](https://dev.azure.com/pasdethunes/teoschool-david-projet/_apis/build/status/teolia.teoSchool-david-projet?branchName=develop)](https://dev.azure.com/pasdethunes/teoschool-david-projet/_build/latest?definitionId=3&branchName=develop)

Ce projet est conçu pour montrer les différentes étapes de montage d'une usine logicielle de bout en bout y compris tout l'outillage pour la mise en place des applications depuis leur development jusqu'au déploiement en production.

## Les applications
Les applications de ce projet sont basées sur l'[orchestration workshop](https://github.com/jpetazzo/container.training) de Jérôme Petazzoni "Dockercoins".

### hasher
hasher est un service web qui fait le hashing des données POSTed.

### rng
rng est un service web qui génère des octets aléatoires.

### webui
webui est une interface web qui permet de regarder le progrès du hashing.

### worker
worker est un procès qui s'execute en arrière plan et qui est en charge de communiquer avec rng et hasher.