# @Author  : ShiRui

from tornado import web, ioloop
import time


class MainHandler(web.RequestHandler):

        def get(self):
            self.render('index.html', name="留言板", messages=Messages)


class LeaveWord(web.RequestHandler):

        def get(self):
            self.render('word.html', messages=Messages)

        def post(self, *args, **kwargs):
            content = self.get_argument('content', default=None)
            name = self.get_argument('name', default="匿名")
            if content:
                Messages.append(
                    {'name': name,
                     'content': content,
                     'id': len(Messages)+1,
                     'num': len(Messages)+1,
                     'time': time.strftime('%Y-%m-%d: %H:%M:%S ')}
                )
                self.redirect('/')
            else:
                self.write("不能为空！")

if __name__ == "__main__":

    try:
        Messages = []

        setting = {
            'template_path': 'templates',
            'static_path': 'statics'
        }

        application = web.Application([
            (r"/", MainHandler),
            (r"/word", LeaveWord),
        ], **setting)

        application.listen(8888)
        ioloop.IOLoop.current().start()

    except Exception as e:

        print(e)
