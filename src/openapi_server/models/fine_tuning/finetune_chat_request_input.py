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




from pydantic import BaseModel, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.chat_completion.chat_completion_functions import ChatCompletionFunctions
from openapi_server.models.chat_completion.chat_completion_tool import ChatCompletionTool
from openapi_server.models.fine_tuning.finetune_chat_request_input_messages_inner import FinetuneChatRequestInputMessagesInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FinetuneChatRequestInput(BaseModel):
    """
    The per-line training example of a fine-tuning input file for chat models
    """ # noqa: E501
    messages: Optional[Annotated[List[FinetuneChatRequestInputMessagesInner], Field(min_length=1)]] = None
    tools: Optional[List[ChatCompletionTool]] = Field(default=None, description="A list of tools the model may generate JSON inputs for.")
    parallel_tool_calls: Optional[StrictBool] = Field(default=True, description="Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.")
    functions: Optional[Annotated[List[ChatCompletionFunctions], Field(min_length=1, max_length=128)]] = Field(default=None, description="A list of functions the model may generate JSON inputs for.")
    __properties: ClassVar[List[str]] = ["messages", "tools", "parallel_tool_calls", "functions"]

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
        """Create an instance of FinetuneChatRequestInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in functions (list)
        _items = []
        if self.functions:
            for _item in self.functions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['functions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FinetuneChatRequestInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "messages": [FinetuneChatRequestInputMessagesInner.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None,
            "tools": [ChatCompletionTool.from_dict(_item) for _item in obj.get("tools")] if obj.get("tools") is not None else None,
            "parallel_tool_calls": obj.get("parallel_tool_calls") if obj.get("parallel_tool_calls") is not None else True,
            "functions": [ChatCompletionFunctions.from_dict(_item) for _item in obj.get("functions")] if obj.get("functions") is not None else None
        })
        return _obj


