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




from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_server.models.realtime.realtime_conversation_item import RealtimeConversationItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RealtimeServerEventResponseOutputItemDone(BaseModel):
    """
    Returned when an Item is done streaming. Also emitted when a Response is interrupted, incomplete, or cancelled.
    """ # noqa: E501
    event_id: StrictStr = Field(description="The unique ID of the server event.")
    type: StrictStr = Field(description="The event type, must be `response.output_item.done`.")
    response_id: StrictStr = Field(description="The ID of the Response to which the item belongs.")
    output_index: StrictInt = Field(description="The index of the output item in the Response.")
    item: RealtimeConversationItem
    __properties: ClassVar[List[str]] = ["event_id", "type", "response_id", "output_index", "item"]

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
        """Create an instance of RealtimeServerEventResponseOutputItemDone from a JSON string"""
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
        """Create an instance of RealtimeServerEventResponseOutputItemDone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_id": obj.get("event_id"),
            "type": obj.get("type"),
            "response_id": obj.get("response_id"),
            "output_index": obj.get("output_index"),
            "item": RealtimeConversationItem.from_dict(obj.get("item")) if obj.get("item") is not None else None
        })
        return _obj

