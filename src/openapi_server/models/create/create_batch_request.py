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




from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateBatchRequest(BaseModel):
    """
    CreateBatchRequest
    """ # noqa: E501
    input_file_id: StrictStr = Field(description="The ID of an uploaded file that contains requests for the new batch.  See [upload file](/docs/api-reference/files/create) for how to upload a file.  Your input file must be formatted as a [JSONL file](/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 100 MB in size. ")
    endpoint: StrictStr = Field(description="The endpoint to be used for all requests in the batch. Currently `/v1/chat/completions`, `/v1/embeddings`, and `/v1/completions` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.")
    completion_window: StrictStr = Field(description="The time frame within which the batch should be processed. Currently only `24h` is supported.")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Optional custom metadata for the batch.")
    __properties: ClassVar[List[str]] = ["input_file_id", "endpoint", "completion_window", "metadata"]

    @field_validator('endpoint')
    def endpoint_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('/v1/chat/completions', '/v1/embeddings', '/v1/completions',):
            raise ValueError("must be one of enum values ('/v1/chat/completions', '/v1/embeddings', '/v1/completions')")
        return value

    @field_validator('completion_window')
    def completion_window_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('24h',):
            raise ValueError("must be one of enum values ('24h')")
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
        """Create an instance of CreateBatchRequest from a JSON string"""
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
        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateBatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input_file_id": obj.get("input_file_id"),
            "endpoint": obj.get("endpoint"),
            "completion_window": obj.get("completion_window"),
            "metadata": obj.get("metadata")
        })
        return _obj


