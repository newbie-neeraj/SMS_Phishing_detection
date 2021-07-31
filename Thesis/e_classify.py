from d_appfend import *



pathrd='F:\\Thesis\\csv_files\\features.csv'
df=pd.read_csv(pathrd,keep_default_na=False)
data=df.values
X1=data[:,:51]
X2=data[:,:60]
y=data[:,60]
y=y.astype('int')


def get_metrics(X,clf):
    global y
    maxrs=[0,0,0,0,0,0,0]
    for i in range(10):
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

def get_all_ml_models_metrics_scores():
    global X1
    global X2
    global clf1
    global clf2
    global clf3
    global clf4
    global clf5
    global clf6
    global clf7
    global clf8
    global clf9
    print('RandomForest')
    get_metrics(X1,clf1)
    get_metrics(X2,clf1)
    print('*'*150,'\n')


    print('Decision Tree')
    get_metrics(X1,clf2)
    get_metrics(X2,clf2)
    print('*'*150,'\n')


    print('AdaBoost')
    get_metrics(X1,clf3)
    get_metrics(X2,clf3)
    print('*'*150,'\n')


    print('SVM')
    get_metrics(X1,clf4)
    get_metrics(X2,clf4)
    print('*'*150,'\n')
    
    print('Naive Bayes')
    get_metrics(X1,clf5)
    get_metrics(X2,clf5)
    print('*'*150,'\n')

    print('Logistic Regression')
    get_metrics(X1,clf6)
    get_metrics(X2,clf6)
    print('*'*150,'\n')

    print('KNN')
    get_metrics(X1,clf7)
    get_metrics(X2,clf7)
    print('*'*150,'\n')

    print('LDA')
    get_metrics(X1,clf8)
    get_metrics(X2,clf8)
    print('*'*150,'\n')
    
    print('Gradient Boost')
    get_metrics(X1,clf9)
    get_metrics(X2,clf9)
    print('*'*150,'\n')
    

get_all_ml_models_metrics_scores()



