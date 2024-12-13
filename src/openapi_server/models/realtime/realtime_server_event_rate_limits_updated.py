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
from openapi_server.models.realtime.realtime_server_event_rate_limits_updated_rate_limits_inner import RealtimeServerEventRateLimitsUpdatedRateLimitsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RealtimeServerEventRateLimitsUpdated(BaseModel):
    """
    Emitted at the beginning of a Response to indicate the updated rate limits. When a Response is created some tokens will be \"reserved\" for the output tokens, the rate limits shown here reflect that reservation, which is then adjusted accordingly once the Response is completed.
    """ # noqa: E501
    event_id: StrictStr = Field(description="The unique ID of the server event.")
    type: StrictStr = Field(description="The event type, must be `rate_limits.updated`.")
    rate_limits: List[RealtimeServerEventRateLimitsUpdatedRateLimitsInner] = Field(description="List of rate limit information.")
    __properties: ClassVar[List[str]] = ["event_id", "type", "rate_limits"]

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
        """Create an instance of RealtimeServerEventRateLimitsUpdated from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rate_limits (list)
        _items = []
        if self.rate_limits:
            for _item in self.rate_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rate_limits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RealtimeServerEventRateLimitsUpdated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_id": obj.get("event_id"),
            "type": obj.get("type"),
            "rate_limits": [RealtimeServerEventRateLimitsUpdatedRateLimitsInner.from_dict(_item) for _item in obj.get("rate_limits")] if obj.get("rate_limits") is not None else None
        })
        return _obj


