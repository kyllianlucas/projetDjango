# EventHub 🎉

## Description
EventHub est une plateforme de gestion d’événements développée en Django.  
Elle permet :
- Création, modification, suppression et consultation d’événements (CRUD)
- Inscription et désinscription des participants
- Ajout d’avis avec médias (photos)
- Recommandations d’événements basées sur les intérêts de l’utilisateur
- Dashboards organisateur et administrateur avec statistiques et graphiques
- Validation ou refus des avis par l’administrateur

---

## Installation

### Prérequis
- Python 3.10+
- pip
- virtualenv

### Étapes
```bash
git clone <repo>
cd eventhub
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # pour créer un admin
python manage.py runserver
