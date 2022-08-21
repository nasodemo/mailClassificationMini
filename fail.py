import email
import email.policy
import os

import os

root = r'C:\Users\pc\Desktop\code\datasets\mail' #폴더 위치
email = []
spam_email = []
i = 0
count = 0
folder_dirs = ['easy_ham', 'easy_ham_2', 'hard_ham']
for folder in folder_dirs:
    file_list = os.listdir(root + '/' + folder)
    email.append([])
    for file in file_list:
        with open(root + '/' + folder + '/' + file) as f:
            try:
                email[i].append(f.read()) #이메일 저장
                if count == 0:
                    print(email[i])
                    count += 1
            except:
                pass
    i += 1
i = 0

folder_dirs = ['spam']
for folder in folder_dirs:
    file_list = os.listdir(root + '/' + folder)
    spam_email.append([])
    for file in file_list:
        with open(root + '/' + folder + '/' + file) as f:
            try:
                spam_email[i].append(f.read()) #이메일 저장
                if count == 0:
                    print(spam_email[i])
                    count += 1
            except:
                pass
    i += 1

import numpy as np
from sklearn.model_selection import train_test_split

X = np.array(email + spam_email, dtype=object)
y = np.array([0] * len(email) + [1] * len(email))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
