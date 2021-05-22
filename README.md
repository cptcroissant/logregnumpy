# logregnumpy


Logistic Regressor Classifier.
    
Performs a gradient descent method for a loss minimizing.
    
Works with binary and multiclass targets. 
    
Parameters
----------
lr : float, default=1e-3
     Learning rate (size) for each step of an gradient descent.
        
l2_reg : float, default=0.2
     Degree of L2 penalty.
        
epochs : int, default=100
     Number of gradient descent iterations.
    
Examples
--------
```
>>> from sklearn.datasets import load_iris  
>>> from logregnumpy import LogRegNumpy  
>>> X, y = load_iris(return_X_y=True)  
>>> model = LogRegNumpy(l2_reg=0.1, epochs=1000)  
>>> model.fit(X, y)  
>>> model.predict(X)  

array([0, 0, 0])  

>>> model.predict_proba(X)[:3]

array([[9.69584306e-01, 3.04018742e-02, 1.38198704e-05],  
       [9.32753885e-01, 6.71844981e-02, 6.16165599e-05],  
       [9.57931295e-01, 4.20313028e-02, 3.74027136e-05]])  
```

"""
