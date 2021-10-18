# 蓝信 Python SDK

## 关于
> - 此Python SDK基于[蓝信开放平台API]构建
> - 蓝信开放平台，便于企业应用与蓝信集成，让协同与管理更加高效
> - 蓝信开放接口SDK，便捷调用服务端API，例如：认证授权、通讯录、消息通知、角色权限、媒体素材、组织管理、应用管理等具体可以访问 [蓝信开放平台API] 文档 看看

## 运行环境
> - Python >= 3.6

## 安装方法
> - 通过pip安装官方发布的版本（以Linux系统为例）：
```sh
pip install lanxinplus_openapi
```

> - 也可下载源码包，执行安装命令：
```sh
sudo python setup.py install
```

## 快速使用
#### 获取 APP_TOKEN
```python
# -*- coding: utf-8 -*-

import lanxinplus_openapi
from lanxinplus_openapi.api import auth_api

config = lanxinplus_openapi.Configuration(
    host = "https://example.com/open/apigw", app_id="", app_secret=""
)

with lanxinplus_openapi.ApiClient(config) as api_client:
    lanxinplus_openapi.Configuration.set_default(config)
    try:
        authApi = auth_api.AuthApi(api_client)
        resp = authApi.v1_app_token_create("client_credential", config.app_id, config.app_secret)
        print(resp)
    except lanxinplus_openapi.ApiException as e:
        print("Exception when calling AuthApi->v1_apptoken_create_get: %s\n" % e)
```

## 测试用例使用说明
#### 运行test
```bash
nosetests -s test/test_auth_api.py:TestAuthApi.test_v1_app_token_create
```

## 联系我们
- [蓝信官方网站](https://www.lanxin.cn/)
- [蓝信开放平台文档中心](https://openapi.lanxin.cn/doc/#/)

[蓝信开放平台API]: https://openapi.lanxin.cn/doc/#/server-api/
