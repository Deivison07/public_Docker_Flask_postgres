from flask import Flask, render_template
from common.routes import register_routes
from common.database import config_database

#init flask
app = Flask(__name__)

#rotas
register_routes(app)

#database
config_database(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'),404

@app.route('/favicon.ico')
def favicon():
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)