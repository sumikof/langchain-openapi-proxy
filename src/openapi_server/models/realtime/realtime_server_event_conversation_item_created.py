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
from typing import Any, ClassVar, Dict, List
from openapi_server.models.realtime.realtime_conversation_item import RealtimeConversationItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RealtimeServerEventConversationItemCreated(BaseModel):
    """
    Returned when a conversation item is created. There are several scenarios that produce this event:   - The server is generating a Response, which if successful will produce either one or two Items, which will be of type `message` (role `assistant`) or type `function_call`.   - The input audio buffer has been committed, either by the client or the server (in `server_vad` mode). The server will take the content of the input audio buffer and add it to a new user message Item.   - The client has sent a `conversation.item.create` event to add a new Item to the Conversation.
    """ # noqa: E501
    event_id: StrictStr = Field(description="The unique ID of the server event.")
    type: StrictStr = Field(description="The event type, must be `conversation.item.created`.")
    previous_item_id: StrictStr = Field(description="The ID of the preceding item in the Conversation context, allows the client to understand the order of the conversation.")
    item: RealtimeConversationItem
    __properties: ClassVar[List[str]] = ["event_id", "type", "previous_item_id", "item"]

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
        """Create an instance of RealtimeServerEventConversationItemCreated from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RealtimeServerEventConversationItemCreated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_id": obj.get("event_id"),
            "type": obj.get("type"),
            "previous_item_id": obj.get("previous_item_id"),
            "item": RealtimeConversationItem.from_dict(obj.get("item")) if obj.get("item") is not None else None
        })
        return _obj


