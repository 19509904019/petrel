# coding=gbk
import urllib.request as r

# ���ڻ�վʹ�������룬����������Ҫ�Ȼ�ȡվ���Ӧ��������
code_url = r"https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
code_data = r.urlopen(code_url).read().decode('utf-8')


# print(code_data)

# �����õ��ַ����������ֵ�����
def zip_dic(code_data):
    code_data = code_data[20:]
    # print(code_data)
    list_code = code_data.split("|")
    # print(list_code)
    a = 1
    b = 2
    t1 = []
    t2 = []
    while (a < (len(list_code))):
        t1.append(list_code[a])
        t2.append(list_code[b])
        a = a + 5
        b = b + 5
    dic = dict(zip(t1, t2))
    return dic


code_dic = zip_dic(code_data)


# print(code_dic)

# ���庯�����û�������ʼվ�յ�վ��ʱ�䣬ת��Ϊ����������
def get_message(code_dic):
    from_station = input("������ʼվ��\n")
    to_station = input("�����յ�վ��\n")
    time = input("����ʱ�䣬���磺2020-4-28:\n")
    for key, value in code_dic.items():
        if (key == from_station):
            from_station = value
        if (key == to_station):
            to_station = value
    return from_station, to_station, time


if __name__ == '__main__':
    from_station, to_station, time = get_message(code_dic)
    # print(from_station,to_station,time)

    train_url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(
        time, from_station, to_station)

    print(train_url)
