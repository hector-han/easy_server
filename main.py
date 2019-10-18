import tornado.ioloop
import tornado.web
import json
import datetime

store_file = 'received_info.txt'
fhandler = open(store_file, 'a', encoding='utf-8')


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        requestId = self.get_body_argument('requestId', default='')
        code = self.get_body_argument('code', default='1')
        text = self.get_body_argument('text', default='')
        resp = {"code": 0, "message": "成功"}
        if code == '0':
            fhandler.write('[{}]: {},{}'.format(now, requestId, text) + '\n')
            fhandler.flush()
        else:
            fhandler.write('[{}]: ERROR: '.format(now) + self.request.body.decode() + '\n')
        self.write(json.dumps(resp, ensure_ascii=False))


def make_app():
    return tornado.web.Application([
        (r"/tencent_record", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8796)
    tornado.ioloop.IOLoop.current().start()