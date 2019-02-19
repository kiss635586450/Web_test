import json
from bottle import get, delete, post, put
from common import convert_helper, web_helper, db_helper, json_helper
@get('/api/product_class/')
def callback():
    """
    获取列表数据
    :return:
    """
    #页面索引
    page_number = convert_helper.to_int1(web_helper.get_query('page', '', False))
    #页面显示记录数量
    page_size = convert_helper.to_int0(web_helper.get_query('row', '', False))
    #排序字段
    sidx = web_helper.get_query('sidx', '', False)
    #顺序还是倒叙排序
    sord = web_helper.get_query('sord', '', False)
    #初始化排序字段
    order_by = 'sort asc'
    if sidx:
        order_by = sidx + '' + sord
    #################################################
    #初始化输出格式（前端使用jqgrid列表，需要指定输出格式）
    data = {
        'records': 0,
        'total': 0,
        'page': 1,
        'rows': [],
    }
    ##############################################
    #执行sql，获取指定条件的记录总数量
    sql = 'select count(1) as records from product_class'
    result = db_helper.read(sql)

    #如果查询失败或不存在指定条件记录，则直接返回初始值
    if not result or result[0]['records'] == 0:
        return data
    #保存总记录数量
    data['records'] = result[0].get('records', 0)

    ##############################################
    #设置分页索引与页面大小
    #设置分页大小
    if page_size is None or page_size <= 0:
        page_size = 10
    #计算总页数
    if data['records'] % page_size == 0:
        page_total = data['records'] // page_size
    else:
        page_total = data['records'] // page_size +1
    #记录总页面数量
    data['total'] = page_total

    #判断提交的页码是否超出范围
    if page_number < 1 or page_number > page_total:
        page_number = page_total
    #记录当前页面索引值
    data['page'] = page_number

    #计算当前页面要显示的记录起始位置
    record_number = (page_number - 1) * page_size
    #设置查询分页条件
    paging = ' limit ' + str(page_size) + ' offset ' + str(record_number)
    ##设置排序
    if not order_by:
        order_by = 'id_desc'
    ##########################################
    #组合sql查询语句
    sql = "select * from product_class order by %(orderby)s %(paging)s" % \
          {'orderby':order_by, 'paging': paging}
    #读取记录
    result = db_helper.read(sql)
    if result:
        #存储记录
        data['rows'] = result
    if data:
        #直接输出json
        return web_helper.return_raise(json.dumps(data, cls=json_helper.CJsonEncoder))
    else:
        return web_helper.return_msg(-1, "查询失败")

@delete('/api/prouct_class/<id:int>/')
def callback(id):
    """
    删除指定记录
    :param id:
    :return:
    """
    #判断该分类是否已经被引用， 是的话不能直接删除
    sql = """select count(*) as total from product where product_class_id=%s"""% (id,)
    #读取记录
    result = db_helper.read(sql)
    if result and result[0].get('total', -1)> 0:
        return web_helper.return_msg(-1, "该分类已经被引用，请清除该分类的绑定后再删除")

    #编辑记录
    sql = """delete from product_class where id=%s returning id"""
    vars = (id,)
    #写入数据库
    result = db_helper.write(sql, vars)
    #判断是否提交成功
    if result:
        return web_helper.return_msg(0, "成功")
    else:
        return web_helper.return_msg(-1, "删除失败")
@post('/api/product_class/')
def callback():
    """
    新增记录
    :return:
    """
    name = web_helper.get_form('name', '分类名称')
    is_enable = convert_helper.to_int0(web_helper.get_form('is_enable', '是否启用'))

    #添加记录（使用returning这个函数能返回指定的字段值，这里要求返回新添加记录的自增ID值）
    sql = """insert into produce_class (name, is_enable) value (%s, %s) returning id"""
    vars = (name, is_enable)
    #写入数据库
    result = db_helper.write(sql, vars)
    #判断是否成功提交
    if result and result[0].get('id'):
        return web_helper.return_msg(0, '成功')
    else:
        return web_helper.return_msg(-1, "提交失败")

@get('/api/product_class/<id:int>')
def callback(id):
    """
    获取指定记录
    :param id:
    :return:
    """
    sql = """select * from produc_class where id = %s""" % (id,)
    #读取记录
    result = db_helper.read(sql)
    if result:
        #直接输出json
        return web_helper.return_msg(0, '成功', result[0])
    else:
        return web_helper.return_msg(-1, "查询失败")

@put('/api/product_class/<id:int>')
def callback(id):
    """
    修改记录
    :param id:
    :return:
    """
    name = web_helper.get_form('name', '分类名称')
    is_enable = convert_helper.to_int0(web_helper.get_form('is_enable', '是否启用'))

    #编辑记录
    sql = """update product_class set name=%s, is_enable=%s where id=%s returning id"""
    vars = (name, is_enable, id)
    #写入数据库
    result = db_helper.write(sql,vars)
    #判断是否成功提交
    if result and result[0].get('id'):
        return web_helper.return_msg(0, '成功')
    else:
        return web_helper.return_msg(-1,"提交失败")
