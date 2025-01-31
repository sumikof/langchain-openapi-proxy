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




from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_server.models.run.run_step_details_tool_calls_file_search_result_object_content_inner import RunStepDetailsToolCallsFileSearchResultObjectContentInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RunStepDetailsToolCallsFileSearchResultObject(BaseModel):
    """
    A result instance of the file search.
    """ # noqa: E501
    file_id: StrictStr = Field(description="The ID of the file that result was found in.")
    file_name: StrictStr = Field(description="The name of the file that result was found in.")
    score: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="The score of the result. All values must be a floating point number between 0 and 1.")
    content: Optional[List[RunStepDetailsToolCallsFileSearchResultObjectContentInner]] = Field(default=None, description="The content of the result that was found. The content is only included if requested via the include query parameter.")
    __properties: ClassVar[List[str]] = ["file_id", "file_name", "score", "content"]

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
        """Create an instance of RunStepDetailsToolCallsFileSearchResultObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item in self.content:
                if _item:
                    _items.append(_item.to_dict())
            _dict['content'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RunStepDetailsToolCallsFileSearchResultObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "file_id": obj.get("file_id"),
            "file_name": obj.get("file_name"),
            "score": obj.get("score"),
            "content": [RunStepDetailsToolCallsFileSearchResultObjectContentInner.from_dict(_item) for _item in obj.get("content")] if obj.get("content") is not None else None
        })
        return _obj


