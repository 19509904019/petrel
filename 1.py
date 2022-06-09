from collections import deque


def find_free_partner(boys, girls, sort_boy_to_girl, sort_girl_to_boy):
    # 当前选择的舞伴
    current_boys = dict(zip(boys, [None] * len(boys)))
    current_girls = dict(zip(girls, [None] * len(girls)))
    # current_boys = {boys[0]:None, boys[1]:None, boys[2]:None, boys[3]:None}
    # current_girls = {girls[0]:None, girls[1]:None, girls[2]:None, boys[3]:None}
    count = len(boys)

    # 建立队列，男孩下一次选择的女孩
    next_select = dict(zip(boys, [None] * len(boys)))
    for i in range(count):
        temp = [girls[m - 1] for m in sort_boy_to_girl[i]]
        next_select[boys[i]] = deque(temp)

    # 女孩选择男孩字典
    sort_girl = dict(zip(girls, [None] * len(boys)))
    for i in range(count):
        # 通过题目给出的sort_girl_to_boy字典,排在前面的名字好感度比较高
        temp = [[boys[m - 1], 4 - ind] for ind, m in enumerate(sort_girl_to_boy[i])]
        name, love = [], []
        for t in temp:
            name.append(t[0])
            love.append(t[1])
        sort_girl[girls[i]] = dict(zip(name, love))

    while None in current_boys.values():
        for i in range(count):
            bid = boys[i]
            if current_boys[bid]:
                # 男孩有对象，跳过
                continue
            else:
                # 优先选择的女孩
                select = next_select[bid][0]
                if current_girls[select] == None:
                    # 女孩没对象，两者结合
                    current_boys[bid] = select
                    current_girls[select] = bid
                    next_select[bid].popleft()
                else:
                    # 和女孩的对象好感度对比,如果对现任的好感度,大于第三者,不动
                    if sort_girl[select][current_girls[select]] > sort_girl[select][bid]:
                        next_select[bid].popleft()
                    # 如果与上面相反
                    # 现任男孩失恋,第三者男孩选择了当前女孩,当前女孩选择了第三者男孩
                    # 第三者男孩失去对当前女孩的追求权(本算法不能对同一女士追求两次)
                    else:
                        current_boys[current_girls[select]] = None
                        current_boys[bid] = select
                        current_girls[select] = bid
                        next_select[bid].popleft()
    return current_boys


## 初始化
boys = ["Alex", "David", "Bob", "Chris"]
girls = ["Ada", "Becky", "Cindy", "Diana"]

# 偏爱列表
sort_boy_to_girl = [[1, 4, 3, 2], [3, 1, 2, 4],
                    [1, 2, 3, 4], [2, 4, 3, 1]]
sort_girl_to_boy = [[4, 1, 3, 2], [1, 2, 4, 3],
                    [3, 2, 4, 1], [2, 3, 1, 4]]

print(find_free_partner(boys, girls, sort_boy_to_girl, sort_girl_to_boy))
