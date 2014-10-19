from flask import Flask, render_template
from flask_bootstrap import Bootstrap

def main():
    app = Flask(__name__)
    app.debug = True
    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(host='0.0.0.0', port=5001)
    
def create_app():
    app = Flask(__name__)
    app.debug = True
    Bootstrap(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
#    create_app().run(host='0.0.0.0', port=5001)
    main()
    