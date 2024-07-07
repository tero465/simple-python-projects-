from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Anime genres with details
genres = {
    "action": [
        {"name": 'Shingeki no Kyojin', "details": 'A story about humanity’s fight against giant humanoid Titans.'},
        {"name": 'Fullmetal Alchemist: Brotherhood', "details": 'Two brothers search for the Philosopher\'s Stone to restore their bodies.'},
        {"name": 'One Punch Man', "details": 'A superhero who can defeat any opponent with a single punch seeks a worthy foe.'}
    ],
    "adventure": [
        {"name": 'Magi: The Labyrinth Of Magic', "details": 'Adventures in a world inspired by One Thousand and One Nights.'},
        {"name": 'Vinland Saga', "details": 'A story of Viking warriors and their quest for revenge and peace.'}
    ],
    "romantic": [
        {"name": 'Sword Art Online', "details": 'Players of a virtual reality MMORPG are trapped in the game, and must clear all levels to escape.'},
        {"name": 'Shigatsu wa Kimi no Uso', "details": 'A piano prodigy rediscovers his love for music with the help of a spirited violinist.'}
    ],
    "horror": [
        {"name": 'Death Note', "details": 'A high school student discovers a notebook that allows him to kill anyone by writing their name in it.'},
        {"name": 'Paranoia Agent', "details": 'A series of attacks by a mysterious boy with a bat leads to paranoia and fear.'}
    ],
    "hentai": [
        {"name": 'Sei Micaela Gakuen Hyôryûki II', "details": 'Explicit adult content involving students and teachers in a fantasy setting.'},
        {"name": 'One: Kagayaku Kisetsu e', "details": 'Explicit adult content involving romantic relationships between students.'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user = request.form['name']
    genre = request.form['genre'].lower()
    
    if genre in genres:
        anime = random.choice(genres[genre])
        return render_template('result.html', user=user, anime=anime)
    else:
        error = "Invalid genre selected. Please try again."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
