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




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_server.models.assistantt.assistant_object_tool_resources import AssistantObjectToolResources
from openapi_server.models.assistantt.assistant_object_tools_inner import AssistantObjectToolsInner
from openapi_server.models.assistants.assistants_api_response_format_option import AssistantsApiResponseFormatOption
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AssistantObject(BaseModel):
    """
    Represents an `assistant` that can call the model and use tools.
    """ # noqa: E501
    id: StrictStr = Field(description="The identifier, which can be referenced in API endpoints.")
    object: StrictStr = Field(description="The object type, which is always `assistant`.")
    created_at: StrictInt = Field(description="The Unix timestamp (in seconds) for when the assistant was created.")
    name: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(description="The name of the assistant. The maximum length is 256 characters. ")
    description: Optional[Annotated[str, Field(strict=True, max_length=512)]] = Field(description="The description of the assistant. The maximum length is 512 characters. ")
    model: StrictStr = Field(description="ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them. ")
    instructions: Optional[Annotated[str, Field(strict=True, max_length=256000)]] = Field(description="The system instructions that the assistant uses. The maximum length is 256,000 characters. ")
    tools: Annotated[List[AssistantObjectToolsInner], Field(max_length=128)] = Field(description="A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`. ")
    tool_resources: Optional[AssistantObjectToolResources] = None
    metadata: Optional[Dict[str, Any]] = Field(description="Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. ")
    temperature: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = Field(default=1, description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. ")
    top_p: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=1, description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both. ")
    response_format: Optional[AssistantsApiResponseFormatOption] = None
    __properties: ClassVar[List[str]] = ["id", "object", "created_at", "name", "description", "model", "instructions", "tools", "tool_resources", "metadata", "temperature", "top_p", "response_format"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('assistant',):
            raise ValueError("must be one of enum values ('assistant')")
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
        """Create an instance of AssistantObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of tool_resources
        if self.tool_resources:
            _dict['tool_resources'] = self.tool_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of response_format
        if self.response_format:
            _dict['response_format'] = self.response_format.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if instructions (nullable) is None
        # and model_fields_set contains the field
        if self.instructions is None and "instructions" in self.model_fields_set:
            _dict['instructions'] = None

        # set to None if tool_resources (nullable) is None
        # and model_fields_set contains the field
        if self.tool_resources is None and "tool_resources" in self.model_fields_set:
            _dict['tool_resources'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if temperature (nullable) is None
        # and model_fields_set contains the field
        if self.temperature is None and "temperature" in self.model_fields_set:
            _dict['temperature'] = None

        # set to None if top_p (nullable) is None
        # and model_fields_set contains the field
        if self.top_p is None and "top_p" in self.model_fields_set:
            _dict['top_p'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AssistantObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "model": obj.get("model"),
            "instructions": obj.get("instructions"),
            "tools": [AssistantObjectToolsInner.from_dict(_item) for _item in obj.get("tools")] if obj.get("tools") is not None else None,
            "tool_resources": AssistantObjectToolResources.from_dict(obj.get("tool_resources")) if obj.get("tool_resources") is not None else None,
            "metadata": obj.get("metadata"),
            "temperature": obj.get("temperature") if obj.get("temperature") is not None else 1,
            "top_p": obj.get("top_p") if obj.get("top_p") is not None else 1,
            "response_format": AssistantsApiResponseFormatOption.from_dict(obj.get("response_format")) if obj.get("response_format") is not None else None
        })
        return _obj


