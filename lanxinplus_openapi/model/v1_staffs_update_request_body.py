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
    from lanxinplus_openapi.model.introduction import Introduction
    from lanxinplus_openapi.model.mobile_phone import MobilePhone
    from lanxinplus_openapi.model.resume import Resume
    from lanxinplus_openapi.model.u_department import UDepartment
    globals()['Introduction'] = Introduction
    globals()['MobilePhone'] = MobilePhone
    globals()['Resume'] = Resume
    globals()['UDepartment'] = UDepartment


class V1StaffsUpdateRequestBody(ModelNormal):
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
            'address': (str,),  # noqa: E501
            'avatarId': (str,),  # noqa: E501
            'birthdate': (str,),  # noqa: E501
            'career': ([Resume],),  # noqa: E501
            'departments': ([UDepartment],),  # noqa: E501
            'duties': (str,),  # noqa: E501
            'education': ([Resume],),  # noqa: E501
            'email': (str,),  # noqa: E501
            'employeeNumber': (str,),  # noqa: E501
            'extAttr1': (str,),  # noqa: E501
            'extAttr2': (str,),  # noqa: E501
            'externalId': (str,),  # noqa: E501
            'extraFieldSet': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'extraPhones': ([MobilePhone],),  # noqa: E501
            'gender': (int,),  # noqa: E501
            'idNumber': (str,),  # noqa: E501
            'introduction': (Introduction,),  # noqa: E501
            'loginName': (str,),  # noqa: E501
            'loginWays': ([int],),  # noqa: E501
            'mobilePhone': (MobilePhone,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'nationality': (str,),  # noqa: E501
            'nativePlace': (str,),  # noqa: E501
            'parties': (str,),  # noqa: E501
            'signature': (str,),  # noqa: E501
            'status': (int,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address': 'address',  # noqa: E501
        'avatarId': 'avatarId',  # noqa: E501
        'birthdate': 'birthdate',  # noqa: E501
        'career': 'career',  # noqa: E501
        'departments': 'departments',  # noqa: E501
        'duties': 'duties',  # noqa: E501
        'education': 'education',  # noqa: E501
        'email': 'email',  # noqa: E501
        'employeeNumber': 'employeeNumber',  # noqa: E501
        'extAttr1': 'extAttr1',  # noqa: E501
        'extAttr2': 'extAttr2',  # noqa: E501
        'externalId': 'externalId',  # noqa: E501
        'extraFieldSet': 'extraFieldSet',  # noqa: E501
        'extraPhones': 'extraPhones',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'idNumber': 'idNumber',  # noqa: E501
        'introduction': 'introduction',  # noqa: E501
        'loginName': 'loginName',  # noqa: E501
        'loginWays': 'loginWays',  # noqa: E501
        'mobilePhone': 'mobilePhone',  # noqa: E501
        'name': 'name',  # noqa: E501
        'nationality': 'nationality',  # noqa: E501
        'nativePlace': 'nativePlace',  # noqa: E501
        'parties': 'parties',  # noqa: E501
        'signature': 'signature',  # noqa: E501
        'status': 'status',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """V1StaffsUpdateRequestBody - a model defined in OpenAPI

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
            address (str): 人员(办公)地址. [optional]  # noqa: E501
            avatarId (str): 人员在蓝信里的头像. [optional]  # noqa: E501
            birthdate (str): 出生日期。格式：yyyy-mm-dd. [optional]  # noqa: E501
            career ([Resume]): 职业 日期格式：yyyy-mm-dd. [optional]  # noqa: E501
            departments ([UDepartment]): 人员所在分支，含分支Id和人员在分支里的排序。人员在分支下排序的序号，不确定时可填0，服务端为忽略0值。有效值从1开始. [optional]  # noqa: E501
            duties (str): 职务. [optional]  # noqa: E501
            education ([Resume]): 教育程度 日期格式：yyyy-mm-dd. [optional]  # noqa: E501
            email (str): 电子邮箱地址. [optional]  # noqa: E501
            employeeNumber (str): 人员号. [optional]  # noqa: E501
            extAttr1 (str): 扩展字段. [optional]  # noqa: E501
            extAttr2 (str): 扩展字段. [optional]  # noqa: E501
            externalId (str): [optional]  # noqa: E501
            extraFieldSet ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): 自定义扩展属性，k代表扩展字段id。. [optional]  # noqa: E501
            extraPhones ([MobilePhone]): 附加联系方式. [optional]  # noqa: E501
            gender (int): 性别：0-保密， 1-男， 2-女. [optional]  # noqa: E501
            idNumber (str): 身份证号. [optional]  # noqa: E501
            introduction (Introduction): [optional]  # noqa: E501
            loginName (str): 人员使用人员名登录蓝信时的人员名，也称staffId。可由组织在创建时指定，并代表一定含义比如工号，创建后不可修改，组织内必须唯一。. [optional]  # noqa: E501
            loginWays ([int]): 蓝信登录方式：0-手机号， 1-邮箱， 2-账密。不填时默认手机号且手机号不能为空. [optional]  # noqa: E501
            mobilePhone (MobilePhone): [optional]  # noqa: E501
            name (str): 人员姓名. [optional]  # noqa: E501
            nationality (str): 民族. [optional]  # noqa: E501
            nativePlace (str): 籍贯. [optional]  # noqa: E501
            parties (str): 党派. [optional]  # noqa: E501
            signature (str): 签名. [optional]  # noqa: E501
            status (int): 成员状态, 更新时允许值 ：NORMAL= 1, 已注册; FROZEN = 2, 冻结. [optional]  # noqa: E501
            tags ([str]): 人员标签信息. [optional]  # noqa: E501
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
        """V1StaffsUpdateRequestBody - a model defined in OpenAPI

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
            address (str): 人员(办公)地址. [optional]  # noqa: E501
            avatarId (str): 人员在蓝信里的头像. [optional]  # noqa: E501
            birthdate (str): 出生日期。格式：yyyy-mm-dd. [optional]  # noqa: E501
            career ([Resume]): 职业 日期格式：yyyy-mm-dd. [optional]  # noqa: E501
            departments ([UDepartment]): 人员所在分支，含分支Id和人员在分支里的排序。人员在分支下排序的序号，不确定时可填0，服务端为忽略0值。有效值从1开始. [optional]  # noqa: E501
            duties (str): 职务. [optional]  # noqa: E501
            education ([Resume]): 教育程度 日期格式：yyyy-mm-dd. [optional]  # noqa: E501
            email (str): 电子邮箱地址. [optional]  # noqa: E501
            employeeNumber (str): 人员号. [optional]  # noqa: E501
            extAttr1 (str): 扩展字段. [optional]  # noqa: E501
            extAttr2 (str): 扩展字段. [optional]  # noqa: E501
            externalId (str): [optional]  # noqa: E501
            extraFieldSet ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): 自定义扩展属性，k代表扩展字段id。. [optional]  # noqa: E501
            extraPhones ([MobilePhone]): 附加联系方式. [optional]  # noqa: E501
            gender (int): 性别：0-保密， 1-男， 2-女. [optional]  # noqa: E501
            idNumber (str): 身份证号. [optional]  # noqa: E501
            introduction (Introduction): [optional]  # noqa: E501
            loginName (str): 人员使用人员名登录蓝信时的人员名，也称staffId。可由组织在创建时指定，并代表一定含义比如工号，创建后不可修改，组织内必须唯一。. [optional]  # noqa: E501
            loginWays ([int]): 蓝信登录方式：0-手机号， 1-邮箱， 2-账密。不填时默认手机号且手机号不能为空. [optional]  # noqa: E501
            mobilePhone (MobilePhone): [optional]  # noqa: E501
            name (str): 人员姓名. [optional]  # noqa: E501
            nationality (str): 民族. [optional]  # noqa: E501
            nativePlace (str): 籍贯. [optional]  # noqa: E501
            parties (str): 党派. [optional]  # noqa: E501
            signature (str): 签名. [optional]  # noqa: E501
            status (int): 成员状态, 更新时允许值 ：NORMAL= 1, 已注册; FROZEN = 2, 冻结. [optional]  # noqa: E501
            tags ([str]): 人员标签信息. [optional]  # noqa: E501
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