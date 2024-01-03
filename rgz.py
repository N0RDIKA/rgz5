from flask import Blueprint, redirect, url_for 
rgz = Blueprint('rgz', __name__)


@rgz. route("/")
@rgz. route("/index")
def start():
    return redirect("/menu", code=302)


@rgz. route("/menu")
def menu():
    return '''
   
<!doctype html>

<html>
 <link rel="stylesheet" href="''' +url_for('static', filename='rgz.css')+'''"
        <head>
         <title>НГТУ, ФБ</title>
        </head>
        <body>
            <header>
                НГТУ,
ФБ, WEB-программирование, часть 2. 
            </header>
            <h2><a href="/glavnaya" >РГЗ</a></h2>
            <footer>
                &copy; Сердюк Анастасия, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
</html>
'''