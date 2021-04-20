from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)

@app.route('/')
def route():
    return '<h1> Ovo je naslov </h1>'


if __name__ == '__main__':
    app.run(debug=True)

