"""
爬虫最基本思路流程：

    一、数据来源分析
        车票信息数据内容
        1.F12或者鼠标右键点击检查选择network，然后刷新一下网页数据，让我们的数据包重新加载出来
        2.通过搜索数据，找到相应的数据包，然后查看url地址、请求方式，以及请求头参数

    二、代码实现的过程
        1.发送请求，对于刚刚分析得到url地址发送请求
        2.获取数据，获取服务器返回响应数据
        3.解析数据，提取我们想要的数据内容
        4.格式化输出效果
"""
import json
import requests
import prettytable as pt


# -------------------查票------------------------
f = open('../file/city.json', encoding='UTF-8')  # 获得所有城市三字码
txt = f.read()  # <class 'str'>
json_data = json.loads(txt)  # 转成字典数据类型
# from_station = input("输入起始站：")
from_station = '芜湖'
# to_station = input("输入终点站：")
to_station = '南京'
# date = input("输入出发的日期，例如：2022-06-01:")
date = "2022-06-02"
# print(json_data[from_station])
# print(json_data[to_station])
"""
发送请求，对于刚刚分析得到url地址发送请求
    python爬虫发送请求：模拟浏览器对于url地址发送请求
请求头:伪装python代码，让它伪装一个浏览器去发送请求
    字典的数据类型，构建完整键值对形式
    User-Agent:用户代理，浏览器基本身份标识
    Cookie:用户信息，常用于检测是否登陆账号
当你请求数据之后，虽然返回<Response [200]> 但是不一定得到你想要数据内容，得到的数据不是想要的说明被反爬了
"""
# 1. 发送请求
url = rf'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={json_data[from_station]}&leftTicketDTO.to_station={json_data[to_station]}&purpose_codes=ADULT'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'Cookie': 'tk=nj4PLPnmG9D7keAGJUvf0Yf80Mg-lihM3FLSliyUbckdqy1y0; JSESSIONID=FAB972504CFF092EEDE0E78184C267D0; RAIL_EXPIRATION=1654343693176; RAIL_DEVICEID=W0vXXJk1MdXF7w_nSim2QG7Vc1PW4iV2Q9urKoe_R_8PjKgoaBycVcOvbfR3z6N_7xh_MWGqHcAazNKcRyrBxT19t_2f2qCFzpaX1XVg1cCSAQxTSMyXaNldj7_DrWDbSexEh2bpMlCpk0eNvDT_20Asu_FdGCv_; BIGipServerpool_passport=98828810.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerpassport=837288202.50215.0000; BIGipServerotn=1675165962.50210.0000; _jc_save_fromStation=%u829C%u6E56%2CWHH; _jc_save_toStation=%u5357%u4EAC%2CNJH; _jc_save_toDate=2022-06-01; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2022-06-02'
}
# 通过requests数据请求模块里面get请求方法，对于url地址发送请求，并且携带上headers请求头伪装，最后用response变量接收返回数据
response = requests.get(url=url, headers=headers)
# print(response)  # <Response [200]> 请求成功，返回响应对象

# 2. 获取数据
print(response.json())  # 报错，不是完整json数据格式，因为没有加Cookie，加了Cookie获得完整数据

# 3. 解析数据，提取我们想要的数据内容
tb = pt.PrettyTable()
tb.field_names = [
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等座',
    '二等座',
    '软卧',
    '硬卧',
    '硬座',
    '无座'
]

page = 1
for index in response.json()['data']['result']:  # 把列表里面的元素提取出来
    # index.split('|')  字符串分割，以 | 进行分割，返回列表
    info = (index.split('|'))
    num = info[3]  # 车次
    start_time = info[8]  # 出发时间
    end_time = info[9]  # 到达时间
    use_time = info[10]  # 耗时
    soft_sleep = info[23]  # 软卧
    hard_sleep = info[28]  # 硬卧
    topGrade = info[32]  # 特等座
    first_class = info[31]  # 一等座
    second_class = info[30]  # 二等座
    hard_seat = info[29]  # 硬座
    no_seat = info[26]  # 无座
    tb.add_row([
        page,
        num,
        start_time,
        end_time,
        use_time,
        topGrade,
        first_class,
        second_class,
        soft_sleep,
        hard_sleep,
        hard_seat,
        no_seat
    ])
    page += 1

# 4.格式化输出效果
print(tb)

# --------抢票---------
choose = input("请选择你想要购买的车票：")
# 进行买票
import GetTicket
GetTicket.get_ticket(int(choose), from_station, to_station, date)

