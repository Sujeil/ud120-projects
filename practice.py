from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[115.0], [140.0], [175.0]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print rescaled_weight

from nltk.corpus import stopwords
esw = stopwords.words('english')
print len(esw)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")