import glob
filenames = glob.glob('paper_abstracts/*.txt')
all_docs = open('all_docs.txt','w')
for file in filenames:
	print>>all_docs, file