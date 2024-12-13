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




from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.run.run_step_delta_step_details_tool_calls_function_object_function import RunStepDeltaStepDetailsToolCallsFunctionObjectFunction
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RunStepDeltaStepDetailsToolCallsFunctionObject(BaseModel):
    """
    RunStepDeltaStepDetailsToolCallsFunctionObject
    """ # noqa: E501
    index: StrictInt = Field(description="The index of the tool call in the tool calls array.")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the tool call object.")
    type: StrictStr = Field(description="The type of tool call. This is always going to be `function` for this type of tool call.")
    function: Optional[RunStepDeltaStepDetailsToolCallsFunctionObjectFunction] = None
    __properties: ClassVar[List[str]] = ["index", "id", "type", "function"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('function',):
            raise ValueError("must be one of enum values ('function')")
        return value

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
        """Create an instance of RunStepDeltaStepDetailsToolCallsFunctionObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of function
        if self.function:
            _dict['function'] = self.function.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RunStepDeltaStepDetailsToolCallsFunctionObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "id": obj.get("id"),
            "type": obj.get("type"),
            "function": RunStepDeltaStepDetailsToolCallsFunctionObjectFunction.from_dict(obj.get("function")) if obj.get("function") is not None else None
        })
        return _obj


