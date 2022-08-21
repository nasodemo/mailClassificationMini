import os
import tarfile
import urllib.request
#import pandas as pd

DOWNLOAD_ROOT = 'https://spamassassin.apache.org/old/publiccorpus/'
SPAM_PATH = os.path.join('datasets', 'spam')
mail_loots = []
mail_loots.append("20030228_easy_ham.tar.bz2")
mail_loots.append("20030228_easy_ham_2.tar.bz2")
mail_loots.append("20030228_hard_ham.tar.bz2")
mail_loots.append("20030228_spam.tar.bz2")
#해야하는 일 정리
#압축파일 열고 => 폴더 내부의 모든 파일을 load하고, 한 변수에 저장하기

def fetch_mail_data(filename, spam_path=SPAM_PATH, download_root = DOWNLOAD_ROOT):
    mail_url = DOWNLOAD_ROOT + filename
    if not os.path.isdir(spam_path): # os.path.isdir 는 (path) 가 존재하면 True 값 반환함
        os.makedirs(spam_path) # spam datasets 폴더 생성
    bz2_path = os.path.join(spam_path, filename)
    if not os.path.isfile(bz2_path):
        urllib.request.urlretrieve(mail_url, bz2_path) # urlretrieve(url주소, 파일 이름)
    mail_bz2 = tarfile.open(bz2_path)
    mail_bz2.extractall()
    mail_bz2.close()

for i in mail_loots:
    fetch_mail_data(i)
