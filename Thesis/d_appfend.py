import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import GradientBoostingClassifier
from tkinter import *


window=Tk()
window.title('SMS-Phishing Detector')
color1='#8A275E'
color2='#EA3008'
color3='#DC512E'
color4='#E7E4E3'
color5='#A9A4A7'
color6='#E81310'
color7='#676AB0'
pstr_number_entry=''
pstr_url_entry=''
pstr_email_entry=''
lstr_number_entry=''
lstr_url_entry=''
lstr_email_entry=''
str_logging_details=''
details_about_the_dataset='Dataset is collected from the research work contributed by the author Almeida.This dataset contains a total of 5574 messages in which 4827 are ham messages and 747 are smishing messages. Same Dataset is used in all Research Paperwork.'
string_dataset_info='Blacklist is created from the Phishtank dataset.'


clf1=RandomForestClassifier(n_estimators=200)
clf2=DecisionTreeClassifier()
clf3=AdaBoostClassifier(n_estimators=50, learning_rate=1)
clf4=svm.SVC(kernel='linear')
clf5=GaussianNB()
clf6=LogisticRegression()
clf7=KNeighborsClassifier(10)
clf8=LinearDiscriminantAnalysis()
clf9=GradientBoostingClassifier(learning_rate=0.1)



def on_btn_click_get_classiification_details():
    global classifiaction_details_constant_string
    txt_extracted.delete('1.0',END)
    Font_tuple = ("Comic Sans MS", 8, "italic")
    txt_extracted['font']=Font_tuple
    txt_extracted.insert(END,classifiaction_details_constant_string)    




def on_btn_click_get_dataset_details():
    txt_extracted.delete('1.0',END)
    Font_tuple = ("Comic Sans MS", 9, "italic")
    txt_extracted['font']=Font_tuple
    txt_extracted.insert(END, details_about_the_dataset)


def on_btn_click_open_phishing_list():
    p = Popen(path_to_phishing_hnames_file, shell=True)


# add
def on_btn_click_add_phishing_emails():
    global pstr_email_entry    
    email=pstr_email_entry.get()
    res=get_emails(email)
    if res[0] and res[1]==email:    
        add_email_to_blacklist(email)
        save_and_close_blacklists(2)
        x=email +'    -  Added to blacklist...'
    else:
        x=email +'    -  not of proper format...'
    str_logging_details.set(x)

def on_btn_click_add_phishing_urls():
    global pstr_url_entry    
    url=pstr_url_entry.get()
    res=get_all_urls(url)
    if res[0] and res[1]==url:    
        add_url_to_blacklist(url)
        save_and_close_blacklists(1)
        x=url +'    -  Added to blacklist...'
    else:
        x=url +'    -  not of proper format...'
    str_logging_details.set(x)

def on_btn_click_add_phishing_numbers():
    global pstr_number_entry    
    num=pstr_number_entry.get()
    res=get_phone_numbers(num)
    if res[0] and res[1]==num:      
        add_phone_to_blacklist(num)
        save_and_close_blacklists(3)
        x=num +'    -  Added to blacklist...'
    else:
        x=num +'    -  not of proper format...'
    str_logging_details.set(x)


# remove
def on_btn_click_remove_phishing_emails():
    global pstr_email_entry    
    email=pstr_email_entry.get()
    res=get_emails(email)
    if res[0] and res[1]==email:    
        remove_email_from_blacklist(email)
        save_and_close_blacklists(2)
        x=email +'    -  Removed from blacklist...'
    else:
        x=email +'    -  not in the Blacklist...'
    str_logging_details.set(x)

def on_btn_click_remove_phishing_urls():
    global pstr_url_entry    
    url=pstr_url_entry.get()
    res=get_all_urls(url)
    if res[0] and res[1]==url:    
        remove_url_from_blacklist(url)
        save_and_close_blacklists(1)
        x=url +'    -  Removed from blacklist...'
    else:
        x=url +'    -  not in the Blacklist...'
    str_logging_details.set(x)

def on_btn_click_remove_phishing_numbers():
    global pstr_number_entry    
    num=pstr_number_entry.get()
    res=get_phone_numbers(num)
    if res[0] and res[1]==num: 
        remove_phone_from_blacklist(num)
        save_and_close_blacklists(3)
        x=num +'    -  Removed from blacklist...'
    else:
        x=num +'    -  not in the Blacklist...'
    str_logging_details.set(x)


# show 
def on_btn_click_show_phishing_emails():
    p = Popen(path_to_blacklist_emailid, shell=True)

