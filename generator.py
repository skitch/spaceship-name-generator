import random

with open('nouns.txt','r') as noun:
	nouns = [line.strip() for line in noun]
with open('adjectives.txt','r') as adj:
	adjectives = [line.strip() for line in adj]


for i in range(50):
	print(random.choice(adjectives).capitalize() + " " + random.choice(nouns).capitalize())