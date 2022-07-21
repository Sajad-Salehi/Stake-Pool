from crypt import methods
from flask import Flask, render_template, request
from static import deposit, withdraw, get_balance

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    
    balance = get_balance()
    return render_template('page_1.html', balance=balance)



@app.route('/deposit', methods=['GET', 'POST'])
def Deposit():

    amount = request.form.get('content1')
    deposit(amount)
    balance = get_balance()
    return render_template('page_1.html', balance=balance)


@app.route('/withdraw', methods=['GET', 'POST'])
def Withdraw():


    withdraw()
    balance = get_balance()
    return render_template('page_1.html', balance=balance)


if __name__ == '__main__':
    app.run(debug=TRUE)