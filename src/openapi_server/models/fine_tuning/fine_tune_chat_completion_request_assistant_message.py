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
from openapi_server.models.chat_completion.chat_completion_message_tool_call import ChatCompletionMessageToolCall
from openapi_server.models.chat_completion.chat_completion_request_assistant_message_audio import ChatCompletionRequestAssistantMessageAudio
from openapi_server.models.chat_completion.chat_completion_request_assistant_message_content import ChatCompletionRequestAssistantMessageContent
from openapi_server.models.chat_completion.chat_completion_request_assistant_message_function_call import ChatCompletionRequestAssistantMessageFunctionCall
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FineTuneChatCompletionRequestAssistantMessage(BaseModel):
    """
    FineTuneChatCompletionRequestAssistantMessage
    """ # noqa: E501
    content: Optional[ChatCompletionRequestAssistantMessageContent] = None
    refusal: Optional[StrictStr] = Field(default=None, description="The refusal message by the assistant.")
    role: StrictStr = Field(description="The role of the messages author, in this case `assistant`.")
    name: Optional[StrictStr] = Field(default=None, description="An optional name for the participant. Provides the model information to differentiate between participants of the same role.")
    audio: Optional[ChatCompletionRequestAssistantMessageAudio] = None
    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = Field(default=None, description="The tool calls generated by the model, such as function calls.")
    function_call: Optional[ChatCompletionRequestAssistantMessageFunctionCall] = None
    weight: Optional[StrictInt] = Field(default=None, description="Controls whether the assistant message is trained against (0 or 1)")
    __properties: ClassVar[List[str]] = ["content", "refusal", "role", "name", "audio", "tool_calls", "function_call", "weight"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('assistant',):
            raise ValueError("must be one of enum values ('assistant')")
        return value

    @field_validator('weight')
    def weight_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1,):
            raise ValueError("must be one of enum values (0, 1)")
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
        """Create an instance of FineTuneChatCompletionRequestAssistantMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of audio
        if self.audio:
            _dict['audio'] = self.audio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tool_calls (list)
        _items = []
        if self.tool_calls:
            for _item in self.tool_calls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tool_calls'] = _items
        # override the default output from pydantic by calling `to_dict()` of function_call
        if self.function_call:
            _dict['function_call'] = self.function_call.to_dict()
        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        # set to None if refusal (nullable) is None
        # and model_fields_set contains the field
        if self.refusal is None and "refusal" in self.model_fields_set:
            _dict['refusal'] = None

        # set to None if audio (nullable) is None
        # and model_fields_set contains the field
        if self.audio is None and "audio" in self.model_fields_set:
            _dict['audio'] = None

        # set to None if function_call (nullable) is None
        # and model_fields_set contains the field
        if self.function_call is None and "function_call" in self.model_fields_set:
            _dict['function_call'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FineTuneChatCompletionRequestAssistantMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content": ChatCompletionRequestAssistantMessageContent.from_dict(obj.get("content")) if obj.get("content") is not None else None,
            "refusal": obj.get("refusal"),
            "role": obj.get("role"),
            "name": obj.get("name"),
            "audio": ChatCompletionRequestAssistantMessageAudio.from_dict(obj.get("audio")) if obj.get("audio") is not None else None,
            "tool_calls": [ChatCompletionMessageToolCall.from_dict(_item) for _item in obj.get("tool_calls")] if obj.get("tool_calls") is not None else None,
            "function_call": ChatCompletionRequestAssistantMessageFunctionCall.from_dict(obj.get("function_call")) if obj.get("function_call") is not None else None,
            "weight": obj.get("weight")
        })
        return _obj


