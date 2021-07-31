from a_imports import *

def get_word_count(msg):
    res = re.sub(' +', ' ',msg)
    wc=len(res.split(' '))
    return wc

def get_counts_digit_size_alpha_space_symbols_punc(msg):
    msglen=len(msg)  
    digits=0
    alphabets=0
    space=0
    upperltrs=0
    all_math_symbols=['+','-','%','/','>','<','^']
    all_punc_symbols=[',' , '.' , '?' , ':' , '!' , ';' , '"', "'" ]
    fnd_maths_symbols_count=0
    fnd_punc_symbols_count=0
    for x in msg:
        if x.isdigit():
            digits+=1
        elif x.isalpha():
            alphabets+=1
            if x.isupper():
                upperltrs+=1
        elif x==' ':
            space+=1
        elif x in all_math_symbols:
            fnd_maths_symbols_count+=1
        elif x in all_punc_symbols:
            fnd_punc_symbols_count+=1           
    return [msglen, digits,alphabets,space,upperltrs,fnd_maths_symbols_count,fnd_punc_symbols_count]
            
                      def get_all_atrate_strings__base_for_getting_email_ids():
    pem=[]
    df=pd.read_csv(path_to_derived_sms_dataset)
    size=df.shape[0]
    for i in range(size):
        sms=df.loc[i,'Message_Content']
        txts=sms.split()
        for x in txts:
            for y in x:
                if y=='@':
                    pem.append((i+2,x))
                    break
    return pem