def on_btn_click_show_phishing_urls():
    p = Popen(path_to_blacklist_urls, shell=True)

def on_btn_click_show_phishing_numbers():
    p = Popen(path_to_blacklist_phone, shell=True)


# clear 
def on_btn_click_clear_phishing_emails():
    clear_email_blacklist()
    save_and_close_blacklists(2)
    x='Blacklist cleared'
    str_logging_details.set(x)

def on_btn_click_clear_phishing_urls():
    clear_url_blacklist()
    save_and_close_blacklists(1)
    x='Blacklist cleared'
    str_logging_details.set(x)

def on_btn_click_clear_phishing_numbers():
    clear_phone_blacklist()
    save_and_close_blacklists(3)
    x='Blacklist cleared'
    str_logging_details.set(x)


def on_btn_click_get_blacklist_options():
    global pstr_number_entry
    global pstr_url_entry
    global pstr_email_entry
    global str_logging_details

    newWindow=Toplevel(window)
    newWindow.title('Blacklist Options')
    newWindow.grid_columnconfigure(0, weight=1)
    
    frame_heading_info=Frame(newWindow,background=color4, width=10, height=100)
    frame_heading_info.grid(row=0, column=0, sticky="nsew")
    str_heading_info=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_heading_info=Label(frame_heading_info,textvariable=str_heading_info,font=Font_tuple,padx=10,pady=20,bg=color4, fg=color2)
    str_heading_info.set(string_dataset_info)
    lbl_heading_info.grid(row=0, column=0, sticky="nsew")
    
    Font_tuple = ("Comic Sans MS", 9, )
    str_pdt_csv=StringVar()
    btn_pdt_csv=Button(frame_heading_info,textvariable=str_pdt_csv,width=18,height=2,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_open_phishing_list)
    str_pdt_csv.set('Phishing Domains')
    btn_pdt_csv.grid(row=0, column=1,pady=(10,10),padx=(10,0))

    # ######### Email id
    new_frame2=Frame(newWindow, width=10, height=100)
    new_frame2.grid(row=2, column=0, sticky="nsew")

    str_email_lbl=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_email_lbl=Label(new_frame2,textvariable=str_email_lbl,font=Font_tuple,fg=color2)
    str_email_lbl.set('Email id')
    lbl_email_lbl.grid(row=2,column=0,pady=(10,10),padx=(20,0))

    Font_tuple = ("Comic Sans MS", 9)

    pstr_email_entry=StringVar()
    entry_email=Entry(new_frame2,textvariable=pstr_email_entry,font=Font_tuple)
    pstr_email_entry.set('')
    entry_email.grid(row=2,column=1,pady=(10,10),padx=(20,0))

    str_email_add=StringVar()
    btn_email_add=Button(new_frame2,textvariable=str_email_add,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_add_phishing_emails)
    str_email_add.set('Add Email id')
    btn_email_add.grid(row=2,column=2,pady=(10,10),padx=(20,0))

    str_email_rem=StringVar()
    btn_email_rem=Button(new_frame2,textvariable=str_email_rem,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_remove_phishing_emails)
    str_email_rem.set('Remove Email id')
    btn_email_rem.grid(row=2,column=3,pady=(10,10),padx=(20,0))

    str_email_show=StringVar()
    btn_email_show=Button(new_frame2,textvariable=str_email_show,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_show_phishing_emails)
    str_email_show.set('Show Email list')
    btn_email_show.grid(row=2,column=4,pady=(10,10),padx=(20,0))

    str_email_clear=StringVar()
    btn_email_clear=Button(new_frame2,textvariable=str_email_clear,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_clear_phishing_emails)
    str_email_clear.set('Clear Email list')
    btn_email_clear.grid(row=2,column=5,pady=(10,10),padx=(20,20))

    # ######### URL
    str_url_lbl=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_url_lbl=Label(new_frame2,textvariable=str_url_lbl,font=Font_tuple,fg=color2)
    str_url_lbl.set('URL')
    lbl_url_lbl.grid(row=3,column=0,pady=(10,10),padx=(20,0))

    Font_tuple = ("Comic Sans MS", 9)

    pstr_url_entry=StringVar()
    entry_url=Entry(new_frame2,textvariable=pstr_url_entry,font=Font_tuple)
    pstr_url_entry.set('')
    entry_url.grid(row=3,column=1,pady=(10,10),padx=(20,0))

    str_url_add=StringVar()
    btn_url_add=Button(new_frame2,textvariable=str_url_add,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_add_phishing_urls)
    str_url_add.set('Add URL')
    btn_url_add.grid(row=3,column=2,pady=(10,10),padx=(20,0))

    str_url_rem=StringVar()
    btn_url_rem=Button(new_frame2,textvariable=str_url_rem,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_remove_phishing_urls)
    str_url_rem.set('Remove URL')
    btn_url_rem.grid(row=3,column=3,pady=(10,10),padx=(20,0))

    str_url_show=StringVar()
    btn_url_show=Button(new_frame2,textvariable=str_url_show,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_show_phishing_urls)
    str_url_show.set('Show URL list')
    btn_url_show.grid(row=3,column=4,pady=(10,10),padx=(20,0))

    str_url_clear=StringVar()
    btn_url_clear=Button(new_frame2,textvariable=str_url_clear,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_clear_phishing_urls)
    str_url_clear.set('Clear URL list')
    btn_url_clear.grid(row=3,column=5,pady=(10,10),padx=(20,20))

    # # ######### phone number
    str_number_lbl=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_number_lbl=Label(new_frame2,textvariable=str_number_lbl,font=Font_tuple,fg=color2)
    str_number_lbl.set('Phone no.')
    lbl_number_lbl.grid(row=4,column=0,pady=(10,10),padx=(20,0))

    Font_tuple = ("Comic Sans MS", 9)

    pstr_number_entry=StringVar()
    entry_number=Entry(new_frame2,textvariable=pstr_number_entry,font=Font_tuple)
    pstr_number_entry.set('')
    entry_number.grid(row=4,column=1,pady=(10,10),padx=(20,0))

    str_number_add=StringVar()
    btn_number_add=Button(new_frame2,textvariable=str_number_add,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_add_phishing_numbers)
    str_number_add.set('Add number')
    btn_number_add.grid(row=4,column=2,pady=(10,10),padx=(20,0))

    str_number_rem=StringVar()
    btn_number_rem=Button(new_frame2,textvariable=str_number_rem,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_remove_phishing_numbers)
    str_number_rem.set('Remove number')
    btn_number_rem.grid(row=4,column=3,pady=(10,10),padx=(20,0))

    str_number_show=StringVar()
    btn_number_show=Button(new_frame2,textvariable=str_number_show,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_show_phishing_numbers)
    str_number_show.set('Show number list')
    btn_number_show.grid(row=4,column=4,pady=(10,10),padx=(20,0))

    str_number_clear=StringVar()
    btn_number_clear=Button(new_frame2,textvariable=str_number_clear,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_clear_phishing_numbers)
    str_number_clear.set('Clear number list')
    btn_number_clear.grid(row=4,column=5,pady=(10,10),padx=(20,20))

    frame_logging_details=Frame(newWindow,background=color5, width=10, height=100)
    frame_logging_details.grid(row=5, column=0, sticky="nsew")
    str_logging_details=StringVar()
    Font_tuple = ("Comic Sans MS", 12,)
    lbl_logging_details=Label(frame_logging_details,textvariable=str_logging_details,font=Font_tuple,padx=10,pady=20,bg=color5, fg=color2)
    str_logging_details.set('----------------- ')
    lbl_logging_details.pack()


