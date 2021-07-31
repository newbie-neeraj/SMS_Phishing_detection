from a_imports import *







def has_IP_address(url):
    x=re.findall(IP_ADDRESS_AS_DOMAIN_SEARCH_PATTERN_1,url)
    y=re.findall(IP_ADDRESS_AS_DOMAIN_SEARCH_PATTERN_2,url)
    if x:
        return x
    if y:
        return y

def get_hostname(url):
    if (len(url)>=7 and url[0:7]=='http://')  or (len(url)>=8 and url[0:8]=='https://'):   
        wopurl=url.split('//',1)[1]
    else:
        wopurl=url    
    hname=wopurl.split('/',1)[0]
    ip=has_IP_address(hname)
    if ip!=None:
        hname=hname[0][2:-1]  if hname[0][-1]=='/' else hname[0][2:]
        return hname
    if hname in shortening_providers:
        return wopurl
    return hname

def intialize_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    if not path.exists(path_to_blacklist_urls):
        pd.DataFrame(columns=['Url']).to_csv(path_to_blacklist_urls,index=False)
    if not path.exists(path_to_blacklist_emailid):
        pd.DataFrame(columns=['Emails']).to_csv(path_to_blacklist_emailid,index=False)
    if not path.exists(path_to_blacklist_phone):
        pd.DataFrame(columns=['Phone number']).to_csv(path_to_blacklist_phone,index=False)    
    df=pd.read_csv(path_to_blacklist_urls,keep_default_na=False)
    for i in range(df.shape[0]):
        url_blacklist.add(df.loc[i,'Url'])
    df=pd.read_csv(path_to_blacklist_emailid,keep_default_na=False)
    for i in range(df.shape[0]):
        email_blacklist.add(df.loc[i,'Emails'])
    df=pd.read_csv(path_to_blacklist_phone,keep_default_na=False)
    for i in range(df.shape[0]):
        phone_blacklist.add(df.loc[i,'Phone number'])

def add_email_to_blacklist(email):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    email_blacklist.add(email)

def add_url_to_blacklist(url):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    url_blacklist.add(url)

def add_phone_to_blacklist(phone):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    phone_blacklist.add(phone)

def remove_email_from_blacklist(email):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    if email in email_blacklist:
        email_blacklist.remove(email)

def remove_url_from_blacklist(url):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    if url in url_blacklist:
        url_blacklist.remove(url)

def remove_phone_from_blacklist(phone):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    if phone in phone_blacklist:
        phone_blacklist.remove(phone)

def show_email_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    return list(email_blacklist)

def show_url_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    return list(url_blacklist)

def show_phone_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    return list(phone_blacklist)

shortening_providers=[ 'goo.gl','bit.ly','rb.gy','l.linklyhq.com','cutt.ly', 'soo.gd','tinyurl.com','shorturl.at','is.gd','bit.do','ow.ly','buff.ly','demo.polr.me','t2m.io','hypr.ink','b.link','yourls.org']

def clear_email_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    email_blacklist.clear()

def clear_url_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    url_blacklist.clear()

def clear_phone_blacklist():
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    phone_blacklist.clear()

def save_and_close_blacklists(option):
    global url_blacklist
    global email_blacklist
    global phone_blacklist
    if option==1:
        df=pd.DataFrame(columns=['Url'])
        df['Url']=list(url_blacklist)
        df.to_csv(path_to_blacklist_urls,index=False)
    elif option==2:
        df=pd.DataFrame(columns=['Emails'])
        df['Emails']=list(email_blacklist)
        df.to_csv(path_to_blacklist_emailid,index=False)
    elif option==3:
        df=pd.DataFrame(columns=['Phone number'])
        df['Phone number']=list(phone_blacklist)
        df.to_csv(path_to_blacklist_phone,index=False)
        
def intialize_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    if not path.exists(path_to_whitelist_urls):
        pd.DataFrame(columns=['Url']).to_csv(path_to_whitelist_urls,index=False)
    if not path.exists(path_to_whitelist_emailid):
        pd.DataFrame(columns=['Emails']).to_csv(path_to_whitelist_emailid,index=False)
    if not path.exists(path_to_whitelist_phone):
        pd.DataFrame(columns=['Phone number']).to_csv(path_to_whitelist_phone,index=False)    
    df=pd.read_csv(path_to_whitelist_urls,keep_default_na=False)
    for i in range(df.shape[0]):
        url_whitelist.add(df.loc[i,'Url'])
    df=pd.read_csv(path_to_whitelist_emailid,keep_default_na=False)
    for i in range(df.shape[0]):
        email_whitelist.add(df.loc[i,'Emails'])
    df=pd.read_csv(path_to_whitelist_phone,keep_default_na=False)
    for i in range(df.shape[0]):
        phone_whitelist.add(df.loc[i,'Phone number'])

