"""
    LanXin+ OpenAPI

    LanXin+ OpenAPI Platform  # noqa: E501

    Generated by: https://openapi.lanxin.cn
"""


import re  # noqa: F401
import sys  # noqa: F401

from lanxinplus_openapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from lanxinplus_openapi.exceptions import ApiAttributeError


def lazy_import():
    from lanxinplus_openapi.model.push_data import PushData
    globals()['PushData'] = PushData


class Event(ModelNormal):
    """NOTE: This class is auto generated by LanXin+.
    Ref: https://openapi.lanxin.cn

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'channelType': (int,),  # noqa: E501
            'deviceType': (int,),  # noqa: E501
            'entryId': (str,),  # noqa: E501
            'eventData': (str,),  # noqa: E501
            'eventType': (str,),  # noqa: E501
            'expires': (int,),  # noqa: E501
            'pushData': (PushData,),  # noqa: E501
            'receiverIds': ([str],),  # noqa: E501
            'version': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'channelType': 'channelType',  # noqa: E501
        'deviceType': 'deviceType',  # noqa: E501
        'entryId': 'entryId',  # noqa: E501
        'eventData': 'eventData',  # noqa: E501
        'eventType': 'eventType',  # noqa: E501
        'expires': 'expires',  # noqa: E501
        'pushData': 'pushData',  # noqa: E501
        'receiverIds': 'receiverIds',  # noqa: E501
        'version': 'version',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Event - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            channelType (int): 通道类型. [optional]  # noqa: E501
            deviceType (int): 推送的目标设备类型：1: android, 2: ios, 4: windows, 8: mac, 16: linux 类似于channelType字段，该字段也支持或运算符( | )。如果不填或者将该字段置0， 那么开平会将该事件推送到所有的登录设备。. [optional]  # noqa: E501
            entryId (str): 应用的入口ID（主要用于微应用）. [optional]  # noqa: E501
            eventData (str): 事件内容，系统预定义的事件-工作台角标参数参见下面数据类型与数据格式定义。对应用自定义事件，此内容由应用服务端与应用客户端沟通协商确定，蓝信开放平台不关心具体内容。. [optional]  # noqa: E501
            eventType (str): 事件类型，目前支持的系统预定义事件有工作台红点:app_changes。 对应用自定义事件数据类型拼接的建议规则 “应用type_场景type_场景Id(openid)” 应用自定义类型，应用内区分不同的事件类型，由应用自行决定具体值（接口透传该值）。. [optional]  # noqa: E501
            expires (int): 事件的过期时间，单位是秒。默认值为0是表示永不过期。如果设置指定过期时间（非0），则应用需要实现事件拉取的回调接口。. [optional]  # noqa: E501
            pushData (PushData): [optional]  # noqa: E501
            receiverIds ([str]): 接收者的open staffId列表. [optional]  # noqa: E501
            version (int): 可选字段，数据的版本号，要求是个时间戳，精确到微秒， 例如：1605693953610320. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys:
                        # self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Event - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            channelType (int): 通道类型. [optional]  # noqa: E501
            deviceType (int): 推送的目标设备类型：1: android, 2: ios, 4: windows, 8: mac, 16: linux 类似于channelType字段，该字段也支持或运算符( | )。如果不填或者将该字段置0， 那么开平会将该事件推送到所有的登录设备。. [optional]  # noqa: E501
            entryId (str): 应用的入口ID（主要用于微应用）. [optional]  # noqa: E501
            eventData (str): 事件内容，系统预定义的事件-工作台角标参数参见下面数据类型与数据格式定义。对应用自定义事件，此内容由应用服务端与应用客户端沟通协商确定，蓝信开放平台不关心具体内容。. [optional]  # noqa: E501
            eventType (str): 事件类型，目前支持的系统预定义事件有工作台红点:app_changes。 对应用自定义事件数据类型拼接的建议规则 “应用type_场景type_场景Id(openid)” 应用自定义类型，应用内区分不同的事件类型，由应用自行决定具体值（接口透传该值）。. [optional]  # noqa: E501
            expires (int): 事件的过期时间，单位是秒。默认值为0是表示永不过期。如果设置指定过期时间（非0），则应用需要实现事件拉取的回调接口。. [optional]  # noqa: E501
            pushData (PushData): [optional]  # noqa: E501
            receiverIds ([str]): 接收者的open staffId列表. [optional]  # noqa: E501
            version (int): 可选字段，数据的版本号，要求是个时间戳，精确到微秒， 例如：1605693953610320. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys:
                        # self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")