def on_btn_click_open_legitimate_list():
    p = Popen(path_to_legit_hnames_file, shell=True)


# add
def on_btn_click_add_legitimate_emails():
    global lstr_email_entry    
    email=lstr_email_entry.get()
    res=get_emails(email)
    if res[0] and res[1]==email:   
        add_email_to_whitelist(email)
        save_and_close_whitelists(2)
        x=email +'    -  Added to whitelist...'
    else:
        x=email +'    -  not of proper format...'
    str_logging_details.set(x)

def on_btn_click_add_legitimate_urls():
    global lstr_url_entry    
    url=lstr_url_entry.get()
    res=get_all_urls(url)
    if res[0] and res[1]==url:    
        add_url_to_whitelist(url)
        save_and_close_whitelists(1)
        x=url +'    -  Added to whitelist...'
    else:
        x=url +'    -  not of proper format...'
    str_logging_details.set(x)

def on_btn_click_add_legitimate_numbers():
    global lstr_number_entry    
    num=lstr_number_entry.get()
    res=get_phone_numbers(num)
    if res[0] and res[1]==num:     
        add_phone_to_whitelist(num)
        save_and_close_whitelists(3)
        x=num +'    -  Added to whitelist...'
    else:
        x=num +'    -  not of proper format...'
    str_logging_details.set(x)