# intialize_whitelist()

def add_email_to_whitelist(email):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    email_whitelist.add(email)

def add_url_to_whitelist(url):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    url_whitelist.add(url)

def add_phone_to_whitelist(phone):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    phone_whitelist.add(phone)

def remove_email_from_whitelist(email):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    if email in email_whitelist:
        email_whitelist.remove(email)

def remove_url_from_whitelist(url):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    if url in url_whitelist:
        url_whitelist.remove(url)

def remove_phone_from_whitelist(phone):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    if phone in phone_whitelist:
        phone_whitelist.remove(phone)

def show_email_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    return list(email_whitelist)

def show_url_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    return list(url_whitelist)

def show_phone_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    return list(phone_whitelist)

def clear_email_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    email_whitelist.clear()

def clear_url_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    url_whitelist.clear()

def clear_phone_whitelist():
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    phone_whitelist.clear()

def save_and_close_whitelists(option):
    global url_whitelist
    global email_whitelist
    global phone_whitelist
    if option==1:
        df=pd.DataFrame(columns=['Url'])
        df['Url']=list(url_whitelist)
        df.to_csv(path_to_whitelist_urls,index=False)
    elif option==2:
        df=pd.DataFrame(columns=['Emails'])
        df['Emails']=list(email_whitelist)
        df.to_csv(path_to_whitelist_emailid,index=False)
    elif option==3:
        df=pd.DataFrame(columns=['Phone number'])
        df['Phone number']=list(phone_whitelist)
        df.to_csv(path_to_whitelist_phone,index=False)
        
def is_url_and_domain_matches(action,url):
    regex=r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))|([^\s]*\.com[^\s]*)"   
    urlPattern = re.compile(regex)
    res=urlPattern.search(action)
    if res is not None:
        purl=action[res.span()[0]:res.span()[1]]
        if '@' not in purl:
            domain_from_action=purl.split("//",1)
            domain_from_msg=url.split("//",1)
            domain_from_action=(domain_from_action[0].split('/',1)[0] if len(domain_from_action)==1 else domain_from_action[1].split('/',1)[0]).split('.')
            domain_from_msg=(domain_from_msg[0].split('/',1)[0] if len(domain_from_msg)==1 else domain_from_msg[1].split('/',1)[0]).split('.')
            if len(domain_from_action)>1:
                if domain_from_action[0]=='www'   or domain_from_action[0]=='identity':
                    domain_from_action=domain_from_action[1]
                else:
                    domain_from_action=domain_from_action[0]
            if len(domain_from_msg)>1:
                if domain_from_msg[0]=='www' or domain_from_msg[0]=='identity':
                    domain_from_msg=domain_from_msg[1]
                else: 
                    domain_from_msg=domain_from_msg[0]
            if domain_from_action==domain_from_msg:
                return 1
    return 0
            
def source_code_analyzer(url):
    match=1
    if url!='':
        try:
            respo = requests.get(url).text
            soup = BeautifulSoup(respo,'html.parser')
            hform=soup.find_all('form')
            if len(hform)!=0:
                for i in range(len(hform)):
                    action=hform[i].attrs.get('action').lower()
                    match=is_url_and_domain_matches(action,url)
                    if not match:
                        return match
                #********************************** optional part 2****************************************
    #             for i in range(len(hform)):
    #                 action=hform[i].attrs.get('action').lower()
    #                 details=dict()
    #                 action=hform[i].attrs.get('action').lower()
    #                 method=hform[i].attrs.get("method", "get").lower()
    #                 inputs=[]
    #                 for input_tag in hform[i].find_all("input"):
    #                     input_type = input_tag.attrs.get("type", "text")
    #                     input_name = input_tag.attrs.get("name")
    #                     input_value =input_tag.attrs.get("value", "")
    #                     inputs.append({"type": input_type, "name": input_name, "value": input_value})  
    #                 details["inputs"] = inputs
    #                 details["method"] = method
    #                 details["action"] = action
        except:
            pass
    return match

phishtank_blacklist=set()
alexa_whielist=set()
url_blacklist=set()
email_blacklist=set()
phone_blacklist=set()
url_whitelist=set()
email_whitelist=set()
phone_whitelist=set()




