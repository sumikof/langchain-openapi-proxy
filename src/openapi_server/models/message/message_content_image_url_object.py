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




from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from openapi_server.models.message.message_content_image_url_object_image_url import MessageContentImageUrlObjectImageUrl
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MessageContentImageUrlObject(BaseModel):
    """
    References an image URL in the content of a message.
    """ # noqa: E501
    type: StrictStr = Field(description="The type of the content part.")
    image_url: MessageContentImageUrlObjectImageUrl
    __properties: ClassVar[List[str]] = ["type", "image_url"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('image_url',):
            raise ValueError("must be one of enum values ('image_url')")
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
        """Create an instance of MessageContentImageUrlObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of image_url
        if self.image_url:
            _dict['image_url'] = self.image_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MessageContentImageUrlObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "image_url": MessageContentImageUrlObjectImageUrl.from_dict(obj.get("image_url")) if obj.get("image_url") is not None else None
        })
        return _obj


