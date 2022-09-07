from random import sample
from dictionary.word_frequency import WordFrequency

data_filename = "Assign1-s3910311-s3912660\sampleData200k.txt"
words_frequencies_from_file = []

data_file = open(data_filename, 'r')
for line in data_file:
    words_frequencies_from_file.append(line)

sample100k = sample(words_frequencies_from_file, 100000)
sample50k = sample(words_frequencies_from_file, 50000)
sample20k = sample(words_frequencies_from_file, 20000)
sample10k = sample(words_frequencies_from_file, 10000)
sample5k = sample(words_frequencies_from_file, 5000)
sample1k = sample(words_frequencies_from_file, 1000)
sample500 = sample(words_frequencies_from_file, 500)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData100k.txt', 'w') as f:
    for word in sample100k:
        f.write("%s" % word)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData50k.txt', 'w') as f:
    for word in sample50k:
        f.write("%s" % word)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData20k.txt', 'w') as f:
    for word in sample20k:
        f.write("%s" % word)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData10k.txt', 'w') as f:
    for word in sample10k:
        f.write("%s" % word)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData5k.txt', 'w') as f:
    for word in sample5k:
        f.write("%s" % word)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData1k.txt', 'w') as f:
    for word in sample1k:
        f.write("%s" % word)

with open(r'C:/Users/user\Desktop/alg/algo-analysis/Assign1-s3910311-s3912660/sampleData500.txt', 'w') as f:
    for word in sample500:
        f.write("%s" % word)

