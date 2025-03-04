print("h")

import pymorphy2
import pymystem3
#from pyaspeller import YandexSpeller

m2 = pymorphy2.MorphAnalyzer()
m3 = pymystem3.Mystem()
#speller = YandexSpeller()
#text = 'В суботу утромь'
#changes = {change['word']: chande['s'][0] for change in speller.spell(text)}
#for word, suggestion in changes.items():
#    text = text.replace(word, suggestion)

u = m2.parse('шёл')[0]

print(u.normal_form)
print(m3.analyze('шёл')[0])



sentences = [['Привет', 'меня', 'зовут', 'Катя'],
             ['каждый', 'охотник', 'желает', 'знать'],
             ['мама', 'мыла', 'раму', 'каждый', 'день'],
             ['привет', 'приятно', 'познакомиться']]

from gensim.models.word2vec import Word2Vec

model = Word2Vec(sentences, size=100, window=10, min_count=1, workers=4)


print(model.most_similar('мама'))