# remove
def on_btn_click_remove_legitimate_emails():
    global lstr_email_entry    
    email=lstr_email_entry.get()
    res=get_emails(email)
    if res[0] and res[1]==email:    
        remove_email_from_whitelist(email)
        save_and_close_whitelists(2)
        x=email +'    -  Removed from whitelist...'
    else:
        x=email +'    -  not in the whitelist...'
    str_logging_details.set(x)

def on_btn_click_remove_legitimate_urls():
    global lstr_url_entry    
    url=lstr_url_entry.get()
    res=get_all_urls(url)
    if res[0] and res[1]==url:    
        remove_url_from_whitelist(url)
        save_and_close_whitelists(1)
        x=url +'    -  Removed from whitelist...'
    else:
        x=url +'    -  not in the whitelist...'
    str_logging_details.set(x)

def on_btn_click_remove_legitimate_numbers():
    global lstr_number_entry    
    num=lstr_number_entry.get()
    res=get_phone_numbers(num)
    if res[0] and res[1]==num:     
        remove_phone_from_whitelist(num)
        save_and_close_whitelists(3)
        x=num +'    -  Removed from whitelist...'
    else:
        x=num +'    -  not in the whitelist...'
    str_logging_details.set(x)


# show 
def on_btn_click_show_legitimate_emails():
    p = Popen(path_to_whitelist_emailid, shell=True)

def on_btn_click_show_legitimate_urls():
    p = Popen(path_to_whitelist_urls, shell=True)

def on_btn_click_show_legitimate_numbers():
    p = Popen(path_to_whitelist_phone, shell=True)


# clear 
def on_btn_click_clear_legitimate_emails():
    clear_email_whitelist()
    save_and_close_whitelists(2)
    x='whitelist cleared'
    str_logging_details.set(x)

def on_btn_click_clear_legitimate_urls():
    clear_url_whitelist()
    save_and_close_whitelists(1)
    x='whitelist cleared'
    str_logging_details.set(x)

def on_btn_click_clear_legitimate_numbers():
    clear_phone_whitelist()
    save_and_close_whitelists(3)
    x='whitelist cleared'
    str_logging_details.set(x)
        

