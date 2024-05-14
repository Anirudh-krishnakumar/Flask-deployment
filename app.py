from flask import Flask,render_template
 
k=Flask(__name__)
@k.route('/')
def anik():
    return render_template('home.html')
    
    