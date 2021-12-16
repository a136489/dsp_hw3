import sys

input_file = sys.argv[1]
output_file = sys.argv[2] 

# constructing map
file = open(input_file, 'r', encoding='big5hkscs')
mapping = {}
for line in file:
	tmp = line.split()
	word = tmp[0]
	ZhuYins = tmp[1].split('/')
	
	for ZY in ZhuYins:
		if ZY[0] not in mapping.keys():
			mapping[ZY[0]] = set()
		mapping[ZY[0]].add(word)

	mapping[word] = {word}

# output
file = open(output_file, 'w', encoding='big5hkscs')
for (ZY, words) in mapping.items():
	line = ZY + '\t' + ' '.join(words)
	print(line, file = file)