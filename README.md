# CIS192 Final Project - NLP Taylor Swift Lyric Generator
### Juliana Lu, Kira Wang

## Installation Instructions:
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Code Structure:
### Folder structure:
* ```lyrics``` - contains all of our corpuses, one corpus for each album and one corpus for all of Taylor Swift's song lyrics
* ```generator``` - contains the code for our website (Django structure) + the code for our NLP (lyric_generator.py)  
  
A Django framework website with a lyric generator app.  
Generates Taylor Swift lyrics given input from various albums.  
Uses NLP given corpus of lyrics from album to generate fake lyrics, 
utilizing probabilities from old Taylor Swift lyrics.  
On the website, you can specify if you want to generate new lyrics from all songs, or one of her 10 albums.

