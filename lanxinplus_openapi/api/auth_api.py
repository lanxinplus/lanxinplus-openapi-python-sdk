"""
    LanXin+ OpenAPI

    LanXin+ OpenAPI Platform  # noqa: E501

    Generated by: https://openapi.lanxin.cn
"""


import re  # noqa: F401
import sys  # noqa: F401

from lanxinplus_openapi.api_client import ApiClient, Endpoint as _Endpoint
from lanxinplus_openapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lanxinplus_openapi.model.v1_app_token_create_response import V1AppTokenCreateResponse
from lanxinplus_openapi.model.v1_js_api_token_create_response import V1JsApiTokenCreateResponse
from lanxinplus_openapi.model.v1_user_token_create_response import V1UserTokenCreateResponse
from lanxinplus_openapi.model.v1_users_fetch_response import V1UsersFetchResponse


class AuthApi(object):
    """NOTE: This class is auto generated by LanXin+
    Ref: https://openapi.lanxin.cn

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.v1_app_token_create_endpoint = _Endpoint(
            settings={
                'response_type': (V1AppTokenCreateResponse,),
                'auth': [],
                'endpoint_path': '/v1/apptoken/create',
                'operation_id': 'v1_app_token_create',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'grant_type',
                    'appid',
                    'secret',
                ],
                'required': [
                    'grant_type',
                    'appid',
                    'secret',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'grant_type':
                        (str,),
                    'appid':
                        (str,),
                    'secret':
                        (str,),
                },
                'attribute_map': {
                    'grant_type': 'grant_type',
                    'appid': 'appid',
                    'secret': 'secret',
                },
                'location_map': {
                    'grant_type': 'query',
                    'appid': 'query',
                    'secret': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_js_api_token_create_endpoint = _Endpoint(
            settings={
                'response_type': (V1JsApiTokenCreateResponse,),
                'auth': [],
                'endpoint_path': '/v1/jsapitoken/create',
                'operation_id': 'v1_js_api_token_create',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'user_token',
                ],
                'required': [
                    'app_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_user_token_create_endpoint = _Endpoint(
            settings={
                'response_type': (V1UserTokenCreateResponse,),
                'auth': [],
                'endpoint_path': '/v1/usertoken/create',
                'operation_id': 'v1_user_token_create',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'grant_type',
                    'code',
                    'redirect_uri',
                ],
                'required': [
                    'app_token',
                    'grant_type',
                    'code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'grant_type':
                        (str,),
                    'code':
                        (str,),
                    'redirect_uri':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'grant_type': 'grant_type',
                    'code': 'code',
                    'redirect_uri': 'redirect_uri',
                },
                'location_map': {
                    'app_token': 'query',
                    'grant_type': 'query',
                    'code': 'query',
                    'redirect_uri': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.v1_users_fetch_endpoint = _Endpoint(
            settings={
                'response_type': (V1UsersFetchResponse,),
                'auth': [],
                'endpoint_path': '/v1/users/fetch',
                'operation_id': 'v1_users_fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_token',
                    'user_token',
                ],
                'required': [
                    'app_token',
                    'user_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'app_token':
                        (str,),
                    'user_token':
                        (str,),
                },
                'attribute_map': {
                    'app_token': 'app_token',
                    'user_token': 'user_token',
                },
                'location_map': {
                    'app_token': 'query',
                    'user_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def v1_app_token_create(
        self,
        grant_type,
        appid,
        secret,
        **kwargs
    ):
        """获取应用访问TOKEN  # noqa: E501

        使用AppId，AppSecret，创建应用访问APP_TOKEN  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_app_token_create(grant_type, appid, secret, async_req=True)
        >>> result = thread.get()

        Args:
            grant_type (str): client_credential
            appid (str): 应用ID
            secret (str): 应用密钥

        Keyword Args:

        Returns:
            V1AppTokenCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['grant_type'] = \
            grant_type
        kwargs['appid'] = \
            appid
        kwargs['secret'] = \
            secret
        return self.v1_app_token_create_endpoint.call_with_http_info(**kwargs)

    def v1_js_api_token_create(
        self,
        app_token,
        **kwargs
    ):
        """获取jsapi访问TOKEN  # noqa: E501

        创建JSAPI访问JS_API_TOKEN，该JS_API_TOKEN用于生成JASPI签名参数，用于JSAPI接口的身份验证  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_js_api_token_create(app_token, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token

        Keyword Args:
            user_token (str): user_token. [optional]

        Returns:
            V1JsApiTokenCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        return self.v1_js_api_token_create_endpoint.call_with_http_info(**kwargs)

    def v1_user_token_create(
        self,
        app_token,
        grant_type,
        code,
        **kwargs
    ):
        """获取人员访问TOKEN  # noqa: E501

        OAuth2 授权流程，通过 OAuth2 授权码获取人员身份访问USER_TOKEN  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_user_token_create(app_token, grant_type, code, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            grant_type (str): 使用固定值 'authorization_code'
            code (str): 人员免登录授权码

        Keyword Args:
            redirect_uri (str): redirect_uri. [optional]

        Returns:
            V1UserTokenCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['grant_type'] = \
            grant_type
        kwargs['code'] = \
            code
        return self.v1_user_token_create_endpoint.call_with_http_info(**kwargs)

    def v1_users_fetch(
        self,
        app_token,
        user_token,
        **kwargs
    ):
        """获取人员基本信息  # noqa: E501

        根据人员token 获取当前端上登录人员信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_users_fetch(app_token, user_token, async_req=True)
        >>> result = thread.get()

        Args:
            app_token (str): app_token
            user_token (str): user_token

        Keyword Args:

        Returns:
            V1UsersFetchResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['app_token'] = \
            app_token
        kwargs['user_token'] = \
            user_token
        return self.v1_users_fetch_endpoint.call_with_http_info(**kwargs)
