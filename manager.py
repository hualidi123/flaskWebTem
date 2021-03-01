from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from api.app import create_app

app = create_app()

if __name__ == "__main__":
    app.debug = True
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5555)
    IOLoop.instance().start()
    # debug
    # app.run(host="192.168.0.29", port="5555", debug=True)
