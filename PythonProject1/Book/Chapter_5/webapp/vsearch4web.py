

from flask import Flask, render_template

from Book.Chapter_4.finder_letters_in import find_letters_in_words

app = Flask(__name__) # створення обьекту Flask і присвоєння його змінній app
@app.route("/") # декоратор функцій додає доп функціонал
def hello() -> str: # звичайна функція яка повертає стрінгу
    return  str('Hello World! from Flask_22!')


@app.route("/search") # декоратор функцій додає доп функціонал
def do_search():
    return  str(find_letters_in_words('eoia','frankinstein'))


@app.route('/entry')
def entry_page() -> 'html':
 return render_template('entry.html',
 the_title='Welcome to search4letters on the web!')

app.run() # обьект app починає виконувати