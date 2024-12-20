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
from openapi_server.models.create.create_transcription_response_json import CreateTranscriptionResponseJson
from openapi_server.models.create.create_transcription_response_verbose_json import CreateTranscriptionResponseVerboseJson
from typing import Union, List, Optional, Dict
from typing_extensions import Literal

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

CREATETRANSCRIPTION200RESPONSE_ONE_OF_SCHEMAS = ["CreateTranscriptionResponseJson", "CreateTranscriptionResponseVerboseJson"]

class CreateTranscription200Response(BaseModel):
    """
    CreateTranscription200Response
    """
    # data type: CreateTranscriptionResponseJson
    oneof_schema_1_validator: Optional[CreateTranscriptionResponseJson] = None
    # data type: CreateTranscriptionResponseVerboseJson
    oneof_schema_2_validator: Optional[CreateTranscriptionResponseVerboseJson] = None
    actual_instance: Optional[Union[CreateTranscriptionResponseJson, CreateTranscriptionResponseVerboseJson]] = None
    one_of_schemas: List[str] = Literal["CreateTranscriptionResponseJson", "CreateTranscriptionResponseVerboseJson"]

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
        instance = CreateTranscription200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: CreateTranscriptionResponseJson
        if not isinstance(v, CreateTranscriptionResponseJson):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateTranscriptionResponseJson`")
        else:
            match += 1
        # validate data type: CreateTranscriptionResponseVerboseJson
        if not isinstance(v, CreateTranscriptionResponseVerboseJson):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CreateTranscriptionResponseVerboseJson`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateTranscription200Response with oneOf schemas: CreateTranscriptionResponseJson, CreateTranscriptionResponseVerboseJson. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateTranscription200Response with oneOf schemas: CreateTranscriptionResponseJson, CreateTranscriptionResponseVerboseJson. Details: " + ", ".join(error_messages))
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

        # deserialize data into CreateTranscriptionResponseJson
        try:
            instance.actual_instance = CreateTranscriptionResponseJson.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CreateTranscriptionResponseVerboseJson
        try:
            instance.actual_instance = CreateTranscriptionResponseVerboseJson.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateTranscription200Response with oneOf schemas: CreateTranscriptionResponseJson, CreateTranscriptionResponseVerboseJson. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateTranscription200Response with oneOf schemas: CreateTranscriptionResponseJson, CreateTranscriptionResponseVerboseJson. Details: " + ", ".join(error_messages))
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