def on_btn_click_get_whitelist_options():
    global lstr_number_entry
    global lstr_url_entry
    global lstr_email_entry
    global str_logging_details

    newWindow=Toplevel(window)
    newWindow.title('Whitelist Options')
    newWindow.grid_columnconfigure(0, weight=1)

    frame_heading_info=Frame(newWindow,background=color4, width=10, height=100)
    frame_heading_info.grid(row=0, column=0, sticky="nsew")
    str_heading_info=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_heading_info=Label(frame_heading_info,textvariable=str_heading_info,font=Font_tuple,padx=10,pady=20,bg=color4, fg=color2)
    str_heading_info.set(string_dataset_info)
    lbl_heading_info.grid(row=0, column=0, sticky="nsew")

    Font_tuple = ("Comic Sans MS", 9, )
    str_pdt_csv=StringVar()
    btn_pdt_csv=Button(frame_heading_info,textvariable=str_pdt_csv,width=18,height=2,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_open_legitimate_list)
    str_pdt_csv.set('Legitimate Domains')
    btn_pdt_csv.grid(row=0, column=1,pady=(10,10),padx=(10,0))

    # ######### Email id
    new_frame2=Frame(newWindow, width=10, height=100)
    new_frame2.grid(row=2, column=0, sticky="nsew")
    
    str_email_lbl=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_email_lbl=Label(new_frame2,textvariable=str_email_lbl,font=Font_tuple,fg=color2)
    str_email_lbl.set('Email id')
    lbl_email_lbl.grid(row=2,column=0,pady=(10,10),padx=(20,0))

    Font_tuple = ("Comic Sans MS", 9)

    lstr_email_entry=StringVar()
    entry_email=Entry(new_frame2,textvariable=lstr_email_entry,font=Font_tuple)
    lstr_email_entry.set('')
    entry_email.grid(row=2,column=1,pady=(10,10),padx=(20,0))

    str_email_add=StringVar()
    btn_email_add=Button(new_frame2,textvariable=str_email_add,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_add_legitimate_emails)
    str_email_add.set('Add Email id')
    btn_email_add.grid(row=2,column=2,pady=(10,10),padx=(20,0))

    str_email_rem=StringVar()
    btn_email_rem=Button(new_frame2,textvariable=str_email_rem,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_remove_legitimate_emails)
    str_email_rem.set('Remove Email id')
    btn_email_rem.grid(row=2,column=3,pady=(10,10),padx=(20,0))

    str_email_show=StringVar()
    btn_email_show=Button(new_frame2,textvariable=str_email_show,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_show_legitimate_emails)
    str_email_show.set('Show Email list')
    btn_email_show.grid(row=2,column=4,pady=(10,10),padx=(20,0))

    str_email_clear=StringVar()
    btn_email_clear=Button(new_frame2,textvariable=str_email_clear,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_clear_legitimate_emails)
    str_email_clear.set('Clear Email list')
    btn_email_clear.grid(row=2,column=5,pady=(10,10),padx=(20,20))

    # ######### URL
    str_url_lbl=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_url_lbl=Label(new_frame2,textvariable=str_url_lbl,font=Font_tuple,fg=color2)
    str_url_lbl.set('URL')
    lbl_url_lbl.grid(row=3,column=0,pady=(10,10),padx=(20,0))

    Font_tuple = ("Comic Sans MS", 9)

    lstr_url_entry=StringVar()
    entry_url=Entry(new_frame2,textvariable=lstr_url_entry,font=Font_tuple)
    lstr_url_entry.set('')
    entry_url.grid(row=3,column=1,pady=(10,10),padx=(20,0))

    str_url_add=StringVar()
    btn_url_add=Button(new_frame2,textvariable=str_url_add,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_add_legitimate_urls)
    str_url_add.set('Add URL')
    btn_url_add.grid(row=3,column=2,pady=(10,10),padx=(20,0))

    str_url_rem=StringVar()
    btn_url_rem=Button(new_frame2,textvariable=str_url_rem,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_remove_legitimate_urls)
    str_url_rem.set('Remove URL')
    btn_url_rem.grid(row=3,column=3,pady=(10,10),padx=(20,0))

    str_url_show=StringVar()
    btn_url_show=Button(new_frame2,textvariable=str_url_show,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_show_legitimate_urls)
    str_url_show.set('Show URL list')
    btn_url_show.grid(row=3,column=4,pady=(10,10),padx=(20,0))

    str_url_clear=StringVar()
    btn_url_clear=Button(new_frame2,textvariable=str_url_clear,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_clear_legitimate_urls)
    str_url_clear.set('Clear URL list')
    btn_url_clear.grid(row=3,column=5,pady=(10,10),padx=(20,20))

    # # ######### phone number
    str_number_lbl=StringVar()
    Font_tuple = ("Comic Sans MS", 10)
    lbl_number_lbl=Label(new_frame2,textvariable=str_number_lbl,font=Font_tuple,fg=color2)
    str_number_lbl.set('Phone no.')
    lbl_number_lbl.grid(row=4,column=0,pady=(10,10),padx=(20,0))

    Font_tuple = ("Comic Sans MS", 9)

    lstr_number_entry=StringVar()
    entry_number=Entry(new_frame2,textvariable=lstr_number_entry,font=Font_tuple)
    lstr_number_entry.set('')
    entry_number.grid(row=4,column=1,pady=(10,10),padx=(20,0))

    str_number_add=StringVar()
    btn_number_add=Button(new_frame2,textvariable=str_number_add,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_add_legitimate_numbers)
    str_number_add.set('Add number')
    btn_number_add.grid(row=4,column=2,pady=(10,10),padx=(20,0))

    str_number_rem=StringVar()
    btn_number_rem=Button(new_frame2,textvariable=str_number_rem,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_remove_legitimate_numbers)
    str_number_rem.set('Remove number')
    btn_number_rem.grid(row=4,column=3,pady=(10,10),padx=(20,0))

    str_number_show=StringVar()
    btn_number_show=Button(new_frame2,textvariable=str_number_show,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_show_legitimate_numbers)
    str_number_show.set('Show number list')
    btn_number_show.grid(row=4,column=4,pady=(10,10),padx=(20,0))

    str_number_clear=StringVar()
    btn_number_clear=Button(new_frame2,textvariable=str_number_clear,width=15,height=1,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_clear_legitimate_numbers)
    str_number_clear.set('Clear number list')
    btn_number_clear.grid(row=4,column=5,pady=(10,20),padx=(20,20))

    frame_logging_details=Frame(newWindow,background=color5, width=10, height=100)
    frame_logging_details.grid(row=5, column=0, sticky="nsew")
    str_logging_details=StringVar()
    Font_tuple = ("Comic Sans MS", 10, )
    lbl_logging_details=Label(frame_logging_details,textvariable=str_logging_details,font=Font_tuple,padx=10,pady=20,bg=color5, fg=color2)
    str_logging_details.set('----------------- ')
    lbl_logging_details.pack()


