# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用[名片管理系统]V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("退出系统:[0]")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ:")
    email_str = input("请输入邮箱:")

    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}
    # 将名片字典追加到列表中
    card_list.append(card_dict)
    print("添加%s的名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在记录
    if len(card_list) == 0:
        print("当前无记录")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")
    print("")
    print("=" * 50)
    for dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (dict["name"], dict["phone"], dict["qq"], dict["email"]))

    print("=" * 50)


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要搜索的姓名: ")
    for dict in card_list:
        if dict["name"] == find_name:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (dict["name"], dict["phone"], dict["qq"], dict["email"]))
            print("=" * 50)
            deal_card(dict)


    else:
        print("没有找到%s" % find_name)


def deal_card(find_dict):
    """
    处理查找到的名片
    :param find_dict: 查找到的字典
    """
    print("修改:1 删除:2 返回上级:0 ")
    action_str = input("请输入您要进行的操作:")
    if action_str in ["1", "2", "0"]:
        if action_str == "1":
            find_dict["name"] = input_card_info(find_dict["name"], "姓名: ")
            find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
            find_dict["qq"] = input_card_info(find_dict["qq"], "qq: ")
            find_dict["email"] = input_card_info(find_dict["email"], "邮箱: ")
            print("修改名片成功")
        elif action_str == "2":
            card_list.remove(find_dict)
            print("删除名片")


def input_card_info(dict_value, tip_massage):
    """
    对修改做的升级函数
    :param dict_value: 字典中原来的值
    :param tip_massage: 提示信息
    """
    result_str = input(tip_massage)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
