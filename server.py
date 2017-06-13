from flask import Flask
from flask import render_template
import pymongo

from config import MONGO_URL, MONGO_DATABASE,MONGO_COLLECTION

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)

site_list = [
    'newsbtc',
    'newsbitcoin',
    'coindesk',
    'bitcoinmagazine',
]


@app.route('/')
def get_site():
    return render_template('index.html', list=site_list)


@app.route('/<site>')
def get_news(site):
    try:
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DATABASE]
        collection = db[MONGO_COLLECTION]

        if not site in site_list:
            return 'Site is not available'
        data = list(collection.find({'site': site}).sort([('time', pymongo.DESCENDING)]).limit(60))
        responses = []
        for doc in data:
            try:
                res = dict()
                res['title'] = doc['title']
                res['link'] = doc['link']
                res['time'] = doc['time']
                responses.append(res)
            except:
                pass
        return render_template('info.html',site = site, list=responses)
    except:
        return"Seems something unexpected happened on server"
    finally:
        client.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    print('[*] Starting Server at port 5000')
    IOLoop.instance().start()