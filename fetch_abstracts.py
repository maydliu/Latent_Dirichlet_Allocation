import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("https://www.eecs.mit.edu/people/faculty-advisors")
soup = BeautifulSoup(page,'html.parser')
faculty = []

faculty_rows = soup.find_all('div',attrs={'class':'views-field views-field-title'})
for i in range(len(faculty_rows)):
	faculty.append(faculty_rows[i].getText())
    

for faculty_member in faculty:
    first_name = faculty_member.split()[0]
    last_name = faculty_member.split()[-1]
    if last_name == "Jr.":
        last_name = faculty_member.split()[-2] 
    search_url = "https://" + "arxiv.org/find/all/1/au:+" + last_name.encode('utf-8') + "_" + first_name.encode('utf-8') + "/0/1/0/all/0/1"
    req = urllib2.Request(search_url, headers={'User-Agent' : 'Magic Browser'})
    author_page = urllib2.urlopen(req)
    html = BeautifulSoup(author_page, 'html.parser')
    paper_rows = html.find_all('a', attrs = {'title':'Abstract'})
    paper_number = 1
    for paper in paper_rows:
        identifier = paper.getText()[6:]
        abstract_url = "https://arxiv.org/abs/" + identifier
        abstract_req = urllib2.Request(abstract_url, headers={'User-Agent' : 'Magic Browser'})
        abstract_page = urllib2.urlopen(abstract_req)
        abstract_html = BeautifulSoup(abstract_page, 'html.parser')
        description = abstract_html.find('blockquote', attrs = {'class':'abstract mathjax'}).getText()
        title = abstract_html.find('h1', attrs = {'class': 'title mathjax'}).getText()
        with open(last_name.encode('utf-8')+"_"+first_name.encode('utf-8')+"_"+str(paper_number) +".txt", 'w') as text_file:
            text_file.write(title.encode('utf-8') + description.encode('utf-8'))
        paper_number = paper_number + 1
    