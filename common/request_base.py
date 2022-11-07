# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#   1.封装requests公共请求方法
# 预期结果:
#   1.所有不同类型请求方式的接口调用requests公共请求方法，可以请求成功
#   2.显示请求内容，响应内容
# 脚本作者: 林德浩
# 写作日期: 2022/11/2 14:53

import requests
import log_base


class RequestsCommon:

    @classmethod
    def requests(self, method: str, url, params=None, data=None, json=None, timeout=None, **kwargs):
        method = method.upper()
        if method == 'GET':
            res = requests.get(url, params, timeout=timeout, **kwargs)
            return res.text

        elif method == 'POST':
            if data:
                res = requests.get(url, data, timeout=timeout, **kwargs)
                return res.text
            elif json:
                res = requests.get(url, data, timeout=timeout, **kwargs)
                return res.text

        elif method == 'DELETE':
            res = requests.delete(url, timeout=timeout, *kwargs)
            return res.text

        elif method == 'PATCH':
            res = requests.patch(url, data, timeout=timeout, *kwargs)
            return res.text

        elif method == 'PUT':
            res = requests.put(url, data, timeout=timeout, *kwargs)
            return res.text

        elif method == 'OPTIONS':
            res = requests.options(url, timeout=timeout, *kwargs)
            return res.text

        elif method == 'HEAD':
            res = requests.head(url, timeout=timeout, *kwargs)
            return res.text

            try:
                log_base.LogCommon.console_file(f'请求url:{url},请求参数:{params},响应结果:{res.text}')
            except Exception as a:
                log_base.LogCommon.console_file(a)

#
# if __name__ == '__main__':
#     url = "http://47.100.175.62:3000/api/v1/topics"
#     res = RequestsCommon.requests(method='get', url=url)
#     log_base.LogCommon().console_file(res)
