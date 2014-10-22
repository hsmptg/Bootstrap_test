from flask import Flask, render_template
from flask_bootstrap import Bootstrap

def main():
    app = Flask(__name__)
    app.debug = True
    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/2')
    def index2():
        return render_template('index2.html')

    @app.route('/3')
    def index3():
        return render_template('index3.html')

    app.run(host='0.0.0.0', port=5001)

if __name__ == '__main__':
    main()
    