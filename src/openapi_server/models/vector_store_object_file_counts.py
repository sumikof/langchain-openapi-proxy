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




from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VectorStoreObjectFileCounts(BaseModel):
    """
    VectorStoreObjectFileCounts
    """ # noqa: E501
    in_progress: StrictInt = Field(description="The number of files that are currently being processed.")
    completed: StrictInt = Field(description="The number of files that have been successfully processed.")
    failed: StrictInt = Field(description="The number of files that have failed to process.")
    cancelled: StrictInt = Field(description="The number of files that were cancelled.")
    total: StrictInt = Field(description="The total number of files.")
    __properties: ClassVar[List[str]] = ["in_progress", "completed", "failed", "cancelled", "total"]

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
        """Create an instance of VectorStoreObjectFileCounts from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of VectorStoreObjectFileCounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "in_progress": obj.get("in_progress"),
            "completed": obj.get("completed"),
            "failed": obj.get("failed"),
            "cancelled": obj.get("cancelled"),
            "total": obj.get("total")
        })
        return _obj


