import xmltodict #pip3 install xmltodict
import os

class xml:
    def __init__(self):
        self.file = ""
        self.branches = None
        
class br:
    def __init__(self):
        self.vector = None
        self.b = None
        
#del(xmls)
xmls = set()

def flattener(root, branch, branches):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if isinstance(root, list):
        for item in root:
            flattener(item, branch, branches)
            
    elif isinstance(root, str):
        branch.append(''.join(filter(whitelist.__contains__, root)).lower())
        b = br()
        b.b = list(branch)
        branches.append(b)
        branch.pop()
    
    elif root is None:
        root = None
        
    else:
        for key, item in root.items():
            branch.append(key.lower())
            flattener(item, branch, branches)
            branch.pop()
    return branches


path = '/Users/leonardomoya/Dropbox/recuperacion/shaks200'
for filename in os.listdir(path):
    if filename.endswith('.xml'):
        fullname = os.path.join(path, filename)
        with open(fullname) as fd:
            docs = xmltodict.parse(fd.read())
            temp = xml()
            temp.file = filename
            temp.branches = list()
            flattener(docs, list(), temp.branches)
            xmls.add(temp)
        
        
def compare(branch, path):
    path = path.lower().split("/")
    if path[len(path)-1] in branch[len(branch)-1]:
        if [x for x in branch[0:len(branch)-1] if x in path[0:len(path)-1]] == path[0:len(path)-1]:
            return (len(path)+1)/(len(branch)+1)
    return 0

class token:
    def __init__(self):
        self.docs = set()
        self.word = ""
        
class doc:
    def __init__(self):
        self.words = set()
        self.file = ""
     
invIndex = set()


def initInv():
    
    docs = set()
    
    for xml in xmls:
        d = doc()
        d.file = xml.file
        for branch in xml.branches: 
            tmp = branch.b[len(branch.b)-1].split()
            for j in tmp:
                w = token()
                w.word = j
                invIndex.add(w)
                d.words.add(j)
        docs.add(d)
    counter =0
    for t in invIndex:
        counter+= 1
        for d in docs:
            for w in d.words:
                if w == t.word:
                    t.docs.add(d.file)
                    print("added ", w, " to ", d.file, counter/len(invIndex))
                      
initInv()

class coef:
    def __init__(self):
        self.num = 0
        self.word = ""
        
coefs = set()

def initCoef():
    for w in initInv:
        c = coef()
        n = len(w.docs)
        N = len(xmls)
        c.word = w.word
        c.num = math.log10(N/n)
        coefs.add(c)
    del(invIndex)

initCoef()

vectors = set()

def initVecs():
    
    for xml in xmls:
        for branch in xml.branches:
            vec = set()
            words = branch.b[len(branch.b)-1].split()
            wordCount = {x:words.count(x) for x in words}
            Words, WordsCounter = wordCount.keys(), wordCount.values()
            for w, count in zip(Words, WordsCounter):
                for c in coefs:
                    if c.word == w:
                        newCoef = coef()
                        newCoef.word = w
                        newCoef.num = c.num * float(count)
                        branch.vector.add(newCoef)


initVecs()

def vectorizeQuey(string):
    vec = set()
    strings = string.lower().split("/")
    for word in strings:
            for c in coefs:
                if c.word == word:
                    vec.coefs.add(c)
    return vec


class result:
    def __init__(self):
        self.doc = ""
        self.num = 0


def simNoMerge(query):
    results = []
    queryVec = vectorizeQuey(query)
    for xml in xmls:
        score = 0
        summatorySqrt = 0
        for branch in xml.branches:
            cr = compare(branch.b, query)
            summatory = 0
            for c1 in queryVec:
                for c2 in branch.vector:
                    if c1.word == c2.word:
                        summatory += c1.num * c2.num
                        summatorySqrt += c2.num ** 2
            score += cr * summatory
        r = result()
        r.doc = xml.file
        r.num = score/(summatorySqrt ** (1/2))
        results.append(r)
    results.sort(key=lambda x: x.num, reverse=True)
    return results

simNoMerge("play/title/cleopatra")    