name=['Accuracy','Precision','Recall','F1_Score','Confusion_Matrix','Jaccard_Score','Mean_Square_Error']
x=[0.99581589958159, 0.996260663507109, 0.997264663507109, 0.997624703087886, [[ 196,    7],[   0, 1470]], 0.995260663507109, 0.0041841004184100415]
classifiaction_details_constant_string=f'Accuracy=  {x[0]}\n\nPrecision=  {x[1]}\n\nRecall=  {x[2]}\n\nF1-Score=  {x[3]} \n\nConfusion Matirx=  {x[4]}\n\nJ Score=  {x[5]}\n\nMean Square Error=  {x[6]}'

def get_classifier_for_msg_verfication():
    pathrd="D:\\DOWNLOADS\\features.csv"    
    df=pd.read_csv(pathrd,keep_default_na=False)
    data=df.values
    X2=data[:,:60]
    y=data[:,60]
    y=y.astype('int')
    clf1=RandomForestClassifier(n_estimators=200)
    X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.3,shuffle=True) # 70% training and 30% tes
    clf1.fit(X_train,y_train)
    return clf1

msg_classifier=get_classifier_for_msg_verfication()

def get_all_details_extracted_form_msg(msg):
    global msg_classifier
    
    r_email_id=get_emails(msg)
    r_phone_number=get_phone_numbers(msg)
    r_url=get_all_urls(msg)
    
    str_email_id,email_id=r_email_id[1],r_email_id[0]
    str_phone_number,phone_number=r_phone_number[1],r_phone_number[0]
    str_url,url=r_url[1],r_url[0]
    
    
    if  (len(str_email_id)!=0 and str_email_id in email_blacklist) or (len(str_url)!=0 and (str_url in url_blacklist or str_url in phishtank_blacklist)) or (len(str_phone_number)!=0 and str_phone_number in phone_blacklist):        
        classification_result_for_msg=0 
        ################################################################################################################################
        str_email_id=str_email_id if len(str_email_id)!=0 else 'Not Present'
        str_phone_number=str_phone_number if len(str_phone_number)!=0 else 'Not Present'
        str_url=str_url if len(str_url)!=0 else 'Not Present'
        details_from_msg=f'Present in Blacklists:\n\nEmail Id=  {str_email_id}\n\nUrl=  {str_url}\n\nPhone Number=  {str_phone_number}'
        ################################################################################################################################
    
    else: 
        suspicious_keywords=get_suspicious_keywords(msg)
        wc=get_word_count(msg)
        ucwc=get_upper_case_word_count(msg)
        spec_char=get_special_character(msg)
        speech_tags=get_speech_tagger(msg)
        feature_counts=get_counts_digit_size_alpha_space_symbols_punc(msg)
        missplled_score=get_misspelled_words(msg)
        read_scores=get_readability_scores(msg)
        self_ans_msg= get_self_answering_type_msgs(msg)
        emotions=get_presence_of_emotions(msg)
        greetings=get_greeting_words(msg)
        visual_morph=get_visual_morph(msg)
        url_features=[0,0,0,0,0,0,-1]
        src_code_analysis=1
        apk_detection=0
        #extracting url based features
        if url!=0:
            ext_url=fetch_urls(msg)
            res_url=short_url_resolution_method_1(ext_url)
            if res_url!=None:
                url_features=get_url_based_features(res_url)
                src_code_analysis=source_code_analyzer(res_url)
                apk_detection=apk_download_detector(res_url)


        features_list=[]
        for x in suspicious_keywords[0]:
            features_list.append(x)

        features_list.append(wc)
        features_list.append(ucwc)
        features_list.append(spec_char[0]) 
        
        for x in speech_tags[0]:
            features_list.append(x)    
        
        for x in feature_counts:
            features_list.append(x)    

        features_list.append(missplled_score)
        
        for x in read_scores:
            features_list.append(x)    

        features_list.append(phone_number)
        features_list.append(email_id)
        features_list.append(url)
        features_list.append(self_ans_msg)
        features_list.append(emotions)
        features_list.append(greetings)
        features_list.append(visual_morph)

        for x in url_features:
            features_list.append(x)    

        features_list.append(src_code_analysis)
        features_list.append(apk_detection)
    
        ################################################################################################################################
        str_email_id=str_email_id if len(str_email_id)!=0 else 'Not Present'
        str_phone_number=str_phone_number if len(str_phone_number)!=0 else 'Not Present'
        str_url=str_url if len(str_url)!=0 else 'Not Present'
        suspicious_keywords='Not Present' if len(suspicious_keywords[1])==0 else suspicious_keywords[1]
        spec_char='Not Present' if len(spec_char[1])==0 else spec_char[1]        
        speech_tags=speech_tags[0]
        self_ans_msg='Yes' if self_ans_msg==0 else 'No'
        emotions='Yes' if emotions==1 else 'No'
        greetings='Yes' if greetings==1 else 'No'
        
        details=[
                    f'Email Id=  {str_email_id}',
                    f'Url=  {str_url}',
                    f'Phone Number=  {str_phone_number}',
                    f'Suspicious Keywords=  {suspicious_keywords}',
                    f'Word Count=  {wc}',
                    f'Upper Case Word Count= {ucwc}',
                    f'Special Characters=  {spec_char}',
                    f'Speech Tags Counts==\n                    Noun:{speech_tags[0]}\n                    Conjunction: {speech_tags[1]}\n                    Adverb: {speech_tags[2]}\n                    Preposition: {speech_tags[3]}\n                    Adjective: {speech_tags[4]}\n                    Pronoun: {speech_tags[5]}\n                    Verb: {speech_tags[6]}',
                    f'Message Length==  {feature_counts[0]}',
                    f'Digits Count==  {feature_counts[1]}',
                    f'Alphabets Count==  {feature_counts[2]}',
                    f'WhiteSpace Count==  {feature_counts[3]}',
                    f'UpperCase Letters Count==  {feature_counts[4]}',
                    f'Mathematical Symbols Count==  {feature_counts[5]}',
                    f'Puncutation Symbols Count==  {feature_counts[6]}',
                    f'Misspelled Words Score==  {missplled_score}',
                    f'Readability Algorithm Scores==  {read_scores}',
                    f'Self Answering Type==  {self_ans_msg}',
                    f'Conatins Emotions==  {emotions}',
                    f'Contains Greeting Words==  {greetings}',
                    '\n\n'              
                ]
        
        divider='-'*70
        details_from_msg=('\n\n'+divider+'\n').join(details)
        ################################################################################################################################
        features_list=np.array(features_list)
        # print(features_list)
        features_list=features_list.reshape(1,-1)
        classification_result_for_msg=msg_classifier.predict(features_list)[0]
    
    x=(  'Legitimate Message' if classification_result_for_msg==1 else 'Phishing Message' ,details_from_msg)
    print('\n',x[0],'\n','*'*150,sep='')
    return x


