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




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.batch.batch_request_output_error import BatchRequestOutputError
from openapi_server.models.batch.batch_request_output_response import BatchRequestOutputResponse
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BatchRequestOutput(BaseModel):
    """
    The per-line object of the batch output and error files
    """ # noqa: E501
    id: Optional[StrictStr] = None
    custom_id: Optional[StrictStr] = Field(default=None, description="A developer-provided per-request id that will be used to match outputs to inputs.")
    response: Optional[BatchRequestOutputResponse] = None
    error: Optional[BatchRequestOutputError] = None
    __properties: ClassVar[List[str]] = ["id", "custom_id", "response", "error"]

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
        """Create an instance of BatchRequestOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response
        if self.response:
            _dict['response'] = self.response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # set to None if response (nullable) is None
        # and model_fields_set contains the field
        if self.response is None and "response" in self.model_fields_set:
            _dict['response'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BatchRequestOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "custom_id": obj.get("custom_id"),
            "response": BatchRequestOutputResponse.from_dict(obj.get("response")) if obj.get("response") is not None else None,
            "error": BatchRequestOutputError.from_dict(obj.get("error")) if obj.get("error") is not None else None
        })
        return _obj


