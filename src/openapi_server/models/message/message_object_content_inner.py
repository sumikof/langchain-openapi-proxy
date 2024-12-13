# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401



from pydantic import BaseModel, ValidationError, field_validator
from openapi_server.models.message.message_content_image_file_object import MessageContentImageFileObject
from openapi_server.models.message.message_content_image_url_object import MessageContentImageUrlObject
from openapi_server.models.message.message_content_refusal_object import MessageContentRefusalObject
from openapi_server.models.message.message_content_text_object import MessageContentTextObject
from typing import Union, List, Optional, Dict
from typing_extensions import Literal

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

MESSAGEOBJECTCONTENTINNER_ONE_OF_SCHEMAS = ["MessageContentImageFileObject", "MessageContentImageUrlObject", "MessageContentRefusalObject", "MessageContentTextObject"]

class MessageObjectContentInner(BaseModel):
    """
    MessageObjectContentInner
    """
    # data type: MessageContentImageFileObject
    oneof_schema_1_validator: Optional[MessageContentImageFileObject] = None
    # data type: MessageContentImageUrlObject
    oneof_schema_2_validator: Optional[MessageContentImageUrlObject] = None
    # data type: MessageContentTextObject
    oneof_schema_3_validator: Optional[MessageContentTextObject] = None
    # data type: MessageContentRefusalObject
    oneof_schema_4_validator: Optional[MessageContentRefusalObject] = None
    actual_instance: Optional[Union[MessageContentImageFileObject, MessageContentImageUrlObject, MessageContentRefusalObject, MessageContentTextObject]] = None
    one_of_schemas: List[str] = Literal["MessageContentImageFileObject", "MessageContentImageUrlObject", "MessageContentRefusalObject", "MessageContentTextObject"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = MessageObjectContentInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: MessageContentImageFileObject
        if not isinstance(v, MessageContentImageFileObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageContentImageFileObject`")
        else:
            match += 1
        # validate data type: MessageContentImageUrlObject
        if not isinstance(v, MessageContentImageUrlObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageContentImageUrlObject`")
        else:
            match += 1
        # validate data type: MessageContentTextObject
        if not isinstance(v, MessageContentTextObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageContentTextObject`")
        else:
            match += 1
        # validate data type: MessageContentRefusalObject
        if not isinstance(v, MessageContentRefusalObject):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MessageContentRefusalObject`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in MessageObjectContentInner with oneOf schemas: MessageContentImageFileObject, MessageContentImageUrlObject, MessageContentRefusalObject, MessageContentTextObject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in MessageObjectContentInner with oneOf schemas: MessageContentImageFileObject, MessageContentImageUrlObject, MessageContentRefusalObject, MessageContentTextObject. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into MessageContentImageFileObject
        try:
            instance.actual_instance = MessageContentImageFileObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MessageContentImageUrlObject
        try:
            instance.actual_instance = MessageContentImageUrlObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MessageContentTextObject
        try:
            instance.actual_instance = MessageContentTextObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MessageContentRefusalObject
        try:
            instance.actual_instance = MessageContentRefusalObject.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into MessageObjectContentInner with oneOf schemas: MessageContentImageFileObject, MessageContentImageUrlObject, MessageContentRefusalObject, MessageContentTextObject. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into MessageObjectContentInner with oneOf schemas: MessageContentImageFileObject, MessageContentImageUrlObject, MessageContentRefusalObject, MessageContentTextObject. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


