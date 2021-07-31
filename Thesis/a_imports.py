import pandas as pd
import string
import nltk
import random
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import enchant
import readability
import  requests
from os import path
import pycurl
import http.client
import whois
import time
import datetime
from collections import defaultdict
import OpenSSL #pip install pyOpenSSL
import socket
from bs4 import BeautifulSoup
import get_cert
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
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
from subprocess import Popen
path_to_original_sms_dataset=''
path_to_legit_alexa_dataset_hostname_file=''
path_to_combined_dataset=''
path_to_phishing_hnames_file=''
path_to_legit_hnames_file=''
path_to_download_phish_file=''
path_to_blacklist_emailid=''
path_to_blacklist_phone=''
path_to_blacklist_urls=''
path_to_whitelist_emailid=''
path_to_whitelist_phone=''
path_to_whitelist_urls=''
path_to_x509_certificate_policies_files=''
path_to_derived_sms_dataset=''
path_to_sms_based_features=''
IP_ADDRESS_AS_DOMAIN_SEARCH_PATTERN_1='//\d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}$'
IP_ADDRESS_AS_DOMAIN_SEARCH_PATTERN_2='//\d{1,3}\\.\d{1,3}\\.\d{1,3}\\.\d{1,3}[/:]'
# from b_msgcntnt_links import *
# from c_lists_apdwnld_src_check import *













