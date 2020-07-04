import tornado.ioloop
import tornado.web


# 类视图
class MainHandler(tornado.web.RequestHandler):
    # get,post,put,delete
    # def get(self):
    # 	# 打开文件返回
    # 	with open('./templates/index.html') as f:
    # 		content = f.read()
    # 	self.write(content)  # 返回网页内容,专门处理文字,

    # 专门用来显示模板内容的
    def get(self):
        self.render("index.html", name='oldyang', show_list=[1, 2, 3, 4])

    def post(self):
        self.write("post")

    def put(self):
        self.write("put")

    def delete(self):
        self.write("delete")


# 路由函数
def make_app():
    return tornado.web.Application([
        (r"/books/", MainHandler),  # 路由
    ],
        static_path='./static',  # 静态文件夹路径
        template_path="./templates"  # 模板路径
    )


# 程序入口
if __name__ == "__main__":
    # 配置信息
    app = make_app()
    # 端口
    app.listen(8787)
    # 启动服务器
    tornado.ioloop.IOLoop.current().start()
