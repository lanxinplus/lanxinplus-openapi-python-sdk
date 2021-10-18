# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from lanxinplus_openapi.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from lanxinplus_openapi.model.ancestor_department import AncestorDepartment
from lanxinplus_openapi.model.app_roaming_org_list import AppRoamingOrgList
from lanxinplus_openapi.model.base_response import BaseResponse
from lanxinplus_openapi.model.department import Department
from lanxinplus_openapi.model.department_data import DepartmentData
from lanxinplus_openapi.model.department_staff_info import DepartmentStaffInfo
from lanxinplus_openapi.model.event import Event
from lanxinplus_openapi.model.extra_field_id import ExtraFieldId
from lanxinplus_openapi.model.group_info_tag import GroupInfoTag
from lanxinplus_openapi.model.introduction import Introduction
from lanxinplus_openapi.model.mobile_phone import MobilePhone
from lanxinplus_openapi.model.push_data import PushData
from lanxinplus_openapi.model.resume import Resume
from lanxinplus_openapi.model.role_staff import RoleStaff
from lanxinplus_openapi.model.search_scope import SearchScope
from lanxinplus_openapi.model.search_staff_info import SearchStaffInfo
from lanxinplus_openapi.model.status_info import StatusInfo
from lanxinplus_openapi.model.system_msg import SystemMsg
from lanxinplus_openapi.model.tag_filter import TagFilter
from lanxinplus_openapi.model.tag_meta import TagMeta
from lanxinplus_openapi.model.tag_staff_info import TagStaffInfo
from lanxinplus_openapi.model.u_department import UDepartment
from lanxinplus_openapi.model.v1_app_roaming_orgs_fetch_data import V1AppRoamingOrgsFetchData
from lanxinplus_openapi.model.v1_app_roaming_orgs_fetch_response import V1AppRoamingOrgsFetchResponse
from lanxinplus_openapi.model.v1_app_token_create_data import V1AppTokenCreateData
from lanxinplus_openapi.model.v1_app_token_create_response import V1AppTokenCreateResponse
from lanxinplus_openapi.model.v1_chat_notification_fetch_data import V1ChatNotificationFetchData
from lanxinplus_openapi.model.v1_chat_notification_fetch_response import V1ChatNotificationFetchResponse
from lanxinplus_openapi.model.v1_depts_children_fetch_data import V1DeptsChildrenFetchData
from lanxinplus_openapi.model.v1_depts_children_fetch_response import V1DeptsChildrenFetchResponse
from lanxinplus_openapi.model.v1_depts_create_data import V1DeptsCreateData
from lanxinplus_openapi.model.v1_depts_create_request_body import V1DeptsCreateRequestBody
from lanxinplus_openapi.model.v1_depts_create_response import V1DeptsCreateResponse
from lanxinplus_openapi.model.v1_depts_delete_response import V1DeptsDeleteResponse
from lanxinplus_openapi.model.v1_depts_fetch_data import V1DeptsFetchData
from lanxinplus_openapi.model.v1_depts_fetch_response import V1DeptsFetchResponse
from lanxinplus_openapi.model.v1_depts_staffs_create_response import V1DeptsStaffsCreateResponse
from lanxinplus_openapi.model.v1_depts_staffs_delete_response import V1DeptsStaffsDeleteResponse
from lanxinplus_openapi.model.v1_depts_staffs_fetch_data import V1DeptsStaffsFetchData
from lanxinplus_openapi.model.v1_depts_staffs_fetch_response import V1DeptsStaffsFetchResponse
from lanxinplus_openapi.model.v1_depts_update_request_body import V1DeptsUpdateRequestBody
from lanxinplus_openapi.model.v1_depts_update_response import V1DeptsUpdateResponse
from lanxinplus_openapi.model.v1_js_api_token_create_data import V1JsApiTokenCreateData
from lanxinplus_openapi.model.v1_js_api_token_create_response import V1JsApiTokenCreateResponse
from lanxinplus_openapi.model.v1_medias_create_data import V1MediasCreateData
from lanxinplus_openapi.model.v1_medias_create_response import V1MediasCreateResponse
from lanxinplus_openapi.model.v1_medias_path_fetch_data import V1MediasPathFetchData
from lanxinplus_openapi.model.v1_medias_path_fetch_response import V1MediasPathFetchResponse
from lanxinplus_openapi.model.v1_messages_create_data import V1MessagesCreateData
from lanxinplus_openapi.model.v1_messages_create_request_body import V1MessagesCreateRequestBody
from lanxinplus_openapi.model.v1_messages_create_response import V1MessagesCreateResponse
from lanxinplus_openapi.model.v1_messages_notification_create_data import V1MessagesNotificationCreateData
from lanxinplus_openapi.model.v1_messages_notification_create_request_body import V1MessagesNotificationCreateRequestBody
from lanxinplus_openapi.model.v1_messages_notification_create_response import V1MessagesNotificationCreateResponse
from lanxinplus_openapi.model.v1_messages_revoke_data import V1MessagesRevokeData
from lanxinplus_openapi.model.v1_messages_revoke_request_body import V1MessagesRevokeRequestBody
from lanxinplus_openapi.model.v1_messages_revoke_response import V1MessagesRevokeResponse
from lanxinplus_openapi.model.v1_org_extra_field_ids_fetch_data import V1OrgExtraFieldIdsFetchData
from lanxinplus_openapi.model.v1_org_extra_field_ids_fetch_response import V1OrgExtraFieldIdsFetchResponse
from lanxinplus_openapi.model.v1_org_fetch_data import V1OrgFetchData
from lanxinplus_openapi.model.v1_org_fetch_response import V1OrgFetchResponse
from lanxinplus_openapi.model.v1_org_role_create_data import V1OrgRoleCreateData
from lanxinplus_openapi.model.v1_org_role_create_request_body import V1OrgRoleCreateRequestBody
from lanxinplus_openapi.model.v1_org_role_create_response import V1OrgRoleCreateResponse
from lanxinplus_openapi.model.v1_org_role_members_fetch_data import V1OrgRoleMembersFetchData
from lanxinplus_openapi.model.v1_org_role_members_fetch_response import V1OrgRoleMembersFetchResponse
from lanxinplus_openapi.model.v1_role_member_create_request_body import V1RoleMemberCreateRequestBody
from lanxinplus_openapi.model.v1_role_member_create_response import V1RoleMemberCreateResponse
from lanxinplus_openapi.model.v1_role_member_delete_request_body import V1RoleMemberDeleteRequestBody
from lanxinplus_openapi.model.v1_role_member_delete_response import V1RoleMemberDeleteResponse
from lanxinplus_openapi.model.v1_staffs_create_data import V1StaffsCreateData
from lanxinplus_openapi.model.v1_staffs_create_request_body import V1StaffsCreateRequestBody
from lanxinplus_openapi.model.v1_staffs_create_response import V1StaffsCreateResponse
from lanxinplus_openapi.model.v1_staffs_delete_response import V1StaffsDeleteResponse
from lanxinplus_openapi.model.v1_staffs_dept_ancestors_fetch_data import V1StaffsDeptAncestorsFetchData
from lanxinplus_openapi.model.v1_staffs_dept_ancestors_fetch_response import V1StaffsDeptAncestorsFetchResponse
from lanxinplus_openapi.model.v1_staffs_fetch_data import V1StaffsFetchData
from lanxinplus_openapi.model.v1_staffs_fetch_response import V1StaffsFetchResponse
from lanxinplus_openapi.model.v1_staffs_infor_fetch_data import V1StaffsInforFetchData
from lanxinplus_openapi.model.v1_staffs_infor_fetch_response import V1StaffsInforFetchResponse
from lanxinplus_openapi.model.v1_staffs_update_request_body import V1StaffsUpdateRequestBody
from lanxinplus_openapi.model.v1_staffs_update_response import V1StaffsUpdateResponse
from lanxinplus_openapi.model.v1_tag_groups_create_data import V1TagGroupsCreateData
from lanxinplus_openapi.model.v1_tag_groups_create_request_body import V1TagGroupsCreateRequestBody
from lanxinplus_openapi.model.v1_tag_groups_create_response import V1TagGroupsCreateResponse
from lanxinplus_openapi.model.v1_tag_groups_delete_response import V1TagGroupsDeleteResponse
from lanxinplus_openapi.model.v1_tag_groups_fetch_data import V1TagGroupsFetchData
from lanxinplus_openapi.model.v1_tag_groups_fetch_request_body import V1TagGroupsFetchRequestBody
from lanxinplus_openapi.model.v1_tag_groups_fetch_response import V1TagGroupsFetchResponse
from lanxinplus_openapi.model.v1_tag_groups_info_fetch_data import V1TagGroupsInfoFetchData
from lanxinplus_openapi.model.v1_tag_groups_info_fetch_response import V1TagGroupsInfoFetchResponse
from lanxinplus_openapi.model.v1_tag_groups_update_request_body import V1TagGroupsUpdateRequestBody
from lanxinplus_openapi.model.v1_tag_groups_update_response import V1TagGroupsUpdateResponse
from lanxinplus_openapi.model.v1_tags_create_data import V1TagsCreateData
from lanxinplus_openapi.model.v1_tags_create_request_body import V1TagsCreateRequestBody
from lanxinplus_openapi.model.v1_tags_create_response import V1TagsCreateResponse
from lanxinplus_openapi.model.v1_tags_delete_response import V1TagsDeleteResponse
from lanxinplus_openapi.model.v1_tags_fetch_data import V1TagsFetchData
from lanxinplus_openapi.model.v1_tags_fetch_request_body import V1TagsFetchRequestBody
from lanxinplus_openapi.model.v1_tags_fetch_response import V1TagsFetchResponse
from lanxinplus_openapi.model.v1_tags_meta_fetch_data import V1TagsMetaFetchData
from lanxinplus_openapi.model.v1_tags_meta_fetch_request_body import V1TagsMetaFetchRequestBody
from lanxinplus_openapi.model.v1_tags_meta_fetch_response import V1TagsMetaFetchResponse
from lanxinplus_openapi.model.v1_tags_update_request_body import V1TagsUpdateRequestBody
from lanxinplus_openapi.model.v1_tags_update_response import V1TagsUpdateResponse
from lanxinplus_openapi.model.v1_user_token_create_data import V1UserTokenCreateData
from lanxinplus_openapi.model.v1_user_token_create_response import V1UserTokenCreateResponse
from lanxinplus_openapi.model.v1_users_fetch_data import V1UsersFetchData
from lanxinplus_openapi.model.v1_users_fetch_response import V1UsersFetchResponse
from lanxinplus_openapi.model.v2_chat_notification_update_request_body import V2ChatNotificationUpdateRequestBody
from lanxinplus_openapi.model.v2_chat_notification_update_response import V2ChatNotificationUpdateResponse
from lanxinplus_openapi.model.v2_event_notification_create_request_body import V2EventNotificationCreateRequestBody
from lanxinplus_openapi.model.v2_event_notification_create_response import V2EventNotificationCreateResponse
from lanxinplus_openapi.model.v2_staffs_id_mapping_fetch_data import V2StaffsIdMappingFetchData
from lanxinplus_openapi.model.v2_staffs_id_mapping_fetch_response import V2StaffsIdMappingFetchResponse
from lanxinplus_openapi.model.v2_staffs_search_data import V2StaffsSearchData
from lanxinplus_openapi.model.v2_staffs_search_request_body import V2StaffsSearchRequestBody
from lanxinplus_openapi.model.v2_staffs_search_response import V2StaffsSearchResponse