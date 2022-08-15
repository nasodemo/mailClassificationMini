# 실패 코드

import os
import tarfile
import urllib.request
import pandas as pd

DOWNLOAD_ROOT = 'https://spamassassin.apache.org/old/publiccorpus/'
MAIL_PATH = os.path.join('datasets', 'mail')
EASY1_MAIL_URL = DOWNLOAD_ROOT + 20030228_easy_ham.tar.bz2
EASY2_MAIL_URL = DOWNLOAD_ROOT + 20030228_easy_ham_2.tar.bz2
HARD_MAIL_URL = DOWNLOAD_ROOT + 20030228_hard_ham.tar.bz2
SPAM_MAIL_URL = DOWNLOAD_ROOT + 20030228_spam.tar.bz2

def fetch_mail_data(easy1_mail_url = EASY1_MAIL_URL, easy2_mail_url=EASY2_MAIL_URL, hard_mail_url=HARD_MAIL_URL, spam_mail_url=SPAM_MAIL_URL, mail_path=MAIL_PATH)
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    bz2_path = os,path.join(mail_path, "mail.bz2")
    urllib.request.urlretrieve(mail_url, bz2_path) # urlretrieve(url주소, 파일 이름)
    mail_bz2 = tarfile.open(bz2_path)
    mail_bz2.extractall(path=mail_path)
    mail_bz2.close()
fetch_mail_data()


#어차피 메일 파일은 html파일이니까 아래 내용은 큰 쓸모는 없을 듯 합니다.
def load_mail_data(mail_path=MAIL_PATH):
    csv_path = os.path.jopin(mail_path, "mail.csv")
    return pd.read_csv(csv_path)
