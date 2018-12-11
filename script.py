# -*- coding: utf-8 -*-
from nltk.corpus import PlaintextCorpusReader
import re
corpus_root = 'F:\\KAIO UFPI\\8 Periodo\\PLN\\PLN_env\\trab_final\\playlists'
meuCorpus = PlaintextCorpusReader(corpus_root, '.*')

meucsv = "Source,Target,Musica\n"
listaCidades = meuCorpus.fileids()
for cidadeOr in range(0,len(listaCidades)-1):
	for musicaOr in re.split(r'\n', meuCorpus.raw(listaCidades[cidadeOr])[:-1]):
		for cidadeDe in range(cidadeOr + 1, len(listaCidades)):
			if musicaOr in re.split(r'\n', meuCorpus.raw(listaCidades[cidadeDe])[:-1]):
				meucsv += listaCidades[cidadeOr][:-4] +','+ listaCidades[cidadeDe][:-4] + ',"' + musicaOr[:-1] + '"' + '\n'

print(meucsv)