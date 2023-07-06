from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/lists')
def table():
    users = [
        {'id' : '1','first_name' : 'Michael', 'last_name' : 'Choi', 'email' : 'yahoo@yehaw.com'},
        {'id' : '2','first_name' : 'John', 'last_name' : 'Supsupin', 'email' : 'google@gaggle.com'},
        {'id' : '3','first_name' : 'Mark', 'last_name' : 'Guillen', 'email' : 'msn@enesem.com'},
        {'id' : '4','first_name' : 'KB', 'last_name' : 'Tonel', 'email' : 'hotmail@coldparcel.com'}
]
    #added extra key:value pairs to match the bootstrap table!
    return render_template('table.html', users=users)

if __name__=="__main__":
    app.run(debug=True)