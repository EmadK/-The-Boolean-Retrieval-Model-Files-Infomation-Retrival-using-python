def postings(w , listofalldata,listofpaths):
    temp = []
    c = -1
    for i in listofalldata:
        c= c+1
        if w in i:
            temp.append(listofpaths[c])
        else:
            continue
    
    return temp


def cleannig(pefore , pre):       #لحذف حروف الجر الموجوده ف لليست برى من الليست بيفور 
    temp = []
    flag= False               # will be true if there is prepositions was deleted
    for i in pefore:
        x = False
        if i not in pre:
            x = True
        else:
            x = False

        if x == True:
            temp.append(i)
            flag = True
    res = set(temp)
    return flag, res


def readDoc(path):
    f = open(path, 'r') # by default the mode is read-only
    doclines = ""
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        else:
            doclines = doclines + line
    f.close()
    return doclines


#print(readDoc("doc1.txt"))

listofpaths = ["doc1.txt","doc2.txt","doc3.txt","doc4.txt"]

def readAlldoc(setofpaths):
    listofalldata = []
    listofalldata2 = []
    
    for p in setofpaths:
        listofalldata.append(readDoc(p).split())
        listofalldata2 = listofalldata2 + readDoc(p).split()
 
    return listofalldata,sorted(set(listofalldata2))

#print(readAlldoc(listofpaths))
listofalldata,listofalldata2 = readAlldoc(listofpaths)
#print(listofalldata,"\n")

#print(listofalldata2)

def madeDic(listofalldata,listofallDa2):
    d1 = {}.fromkeys(listofallDa2)
    for k in d1.keys():  # to make the inverted index 
        d1[k] = postings(k,listofalldata,listofpaths)
    return d1

invertedindexDic = madeDic(listofalldata,listofalldata2)
terms = invertedindexDic.keys()

def itemIndex(list1,item):
    listofindex =[] 
    counter = 0
    for x in list1:
        if item == x:
            listofindex.append(counter)
            counter = counter +1
        else:
            counter = counter +1
    return listofindex

#print(itemIndex(listofalldata[0],'ahmed'))          

def makePositionalindex(invertedindexdic):              # add position of every term in every document for Phrase queries 
     terms = invertedindexdic.keys()
     postings = invertedindexdic.values()
     termIndex = -1

     for x in postings:
         termIndex = termIndex+1
         d2 = {}.fromkeys(x)
         for d in x:
             temp = []
             data = readDoc(d).split()
             temp = itemIndex(data,list(terms)[termIndex])
             d2[d] = temp
         
         invertedindexdic[list(terms)[termIndex]] = d2
         
     return invertedindexdic

         
positionalDic = makePositionalindex(invertedindexDic) 


#print( madeDic(listofalldata,listofalldata2))

pre =["and","are","to","is","with"]
pre2=["and","or","not"]

#d1 ="emad and ahmed are going to play football with ahmed"
#d2 ="ahmed is going to school"
#d3 ="hassan  or ahmed not gode boy"
#d4 ="maher and emad and ahmed is cowboy"
#listofDoc = {1,2,3,4} 
#l1= d1.split()
#l2= d2.split()
#l3= d3.split()
#l4= d4.split()
#lf=[]
#lf.append(l1)
#lf.append(l2)
#lf.append(l3)
#lf.append(l4)
#print(len(lf))
#lf2 = l1 +l2 +l3+ l4
#s1 = set(lf2)
#lf2 = sorted(list(s1))

#d1 = {}.fromkeys(lf2)

#for k in d1.keys():  # to make the inverted index 
#    d1[k] = postings(k,lf)
    

query = input('Enter your query: ')

def Relatedpostings(q , dic, pre):
    temp = []
    q= q.lower().split()
    f, ql= cleannig(q, pre)
    #print(ql)
    for x in ql:
        print(x)
        if x in dic.keys():   #or (str(x) != "and" or str(x) != "or"):
            temp.append(dic[x])
        else:
            continue
    return f, q, temp


def processQuery(q, dic, pre,temp):
    f, q, postings = Relatedpostings(q,dic,pre)
    c = 0
    for x in postings:
        postings[c]= set(x)
        c = c+1       
    if f == True:        #to make the AND, OR, Not operations 
        if q[1] == "and":
            for p in postings:
                print(p)
                temp = set(temp) & p 
        elif q[1] == "or":
            for p in postings:
                print(p)
                temp = set(temp).union(p)   
        elif q[0] == "not":
            for p in postings:
                print(p)
                temp = set(temp) - p
            
    else:
        print("sorry! Your query doesnot have boolean operator or not homogenous")
        
    
    return temp, len(temp)

print(processQuery(query,invertedindexDic,pre2,listofpaths))

def Relatedpostings2(q , dic):
    temp = []
    q= q.lower().split()
    for x in q:
        print(x)
        if x in dic.keys():   #or (str(x) != "and" or str(x) != "or"):
            temp.append(dic[x])
        else:
            continue
    return temp


#query2 = input('Enter your phrase query: ')

def processQuery2(query,dic):
    termsOfquery = query.split()
    postings = Relatedpostings2(query,dic)
    
    for x in termsOfquery:
        for p in postings:
            print(p.keys())
            break
                
    
    
    
#processQuery2(query2,positionalDic)
    

def longandShortPostList(dic):
    #postings = dic.values()
    longest =  0
    shortest = 4
    #index
    for x in dic.keys():
        xlen = len(dic[x])
        if  xlen > longest:
            longest = xlen
        elif xlen < shortest:
            shortest = xlen
            
            
    return longest,shortest
        
print("longest , shortest post list",longandShortPostList(invertedindexDic))       




from PorterStemmer import PorterStemmer

def porterStem(dic):
    p = PorterStemmer() 
    for w in dic.keys():
        print(p.stem(w))

#porterStem(invertedindexDic)

#query = input('Enter your query: ')
#def phraseQueries(query):
    




   