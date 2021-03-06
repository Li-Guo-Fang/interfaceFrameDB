# coding=utf-8
from utils.db_handler import DB

#主要就是把储存的结构画出来
class RelyDataStore(object):
    def __init__(self):
        pass

    #store_point
    {"request": ["username", "password"], "response": ["code"]}
    @classmethod
    def do(cls,store_point,api_name,case_id,request_source = {},response_source = {}):
        tem = {"request":{},"response":{}}
        for key,value in store_point.items():
            if key == "request":
                #说明取得是请求参数中的，即使request_source
                for i in value:
                    if i in request_source:
                        val = request_source[i]
                        if api_name not in tem["request"]:
                            tem["request"] = {api_name:{case_id:{i:val}}}
                        elif case_id not in tem["request"][api_name]:
                            tem["request"][api_name] = {case_id:{i:val}}
                        else:
                            tem["request"][api_name][case_id][i]=val
                    else:
                        print("字段[%s]在原始数据request_source中不存在！"%i)
            elif key =="response":
                #说明取的响应body中的字段值，即是response_source
                for i in value:
                    if i in response_source:
                        val = response_source[i]
                        if api_name not in tem["response"]:
                            tem["response"] = {api_name: {case_id: {i: val}}}
                        elif case_id not in tem["response"][api_name]:
                            tem["response"][api_name] = {case_id: {i: val}}
                        else:
                            tem["response"][api_name][case_id][i] = val
                    else:
                        print("字段[%s]在原始数据response_source中不存在！" % i)
        if tem["request"] or tem["response"]:
            db = DB()
            api_id = db.get_api_id(api_name)
            db.update_store_data(api_id,int(case_id),tem)


if __name__ == "__main__":
    store_point = {"request": ["username", "password"], "response": ["userid"]}
    request_source = {"username":"lisi123", "password":"wang1234dsfe","email":"xx@qq.com"}
    response_source = {"userid":12, "code":"00"}
    data = RelyDataStore.do(store_point, "用户注册",2,request_source, response_source)


