import requests, re
from unicodedata import normalize
import unidecode

re_br = re.compile(' BR$', re.I)
re_inicio_titulo = re.compile('The Sound of ', re.I)

cachorro = ['https://api.spotify.com/v1/playlists/6HpBYYSj2Ekbk4KMEqfXTU',
'https://api.spotify.com/v1/playlists/2niJAkfLqjhPnzpLixYl7h',
'https://api.spotify.com/v1/playlists/2xE5Z5pnvyNLKoo1kCkwFe',
'https://api.spotify.com/v1/playlists/0nFPFxzBc3SWbwaneiZQXw',
'https://api.spotify.com/v1/playlists/7FeEIQE2SA2DnDINp3Q0m8',
'https://api.spotify.com/v1/playlists/0fobacSKKqIxsNLK5ZR30S',
'https://api.spotify.com/v1/playlists/654ZiW7lLyjUXZlfFJPhT7',
'https://api.spotify.com/v1/playlists/5ngQac05vn8kHLmnEuFXwK',
'https://api.spotify.com/v1/playlists/1s83xcj4GrvcbGEu82rJ9U',
'https://api.spotify.com/v1/playlists/30iOfJzkPhiW1YNR2KYWiE',
'https://api.spotify.com/v1/playlists/7lmo9jOcf5BaDRcVHmEWgr',
'https://api.spotify.com/v1/playlists/5NTCNh5Nnd6cJcOoyYkeur',
'https://api.spotify.com/v1/playlists/1C0qVjGDRNflAQmKckeuXQ',
'https://api.spotify.com/v1/playlists/3n52WgKQlMp4igxvdoVNHI',
'https://api.spotify.com/v1/playlists/2X4Ug6gjllZZtCVTXcbBba',
'https://api.spotify.com/v1/playlists/6CuHx0PQqNygXgcOXV8GRT',
'https://api.spotify.com/v1/playlists/0GBWGFEatBTLo6DLiCqVWK',
'https://api.spotify.com/v1/playlists/6S2q3IyYouIW4luqohbCuG',
'https://api.spotify.com/v1/playlists/6EjGY2g4TZIu3MZ0RwRv1n',
'https://api.spotify.com/v1/playlists/0nxQfhOoJtLPLgj1Miqf76',
'https://api.spotify.com/v1/playlists/6MP0EKbToSg5mLY6oNOO0X',
'https://api.spotify.com/v1/playlists/6Dgj4lSaAtWbIsSelM0Ttp',
'https://api.spotify.com/v1/playlists/4FEX4CQRt386ptxFQSIXT1',
'https://api.spotify.com/v1/playlists/5QHKGAtHcAuvhMkOCJfe8f',
'https://api.spotify.com/v1/playlists/78iFduxEcgZWsXV6ctovIN']

def remove_acentos(texto):
	return unidecode.unidecode(texto).lower()



def get_musicas():
	token = "Bearer " + "BQDotM7v-PBGXjMhCS3jtcZ6LsYOXlhGrocTSeiX2aycIHV_wKC0KrQLCG30YcgNZi88SGbgegJVdvt33EzZa_EEedFEaUkrGr84RXa-DI-237j8u7EEg5LO_TISv8v_lBNNGM1VGy6K-8N219s3H7h1mG56TUPZ4ZE-jLaS4Pw"
	headers = {"accept": "application/json", "content-type": "application/json","authorization": token}
	for link in cachorro:
		r = requests.get(link, headers=headers)
		j = r.json()
		titulo_playlist = j['name']
		musicas = j['tracks']['items']
		nome_mus = []
		for musica in musicas:
			nome_mus.append(remove_acentos(musica['track']['name']))
		nome_cidade = re_inicio_titulo.sub('', re_br.sub('', titulo_playlist))
		salvar(nome_cidade,nome_mus)
		print('Escreveu ', nome_cidade)




def salvar(nome_cidade,musicas):
	f = open('./playlists/' + remove_acentos(nome_cidade) + ".txt", "w")

	for musica in musicas:
		f.write(
			remove_acentos(musica) + '\n'
		)
	f.close()

get_musicas()

 	

#map(lambda x: print('a: ',x), musica['track']['artists'])