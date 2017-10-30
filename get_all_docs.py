LISTOFDOCS = "all_docs.txt"

filenames = []

def get_filenames(filename):
	if filename == None:
		filename = LISTOFDOCS
	with open(filename, 'r') as f:
		docs = f.readlines()

		for doc in docs:
			filenames.append(str(doc).split("\n")[0])

	return filenames

def getfiles(filename):
	#print "getting file " + filename
	f = open(filename, 'r')
	doc = f.read()
	#print doc
	return doc


def getalldocs(filename = None):
	files = get_filenames(filename)
	docs = []
	for file in files:
		doc = getfiles(file)
		#print doc
		docs.append(doc)
	#print docs
	return docs


getalldocs()
print getalldocs()