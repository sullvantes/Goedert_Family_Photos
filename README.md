# Goedert_Family_Photos
To Create Dev Server:
  - mkdir "Fam_Photos"
  - cd "Fam_Photos"
  - clone repo.
  - install python3 and pip3 and virtualenv
  - run 'virtualenv -p python3 venv'
  - activate venv: 'source venv/bin/activate'
  - install requirements from file: 'pip3 install -r requirements.txt'
  - build db: 'cd Goedert_Family_Photos; python manage.py migrate'
  - create superuser: 'python manage.py createsuperuser'
  - run server: 'python manage.py runserver'
  
  if you have questions, reach 
