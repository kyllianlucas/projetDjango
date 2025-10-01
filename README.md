# EventHub 🎉

## Description
EventHub est une plateforme de gestion d’événements développée en Django.
Elle permet :
- Création et gestion d’événements (CRUD)
- Inscription des participants
- Ajout d’avis avec médias (photos)
- Recommandations d’événements
- Dashboards organisateur et administrateur avec statistiques et graphiques

## Installation

### Prérequis
- Python 3.10+
- pip + virtualenv

### Étapes
```bash
git clone <repo>
cd eventhub
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
