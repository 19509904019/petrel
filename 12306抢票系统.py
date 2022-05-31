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
import requests  # 数据请求模块
import prettytable as pt  # 表格格式的输出
import urllib.request as r

# 由于火车站使用三字码，所以我们需要先获取站点对应的三字码
code_url = r"https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
code_data = r.urlopen(code_url).read().decode('utf-8')

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
url = r'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-06-01&leftTicketDTO.from_station=NKH&leftTicketDTO.to_station=ENH&purpose_codes=ADULT'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'Cookie': '_uab_collina=165400073607379238874316; JSESSIONID=E0CC58164BAC46E4FA1D11C1D4BB4B21; RAIL_EXPIRATION=1654288609235; RAIL_DEVICEID=DVZzIsY_rjCELsAKZ32A2Glrd4Y5sHsdWc7tPqJOgvp8OLK4VT-FKv1vtbAwKHpyTvpBbsxzfucbRMNO0704vCqGu1quu0ADREQTRyrZvsvUbUNdTB8FTKAlUVXORTsVd4ojbjBnBArF12a7NmzUtw52GXBO9UeA; BIGipServerpassport=954728714.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=9036359bb8a8a461c164a04f8f50b252; _jc_save_toDate=2022-05-31; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5357%u4EAC%u5357%2CNKH; _jc_save_toStation=%u5408%u80A5%u5357%2CENH; _jc_save_fromDate=2022-06-01; BIGipServerotn=3788964106.50210.0000'
}
# 通过requests数据请求模块里面get请求方法，对于url地址发送请求，并且携带上headers请求头伪装，最后用response变量接收返回数据
response = requests.get(url=url, headers=headers)
# print(response)  # <Response [200]> 请求成功，返回响应对象

# 2. 获取数据
# print(response.json())  # 报错，不是完整json数据格式，因为没有加Cookie，加了Cookie获得完整数据

# 3. 解析数据，提取我们想要的数据内容
tb = pt.PrettyTable()
tb.field_names = [
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '软卧',
    '硬卧',
    '特等座',
    '一等座',
    '二等座',
    '硬座',
    '无座'
]
for index in response.json()['data']['result'][2:]:  # 把列表里面的元素提取出来
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
    dit = {
        '车次': num,
        '出发时间': start_time,
        '到达时间': end_time,
        '耗时': use_time,
        '软卧': soft_sleep,
        '硬卧': hard_sleep,
        '特等座': topGrade,
        '一等座': first_class,
        '二等座': second_class,
        '硬座': hard_seat,
        '无座': no_seat
    }
    # print(dit)
    tb.add_row([
        num,
        start_time,
        end_time,
        use_time,
        soft_sleep,
        hard_sleep,
        topGrade,
        first_class,
        second_class,
        hard_seat,
        no_seat
    ])
print(tb)

# 4.格式化输出效果
