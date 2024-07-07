import random
import time


def delay(n):
  time.sleep(n)


# List of anime
action = [
    'Shingeki no Kyojin', 'Fullmetal Alchemist: Brotherhood', 'One Punch Man',
    'Sword Art Online', 'Kimetsu no Yaiba', 'Boku no Hero Academia', 'Naruto',
    'Hunter x Hunter', 'Tokyo Ghoul', 'Jujutsu Kaisen', 'Naruto Shippuden',
    'One Piece'
]

adventure = [
    'Magi: The Labyrinth Of Magic', 'Vinland Saga', 'Berserk (1997)',
    'Tengen Toppa Gurren Lagann', 'JoJo’s Bizarre Adventure',
    'Frieren: Beyond Journey’s End', 'One Piece', 'Hunter X Hunter',
    'Dragon Quest: The Adventure Of Dai', 'Dragon Ball'
]

romantic = [
    'Sword Art Online', 'Shigatsu wa Kimi no Uso', 'Toradora!',
    'Sword Art Online II', 'Seishun Buta Yarou wa Bunny Girl Senpai',
    'Darling in the FranXX', 'Elfen Lied', 'Yahari Ore no Seishun Love Comedy',
    'High School DxD', 'Clannad', 'Bakemonogatari', 'Horimiya',
    'Chuunibyou demo Koi ga Shitai!', 'Howl no Ugoku Shiro',
    'Kaichou wa Maid-sama!', 'Sakura-sou no Pet na Kanojo',
    'Clannad: After Story', 'Nisekoi', 'Kanojo, Okarishimasu'
]

horror = [
    'Death Note', 'Paranoia Agent', 'Devilman Crybaby', 'Parasyte',
    'Boogiepop Phantom', 'Perfect Blue', 'Therate of Darkness', 'Hellsing'
]

hentai = [
    'Sei Micaela Gakuen Hyôryûki II', 'One: Kagayaku Kisetsu e',
    'Doragon Naito Gaiden', 'Chu²',
    'Crazy Over His Fingers: Just the Two of Us in a Salon After Closing',
    '25-sai No Joshikousei', 'Hotel Bitch', 'Papa Datte, Shitai', 'Over Flow',
    'Dutch Wife 28'
]

genres = {
    "action": action,
    "adventure": adventure,
    "romantic": romantic,
    "horror": horror,
    "hentai": hentai
}

# Main program
user = input('Hey, welcome to our website! What is your name? ')
delay(1)
print("Hello", user)
delay(2)
print("Type of genre in anime:")
print("a. Action\nb. Adventure\nc. Horror\nd. Romantic\ne. Hentai")

while True:
  delay(3)
  anime_genre = input(
      "What type of anime do you want to watch? Please select your genre: "
  ).lower()

  if anime_genre in genres:
    print(anime_genre.capitalize(), "- Your choice is:",
          random.choice(genres[anime_genre]))
    break
  else:
    print("Sorry, we don't recognize the genre:", anime_genre)
    print(
        "Please enter a valid genre: a. Action, b. Adventure, c. Horror, d. Romantic, e. Hentai"
    )
