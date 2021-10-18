
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.addrbk_department_api import AddrbkDepartmentApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from lanxinplus_openapi.api.addrbk_department_api import AddrbkDepartmentApi
from lanxinplus_openapi.api.addrbk_staff_api import AddrbkStaffApi
from lanxinplus_openapi.api.addrbk_tags_api import AddrbkTagsApi
from lanxinplus_openapi.api.appmge_api import AppmgeApi
from lanxinplus_openapi.api.auth_api import AuthApi
from lanxinplus_openapi.api.media_api import MediaApi
from lanxinplus_openapi.api.message_api import MessageApi
from lanxinplus_openapi.api.org_api import OrgApi
from lanxinplus_openapi.api.role_api import RoleApi