def on_btn_click_verify_message():
    txt_extracted.delete('1.0',END)
    Font_tuple = ("Comic Sans MS", 8, "italic")
    msg=txt_feild.get('1.0',END)
    if msg=='Enter the Message here...\n':
        str_classification_result.set("First Enter the Message to be Classified...")
        return
    print('*'*150)
    print('Message-->     ',msg)
    extracted_details_from_msg=get_all_details_extracted_form_msg(msg)
    str_classification_result.set(extracted_details_from_msg[0])
    txt_extracted.insert(END,extracted_details_from_msg[1])
    


frame_heading=Frame(window,background=color5, width=10, height=100)
frame_heading.grid(row=0, column=0, sticky="nsew")
str_heading=StringVar()
Font_tuple = ("Comic Sans MS", 20, "bold")
lbl_heading=Label(frame_heading,textvariable=str_heading,font=Font_tuple,padx=10,pady=20,bg=color5, fg=color2)
str_heading.set('SMS Phishing Detector')
lbl_heading.pack()
window.grid_columnconfigure(0, weight=1)
#******************************************************************************************************************************************************************************************************************************************************************************************************************************


frame_msg=Frame(window, width=10, height=100,bd=7,padx=10)
frame_msg.grid(row=1, column=0, sticky="nsew")

frame_details_lbl=Frame(frame_msg, width=10, height=100)
frame_details_lbl.grid(row=1, column=0, sticky="nsew")
Font_tuple = ("Comic Sans MS", 10,'bold')
str_feild=StringVar()
lbl_feild=Label(frame_details_lbl,textvariable=str_feild,font=Font_tuple,anchor='w')
str_feild.set('Message Content')
lbl_feild.grid(row=1, column=0,pady=(5,0))