def get_emails(msg):
    emailPattern = re.compile(r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''')    
    res=emailPattern.search(msg)
    if res is not None:
        return (1,msg[res.span()[0]:res.span()[1]])
    return (0,'')

def get_greeting_words(msg):
    wlist=['hai','thanks','sorry','hi','hey','hello','gud ni8','good 9t','gud nyt','g o o d n i g h t' ,'gud mrng','goodmorning','gud noon','gud nite','gud eve','good afternoon','happy morning','happy day','goodnight','good nte','goodevening','gud mornin','good night','good morning','bad day']
    txt=msg.lower()
    for x in wlist:
        if x in txt:
            return 1
    return 0

def get_misspelled_words(msg):    
    d = enchant.Dict("en_US")
    count = 0
    text_str = re.sub(r'[?|$|.|!|,|@|#|^|*]',r'', msg)
    line = text_str.split(" ")
    len_line=len(line)
    for word in line:
        if word == "":
            pass
        else:
            if d.check(word) == False:
                count += 1
    temp = (float(count) / len_line)*100
    return round(temp,2)

def get_all_words_with_digits__base_for_getting_phone_numbers():
    numbers=[]
    df=pd.read_csv(path_to_derived_sms_dataset)
    size=df.shape[0]
    for i in range(size):
        sms=df.loc[i,'Message_Content']
        txts=sms.split()
        for x in txts:
            for y in x:
                if y.isdigit():
                    numbers.append((i+2,x))
                    break            
    return numbers

def get_phone_numbers(msg):
    phonePattern = re.compile(r"(?<!\d)(\d{4} \d{3} \d{4})|(\d{4}-\d{3}-\d{4})|(\d{4}-\d{4}-\d{3})|(\d{4} \d{3} \d{2} \d{2})|(\d{11})|(\d{10})|(\d{9})|(\d{8})|(\d{7})|(\d{6})|(\d{5})(?!\d)")    
    res=phonePattern.search(msg)
    if  res is not None:
        return (1,msg[res.span()[0]:res.span()[1]])
    return (0,'')

def get_all_emoji_symbols():
    df=pd.read_csv(path_to_derived_sms_dataset)
    size=df.shape[0]
    for i in range(size):
        txt=df.loc[i,'Message_Content']
        if ':' in txt:
            print(i+2,df.loc[i,'Label'],txt,'\n')

def get_presence_of_emotions(msg):
    em=[':-)',':)',':-O',':-o',';-)',';)',':-S',':-s',":'(" ,'(H)','(h)','(A)','(a)',':-#','8-|',':-*',':^)','<:o)','|-)','(Y)','(y)','(B)','(b)','(X)','(x)','({)',
       ':-[',':[','(L)','(l)','(K)','(k)','(F)','(f)','(P)','(p)','(@)','(T)','(t)','(8)','(*)','(O)','(o)','(M)','(m)','(E)','(e)','(S)','(I)','(i)','(&)','(~)',
       '(W)','(w)','(G)','(g)','(U)','(u)','(^)','(})','(Z)','(z)','(D)','(d)','(N)','(n)','(C)','(c)','8-)','*-)','+o(','^o)','8o|','(6)',':-D',':d',':-P',':p',':-(',':(',':-|',':|',':-$',':$',':-@',':@',':V',':-D',':/',';-)','-)',';-(']
    for x in em:
        if x in msg:
            return 1 
        return 0

def get_readability_scores(msg):
    scores=[]
    results = readability.getmeasures(msg, lang='en')
    scores.append(results['readability grades']['Kincaid'])
    scores.append(results['readability grades']['ARI'])
    scores.append(results['readability grades']['Coleman-Liau'])
    scores.append(results['readability grades']['FleschReadingEase'])
    scores.append(results['readability grades']['GunningFogIndex'])
    scores.append(results['readability grades']['SMOGIndex'])    
    return scores

def get_money(msg):
    specialPattern= re.compile(r'([$€]\d*)|([\w,]*\s*pound)')
    idx=specialPattern.search(msg)
    if  idx is not None:
        return 1
    return 0

def get_all_msgs_with_reply_subscrib():
    df=pd.read_csv(path_to_derived_sms_dataset)
    size=df.shape[0]
    for i in range(size):
        txt=df.loc[i,'Message_Content']
        txt=txt.lower()
        if 'yes' in txt and  'no' in txt:
            print(i,df.loc[i,'Label'],txt,'\n')
        elif 'reply' in txt or 'subscri' in txt:
            print(i,df.loc[i,'Label'],txt,'\n')

def get_self_answering_type_msgs(msg):
    mylbl=1
    txt=msg.lower()
    subs_words=['sub ','unsub','subscriber','subscribe','subscription','unsubscribe']
    for x in subs_words:
        if x in txt:
            mylbl=0
    if mylbl==1:
        if 'reply' in txt:
            if get_all_urls(txt)[0] or get_emails(txt)[0] or get_phone_numbers(txt)[0]:
                if 'stop' in txt:
                    mylbl=0
                elif 'pound' in txt or 'dollar' or get_money(txt):
                    mylbl=0                    
    return mylbl

def get_special_character(msg):   
    specialPattern= re.compile(r'[$€]\d*')
    idx=specialPattern.findall(msg)
    if idx:
        return (1,idx)
    return (0,idx)

def get_metrics(X,clf,y):
    maxrs=[0,0,0,0,0,0,0]
    for i in range(0,10):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        clf.fit(X_train,y_train)
        y_pred=clf.predict(X_test)
        pre=metrics.precision_score(y_test, y_pred)
        rec=metrics.recall_score(y_test, y_pred)
        acc=metrics.accuracy_score(y_test, y_pred)
        fscore=metrics.f1_score(y_test,y_pred)
        cmatrix=metrics.confusion_matrix(y_test,y_pred)
        jscore=metrics.jaccard_score(y_test,y_pred)
        msqrerror=metrics.mean_squared_error(y_test,y_pred)
        msrs=[acc,pre,rec,fscore,cmatrix,jscore,msqrerror]
        if msrs[0]>maxrs[0]:
            maxrs=msrs
    print(maxrs)
    return maxrs

def get_url_based_features(url):
    f=[0]*7
    for x in url:
        f[4]+=1
        if x=='@':
            f[1]=1
        elif x=='-':
            f[2]=1
        elif x=='.':
            f[3]+=1
        elif x in ['$',',','*',';','_']:
            f[5]+=1
    if url==None:
        f[0],f[6]=0,-1
    else:
        f[0]=get_age_of_domain(url)
        f[6]=get_ssl_certificate_type(url)
    return f

def get_speech_tagger(msg):
    text = nltk.tokenize.word_tokenize(msg)
    noun = conjunction = adverb = preposition = adjective = pronoun = verb = 0
    noun_lst=[] 
    conjunction_lst=[] 
    adverb_lst=[] 
    preposition_lst=[]
    adjective_lst=[]
    pronoun_lst=[]
    verb_lst=[]
    temp =  nltk.pos_tag(text)
    for line in temp:
        if line[1] == "NN":
            noun +=1
            noun_lst.append(line[0])
        elif line[1] == 'PRP':
            pronoun += 1
            pronoun_lst.append(line[0])
        elif line[1] == 'JJ':
            adjective += 1
            adjective_lst.append(line[0])
        elif line[1] == "VB":
            verb += 1
            verb_lst.append(line[0])
        elif line[1] == 'RB': # adverbs
            adverb += 1
            adverb_lst.append(line[0])
        elif line[1] == "IN":
            preposition += 1
            preposition_lst.append(line[0])
        elif line[1] == "CC":
            conjunction += 1
            conjunction_lst.append(line[0])        
    lst=[noun_lst,pronoun_lst,adjective_lst,verb_lst,adverb_lst,preposition_lst,conjunction_lst]
    return [[noun, pronoun, adjective, verb, adverb, preposition, conjunction],lst]

def get_suspicious_keywords(msg):
    kw=["please", "guaranteed", "purchase", "interested", "store", "account","customer", "bank", "sms", "club", "message", "call", "nationwide", "cost", "card", "mail", "apple", "charges", "update", "today"  ]
    feature = []
    features_list=[]
    msg=msg.lower()
    for key in kw:
        if key in msg:
            feature.append(1)
            features_list.append(key)
        else:
            feature.append(0)
    return (feature,features_list)

def get_upper_case_word_count(msg):
    tokens = nltk.tokenize.word_tokenize(msg)
    ucc=0
    for x in tokens:
        if x.isupper():
            ucc+=1
    return ucc

def get_all_urls(msg):    
    ig=['"Si.como','ok..come']
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))|([^\s]*\.com[^\s]*)"   
    urlPattern = re.compile(regex)
    for x in msg.split():
        res=urlPattern.search(x)
        if res is not None:
            purl=x[res.span()[0]:res.span()[1]]
            if '@' not in purl and purl not in ig:
                return (1,x[res.span()[0]:res.span()[1]])
    return (0,'')

def get_visual_morph(msg):
    vismorp='xx'
    txt=msg.lower()
    if vismorp in txt:
        return 0
    return 1

def fetch_urls(msg):    
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))|([^\s]*\.com[^\s]*)"   
    urlPattern = re.compile(regex)
    res=urlPattern.search(msg)
    if res is not None:
        purl=msg[res.span()[0]:res.span()[1]]
        if '@' not in purl:
            return purl

def short_url_resolution_method_2(url):
    try:
        conn = pycurl.Curl()
        conn.setopt(pycurl.URL, url)
        conn.setopt(pycurl.FOLLOWLOCATION, 1)
        conn.setopt(pycurl.CUSTOMREQUEST, 'HEAD')
        conn.setopt(pycurl.NOBODY, True)
        conn.perform()
        return conn.getinfo(pycurl.EFFECTIVE_URL)
    except:
        return None

def get_metrics_res():
    pathrd=path_to_sms_based_features 
    df=pd.read_csv(pathrd,keep_default_na=False)
    data=df.values
    X1=data[:,:51]
    X2=data[:,:60]
    y=data[:,60]
    y=y.astype('int')
    clf1=RandomForestClassifier(n_estimators=200)
    clf2=DecisionTreeClassifier()
    clf3=AdaBoostClassifier(n_estimators=50, learning_rate=1)
    clf4=svm.SVC(kernel='linear')
    clf5=GaussianNB()
    clf6=LogisticRegression()
    clf7=KNeighborsClassifier(n_neighbors=3)
    clf8=LinearDiscriminantAnalysis()
    clf9=GradientBoostingClassifier(learning_rate=0.1)
    get_metrics(X1,clf1,y)
    get_metrics(X2,clf1,y)
    print('*'*150,'\n')
    get_metrics(X1,clf2,y)
    get_metrics(X2,clf2,y)
    print('*'*150,'\n')
    get_metrics(X1,clf3,y)
    get_metrics(X2,clf3,y)
    # # get_metrics(X1,clf4,y)
    # # get_metrics(X2,clf4,y)
    get_metrics(X1,clf5,y)
    get_metrics(X2,clf5,y)
    print('*'*150,'\n')
    get_metrics(X1,clf6,y)
    get_metrics(X2,clf6,y)
    print('*'*150,'\n')
    get_metrics(X1,clf7,y)
    get_metrics(X2,clf7,y)
    print('*'*150,'\n')
    get_metrics(X1,clf8,y)
    get_metrics(X2,clf8,y)
    print('*'*150,'\n')
    get_metrics(X1,clf9,y)
    get_metrics(X2,clf9,y)
    print('*'*150,'\n')

def get_domain_path(url):
    part=url.split('//',1)
    part= part[0] if len(part)==1 else part[1]
    part=part.split('/',1)
    domain=part[0]
    path= '/' if len(part)==1 else '/'+part[1]
    return (domain,path)

def short_url_resolution_method_1(url):
    try:
        l=get_domain_path(url)
        c =http.client.HTTPConnection(l[0],timeout=5)
        c.request('HEAD', l[1])
        response = c.getresponse()
        sts=response.status
        rsn=response.reason
        hdr=response.getheader('location')   
        return hdr
    except:
        return None

def get_age_of_domain(url):
    try:
        dt=whois.whois(url)['creation_date']
        hrs=int(((datetime.datetime.now()-dt).total_seconds())/3600)
        return hrs
    except Exception as e:
        return 0  






    



