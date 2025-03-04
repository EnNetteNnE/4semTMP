import zipfile
import wget
import gensim

model_url = 'http://vectors.nlpl.eu/repository/20/180.zip'
m = wget.download(model_url)
model_file = model_url.split('/')[-1]
with zipfile.ZipFile(model_file, 'r') as archive:
   stream = archive.open('model.bin')
   model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)

words = ['день_NOUN']

for word in words:
   # есть ли слово в модели? Может быть, и нет
   if word in model:
       print(word)
       # выдаем 10 ближайших соседей слова:
       for i in model.most_similar(positive=[word], topn=10):
           # слово + коэффициент косинусной близости
           print(i[0], i[1])
       print('\n')
   else:
       # Увы!
       print(word + ' is not present in the model')

print('Расстояние между человек и обезьяна: ')
print(model.similarity('человек_NOUN', 'обезьяна_NOUN'))

print('Лишенее между яблоко, гурша, виноград, банан, лимон, картофель: ')
print(model.doesnt_match('яблоко_NOUN груша_NOUN виноград_NOUN банан_NOUN лимон_NOUN картофель_NOUN'.split()))

print('Пицца + россия - италия: ')
print(model.most_similar(positive=['пицца_NOUN', 'россия_NOUN'], negative=['италия_NOUN'])[0][0])
