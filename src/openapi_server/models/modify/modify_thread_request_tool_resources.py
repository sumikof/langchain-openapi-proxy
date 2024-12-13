# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.create_assistant.create_assistant_request_tool_resources_code_interpreter import CreateAssistantRequestToolResourcesCodeInterpreter
from openapi_server.models.modify.modify_thread_request_tool_resources_file_search import ModifyThreadRequestToolResourcesFileSearch
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ModifyThreadRequestToolResources(BaseModel):
    """
    A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs. 
    """ # noqa: E501
    code_interpreter: Optional[CreateAssistantRequestToolResourcesCodeInterpreter] = None
    file_search: Optional[ModifyThreadRequestToolResourcesFileSearch] = None
    __properties: ClassVar[List[str]] = ["code_interpreter", "file_search"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModifyThreadRequestToolResources from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of code_interpreter
        if self.code_interpreter:
            _dict['code_interpreter'] = self.code_interpreter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_search
        if self.file_search:
            _dict['file_search'] = self.file_search.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ModifyThreadRequestToolResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code_interpreter": CreateAssistantRequestToolResourcesCodeInterpreter.from_dict(obj.get("code_interpreter")) if obj.get("code_interpreter") is not None else None,
            "file_search": ModifyThreadRequestToolResourcesFileSearch.from_dict(obj.get("file_search")) if obj.get("file_search") is not None else None
        })
        return _obj