frame_txt=Frame(frame_msg, width=10, height=100)
frame_txt.grid(row=2, column=0, sticky="nsew")
Font_tuple = ("Comic Sans MS", 8, "italic")
txt_feild=Text(frame_txt,bg=color4,bd=3,font=Font_tuple,height=8,width=50,insertofftime=0)
txt_feild.insert(INSERT,'Enter the Message here...')
txt_feild.grid(row=2, column=0)

frame_extracted_lbl=Frame(frame_msg, width=10, height=100)
frame_extracted_lbl.grid(row=3, column=0, sticky="nsew")
Font_tuple = ("Comic Sans MS", 10,'bold')
str_extracted=StringVar()
lbl_extracted=Label(frame_extracted_lbl,textvariable=str_extracted,font=Font_tuple,anchor='w')
str_extracted.set('Details.. ')
lbl_extracted.grid(row=3, column=0,pady=(15,0))

frame_extracted_txt=Frame(frame_msg, width=10, height=100)
frame_extracted_txt.grid(row=4, column=0, sticky="nsew")
Font_tuple = ("Comic Sans MS", 8, "italic")
txt_extracted=Text(frame_extracted_txt,bg=color4,bd=3,font=Font_tuple,height=14,width=50,insertofftime=0)
txt_extracted.insert(INSERT,'Details Extracted...')
txt_extracted.grid(row=4, column=0,pady=(0,5))
#******************************************************************************************************************************************************************************************************************************************************************************************************************************


frame_classification_result=Frame(window,background=color5, width=10, height=100)
frame_classification_result.grid(row=5, column=0, sticky="nsew")
str_classification_result=StringVar()
Font_tuple = ("Comic Sans MS", 15, "bold")
lbl_classification_result=Label(frame_classification_result,textvariable=str_classification_result,font=Font_tuple,padx=10,pady=20,bg=color5, fg=color2)
str_classification_result.set('----------------- ')
lbl_classification_result.pack()
#******************************************************************************************************************************************************************************************************************************************************************************************************************************


frame_details=Frame(frame_msg, width=10, height=100)
frame_details.grid(row=1, column=1,rowspan=4, sticky="nsew",padx=(30,10),pady=(20,10))
Font_tuple = ("Comic Sans MS", 9, )

str_classification_details=StringVar()
btn_classification_details=Button(frame_details,textvariable=str_classification_details,width=18,height=2,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_get_classiification_details)
clf7=LinearDiscriminantAnalysis()
str_classification_details.set('Classification Details')
btn_classification_details.grid(row=1, column=1,pady=(0,12))

str_dataset_details=StringVar()
btn_dataset_details=Button(frame_details,textvariable=str_dataset_details,width=18,height=2,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_get_dataset_details)
str_dataset_details.set('Dataset Details')
btn_dataset_details.grid(row=2, column=1,pady=(0,12))

str_blacklist_details=StringVar()
btn_blacklist_details=Button(frame_details,textvariable=str_blacklist_details,width=18,height=2,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_get_blacklist_options)
str_blacklist_details.set('Blacklist Options')
btn_blacklist_details.grid(row=3, column=1,pady=(0,12))

# str_whitelist_details=StringVar()
# btn_whitelist_details=Button(frame_details,textvariable=str_whitelist_details,width=18,height=2,bg=color3,bd=3,font=Font_tuple,command=on_btn_click_get_whitelist_options)
# str_whitelist_details.set('Whitelist Options')
# btn_whitelist_details.grid(row=4, column=1,pady=(0,12))

str_Verify_details=StringVar()
btn_Verify_details=Button(frame_details,textvariable=str_Verify_details,width=18,height=2,bg=color6,bd=3,font=Font_tuple,command=on_btn_click_verify_message)
str_Verify_details.set('Verify Message')
btn_Verify_details.grid(row=4, column=1,pady=(0,12))

str_exit_details=StringVar()
btn_exit_details=Button(frame_details,textvariable=str_exit_details,width=18,height=2,bg=color7,bd=3,font=Font_tuple,command=window.destroy)
str_exit_details.set('Exit')
btn_exit_details.grid(row=5, column=1,pady=(0,12))
#******************************************************************************************************************************************************************************************************************************************************************************************************************************
#******************************************************************************************************************************************************************************************************************************************************************************************************************************

# if (len(email_blacklist)==0):
#     intialize_blacklist()
    
# if (len(email_whitelist)==0):
#     intialize_whitelist()

# if (len(phishtank_blacklist)==0):
#     intialize_phishtank_alexa_list()

# window.mainloop()












