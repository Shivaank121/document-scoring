from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
analyser = SentimentIntensityAnalyzer()

with open('Agra Art Gallery.json', 'r') as f:
	data = json.load(f)

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

i = 0
for r in data:
	if i == 15:
		break
	sentiment_analyzer_scores(r["review"])
	print()
	i += 1

