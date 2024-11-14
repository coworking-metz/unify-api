# Programme de Heartbeat pour Unifi

Ce programme est conçu pour envoyer un signal de heartbeat à ticket backend, contenant des informations sur les clients connectés à chaque appareil UniFi du réseau (pour définir la valeur de `location`). Ce script récupère les adresses MAC des clients et la localisation des appareils, puis envoie une requête POST avec ces informations à l'URL heartbeat

## Contenu du Projet

- **location** : Script principal du programme. Ce fichier n’a pas d’extension `.py` et est configuré pour être exécuté directement.
- **unifi_api.py** : Contient les fonctions utilitaires pour récupérer les informations des appareils UniFi et de leurs clients, normaliser les adresses MAC, et envoyer les signaux heartbeat.
- **.env** : Fichier d’environnement pour stocker de manière sécurisée les configurations sensibles, telles que l’URL du backend et le jeton d’authentification.
- **README.md** : Documentation pour installer, configurer et exécuter le programme.

## Prérequis

Assurez-vous que Python 3 est installé. L'outil pip doît être dispo.

```bash
sudo apt install python3-pip
``` 

Ainsi que les bibliothèques nécessaires. Vous pouvez installer les bibliothèques requises avec la commande suivante :

```bash
pip install requests python-dotenv
``` 
## Configuration

Variables d’environnement : Créez un fichier .env dans le répertoire du projet à partir du fichier `.env.modele`  et compléter toutes les valeurs (les identifiants sont dans bitwarden)


## Exécution du Programme

Rendre le Script Exécutable : Assurez-vous que le fichier location est exécutable :

```bash
chmod +x location
```

Lancer le Script : Exécutez le script avec la commande suivante :

```bash
./location
```

Le programme enverra un signal de heartbeat contenant les informations des clients connectés pour chaque appareil UniFi.

## Automatisation avec Crontab

Pour exécuter le script automatiquement toutes les 3 minutes, vous pouvez ajouter le script `./location` à crontab.


Ajoutez la ligne suivante à la fin du fichier crontab pour exécuter le script toutes les 3 minutes Exemple si le depot est installé dans `/opt/unify-api/location`

```crontab
*/3 * * * * /opt/unify-api/location > /dev/null 2>&1
```

Remplacez /chemin/vers/votre/dossier/location par le chemin complet du fichier location dans votre système.

