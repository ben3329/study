# 장점: 쉬운 유지보수, 각 분야 전문가들이 독립적으로 일할 수 있음(프론트, 백, ...)
class Model(object):
    services = {
        'email':{'number':1000, 'price':2},
        'sms':{'number':1000, 'price':10},
        'voice':{'number':1000, 'price':15},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')
    def list_pricing(self, services):
        for svc in services:
            print('for', Model.services[svc]['number'], svc, "mes pay $", Model.services[svc]['price'])

class Controller(object):
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))
    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_pricing(services))

class Client(object):
    controller = Controller()
    print('svc provid: ')
    controller.get_services()
    print('pric for svc:')
    controller.get_pricing()
    
print('================================')
    
class Model(object):
    def logic(self):
        data = 'got it'
        print('model...')
        return data
class View(object):
    def update(self, data):
        print('view ', data)
class Controller(object):
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
    def interface(self):
        print('ctr')
        data = self.model.logic()
        self.view.update(data)
class Client(object):
    print('client')
    controller = Controller()
    controller.interface()
    
print('================================')

from signal import Handlers
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

s = sqlite3.connect('a.db')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = 'select * from task'
        todos = s.execute(query)
        self.render('index.html', todos=todos)
class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', None)
        query = 'create table if not exists task (id INTERGER PRIMARY KEY, name TEXT, status NUMERIC'
        s.execute(query)
        query = "insert into task (name, status) values('%s', %d) " %(name, 1)
        s.execute(query)
        self.redirect('/')
    def get(self):
        self.render('new.html')
class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = 'update task set status=%d where id=%s' %(int(status), id)
        s.execute(query)
        self.redirect('/')
class DeleteHandler(tornado.web.RedirectHandler):
    def get(self, id):
        query = 'delete from task where id=%s' % id
        s.execute(query)
        self.redirect('/')

class RunApp(tornado.web.Application):
    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'/todo/update/(\d+)/status(/d+)', UpdateHandler),
            (r'/todo/delete/(\d+)', DeleteHandler),
        ]
        settings = dict(
            debug=True,
            template_path = 'templates',
            static_path='static',
        )
        tornado.web.Application.__init__(self, Handlers, **settings)
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()
