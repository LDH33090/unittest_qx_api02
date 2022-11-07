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
import json
import random

import requests
import log_base


class RequestsCommon:

    def __init__(self):
        pass

    # 封装 get方法
    @classmethod
    def setGet(self, method: str, url, params=None, timeout=None, **kwargs):
        method = method.upper()
        if method == 'GET':
            try:
                res = requests.get(url, params, timeout, **kwargs)
                log_base.LogCommon().console_file_info(
                    f'请求url:{res.url},请求方法:{method},请求头{res.headers},\n请求参数:{params},响应结果:{res.content.decode()}')
                return res
            except ConnectionError as a:
                log_base.LogCommon().console_file_error(f'请求失败{a}')
                return False

    # 封装post方法
    @classmethod
    def setPost(self, method: str, url, data=None, json=None, timeout=None, **kwargs):
        method = method.upper()
        if method == 'POST':
            if data:
                res = requests.post(url, data, **kwargs)
                log_base.LogCommon().console_file_info(
                    f'请求url:{res.url},请求方法:{method},请求头{res.headers},\n请求参数:{data},\n响应结果:{res.content.decode()}')
                return res
            elif json:
                try:
                    res = requests.post(url, json, timeout, **kwargs)
                    log_base.LogCommon().console_file_info(
                        f'请求url:{res.url},请求方法:{method},请求头{res.headers},\n请求参数:{json},\n响应结果:{res.content.decode()}')
                except ConnectionError as a:
                    log_base.LogCommon().console_file_error(f'请求失败{a}')
                    return False

    # 封装 delete方法
    @classmethod
    def setDelete(self, method: str, url, **kwargs):
        method = method.upper()
        if method == 'DELETE':
            try:
                res = requests.delete(url, **kwargs)
                log_base.LogCommon().console_file_info(
                    f'请求url:{url},请求方法:{method},请求头{res.headers},\n请求参数:{json},\n响应结果:{res.content.decode()}')
                return res
            except ConnectionError as a:
                log_base.LogCommon().console_file_error(f'请求失败{a}')
                return False
            else:
                log_base.LogCommon().console_file_error(f'请求失败{TimeoutError}')
                return False

    # 封装 put方法
    @classmethod
    def setPut(self, method: str, url, data=None, **kwargs):
        method = method.upper()
        if method == 'PUT':
            try:
                res = requests.put(url, data, **kwargs)
                log_base.LogCommon().console_file_info(
                    f'请求url:{url},请求方法:{method},请求头{res.headers},\n请求参数:{data},\n响应结果:{res.content.decode()}')
                return res
            except ConnectionError as a:
                log_base.LogCommon().console_file_error(f'请求失败{a}')
                return False
            else:
                log_base.LogCommon().console_file_error(f'请求失败{TimeoutError}')
                return False

    # 封装option方法
    def setOption(self, method: str, url, **kwargs):
        method = method.upper()
        if method == 'OPTIONS':
            try:
                res = requests.options(url, **kwargs)
                log_base.LogCommon().console_file_info(
                    f'请求url:{url},请求方法:{method},请求头{res.headers},响应结果:{res.content.decode()}')
                return res
            except ConnectionError as a:
                log_base.LogCommon().console_file_error(f'请求失败{a}')
                return False
            else:
                log_base.LogCommon().console_file_error(f'请求失败{TimeoutError}')
                return False

    # 封装patch方法
    def setPatch(self, method: str, url, data=None, **kwargs):
        method = method.upper()
        if method == 'PATCH':
            try:
                res = requests.patch(url, data, **kwargs)
                log_base.LogCommon().console_file_info(
                    f'请求url:{url},请求方法:{method},请求头{res.headers},\n请求参数{data},\n响应结果:{res.content.decode()}')
                return res
            except ConnectionError as a:
                log_base.LogCommon().console_file_error(f'请求失败{a}')
                return False
            else:
                log_base.LogCommon().console_file_error(f'请求失败{TimeoutError}')
                return False


if __name__ == '__main__':
    pass
