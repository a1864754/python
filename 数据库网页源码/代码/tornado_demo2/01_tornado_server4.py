import json

# 类视图
import aiomysql
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    # get,post,put,delete
    # def get(self):
    # 	# 打开文件返回
    # 	with open('./templates/index.html') as f:
    # 		content = f.read()
    # 	self.write(content)  # 返回网页内容,专门处理文字,

    # 专门用来显示模板内容的
    async def get(self):
        print("get请求开始")
        # 1.读取数据库的数据
        # 2.把数据库的数据传给模板
        # 3.模板中渲染我们的数据

        # 1.读取数据库的数据
        # 1. 从数据库得到数据
        # 1.1连接数据库
        # 创建Connection连接
        conn = await aiomysql.connect(host='localhost', port=1433, db='lrdb', user='liurui1',
                                      password='10086',
                                      charset='utf8')

        # cursor异步上下文管理器,好处我们就不需要使用cur.close进行游标的关闭了
        async with conn.cursor() as cur:
            await cur.execute("select * from books;")
            data = await cur.fetchall()

        # # 获得Cursor对象
        # cs1 = await conn.cursor()
        #
        # # for temp in range(10000):
        # # 	# 1.2 执行查询的sql语句
        # # 	await cs1.execute("select * from books;")
        # # 	# 得到数据库的数据
        # # 	data = await cs1.fetchall()
        #
        # # 1.2 执行查询的sql语句
        # await cs1.execute("select * from books;")
        # # 得到数据库的数据
        # data = await cs1.fetchall()
        #
        # # 1.3 关闭
        # await cs1.close()
        conn.close()

        # print(data)
        # 2.把数据库的数据传给模板
        # 3.模板中渲染我们的数据

        print("展示内容")
        self.render("index.html", show_list=data)

    async def post(self):
        # 1.得到前端的数据
        # 2.根据前端的数据做一下数据插入的动作
        # 3. 返回一个json格式的数据,直接返回一个字典

        # 1.得到前端的数据
        # print(self.get_argument("btitle"))

        # 1.1创建一个列表
        params_list = list()

        # 1.2把参数添加到列表中
        params_list.append(self.get_argument('btitle'))
        params_list.append(self.get_argument('bauthor'))
        params_list.append(self.get_argument('bperson'))
        params_list.append(self.get_argument('bpub_date'))
        params_list.append(self.get_argument('bread'))
        params_list.append(self.get_argument('bcomment'))

        # print(params_list)

        # 2.根据前端的数据做一下数据插入的动作
        # 1. 从数据库得到数据
        # 1.1连接数据库
        # 创建Connection连接
        conn = await aiomysql.connect(host='localhost', port=1433, db='lrdb', user='liurui1',
                                      password='10086',
                                      charset='utf8')
        # 获得Cursor对象
        cs1 = await conn.cursor()

        # 1.2 执行查询的sql语句
        await cs1.execute(
            "insert into books(btitle,bauthor,bperson,bpub_date,bread,bcomment) VALUES (%s,%s,%s,%s,%s,%s)",
            params_list)

        # 数据修改了进行提交
        await conn.commit()

        # 1.3 关闭
        await cs1.close()
        conn.close()

        # 3. 返回一个json格式的数据,直接返回一个字典
        self.write({"data": "添加成功"})

    # put,delete这个数据都是在body中获取数据
    async def put(self):
        # 1.得到前端传过来的body数据
        # 2.进行解码
        # 3.把字符串转成字典
        # 4.更新数据库操作
        # 5.返回对应的数据

        # 1.得到前端传过来的body数据
        decode_body = self.request.body.decode("utf-8")
        # 2.进行解码
        # 3.把字符串转成字典
        params_dict = json.loads(decode_body)

        print(params_dict)
        # 4.更新数据库操作
        # 1. 从数据库得到数据
        # 1.1连接数据库
        # 创建Connection连接
        conn = await aiomysql.connect(host='localhost', port=1433, db='lrdb', user='liurui1',
                                      password='10086',
                                      charset='utf8')
        # 获得Cursor对象
        cs1 = await conn.cursor()

        # 1.2 执行查询的sql语句
        # btitle,bauthor,bperson,bpub_date,bread,bcomment
        await cs1.execute(
            "update books set btitle=%(btitle)s,bauthor=%(bauthor)s,bperson=%(bperson)s,bpub_date=%(bpub_date)s,bread=%(bread)s,bcomment=%(bcomment)s where id = %(id)s",
            params_dict)

        # 提交
        await conn.commit()

        # 1.3 关闭
        await cs1.close()
        conn.close()
        # 5.返回对应的数据

        self.write({"data": "更新成功"})

    async def delete(self):
        # 1.得到前端的数据
        # 2.解码
        # 3. 转成字典
        # 4. 执行删除的操作
        # 5. 返回数据

        # 1.得到前端的数据
        # 2.解码
        decode_body = self.request.body.decode("utf-8")
        # 3. 转成字典
        params_dict = json.loads(decode_body)
        # 4. 执行删除的操作
        # 1. 从数据库得到数据
        # 1.1连接数据库
        # 创建Connection连接
        # await --> yield from
        conn = await aiomysql.connect(host='localhost', port=1433, db='lrdb', user='liurui1',
                                      password='10086',
                                      charset='utf8')
        # 获得Cursor对象
        cs1 = await conn.cursor()

        # 1.2 执行查询的sql语句
        await cs1.execute("delete from books where id = %(id)s;", params_dict)

        # 提交
        await conn.commit()

        # 1.3 关闭
        await cs1.close()
        conn.close()
        # 5. 返回数据
        self.write({"data": "删除成功"})


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
