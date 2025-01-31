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




from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.run.run_step_completion_usage import RunStepCompletionUsage
from openapi_server.models.run.run_step_object_last_error import RunStepObjectLastError
from openapi_server.models.run.run_step_object_step_details import RunStepObjectStepDetails
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RunStepObject(BaseModel):
    """
    Represents a step in execution of a run. 
    """ # noqa: E501
    id: StrictStr = Field(description="The identifier of the run step, which can be referenced in API endpoints.")
    object: StrictStr = Field(description="The object type, which is always `thread.run.step`.")
    created_at: StrictInt = Field(description="The Unix timestamp (in seconds) for when the run step was created.")
    assistant_id: StrictStr = Field(description="The ID of the [assistant](/docs/api-reference/assistants) associated with the run step.")
    thread_id: StrictStr = Field(description="The ID of the [thread](/docs/api-reference/threads) that was run.")
    run_id: StrictStr = Field(description="The ID of the [run](/docs/api-reference/runs) that this run step is a part of.")
    type: StrictStr = Field(description="The type of run step, which can be either `message_creation` or `tool_calls`.")
    status: StrictStr = Field(description="The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.")
    step_details: RunStepObjectStepDetails
    last_error: Optional[RunStepObjectLastError]
    expired_at: Optional[StrictInt] = Field(description="The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.")
    cancelled_at: Optional[StrictInt] = Field(description="The Unix timestamp (in seconds) for when the run step was cancelled.")
    failed_at: Optional[StrictInt] = Field(description="The Unix timestamp (in seconds) for when the run step failed.")
    completed_at: Optional[StrictInt] = Field(description="The Unix timestamp (in seconds) for when the run step completed.")
    metadata: Optional[Dict[str, Any]] = Field(description="Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long. ")
    usage: Optional[RunStepCompletionUsage]
    __properties: ClassVar[List[str]] = ["id", "object", "created_at", "assistant_id", "thread_id", "run_id", "type", "status", "step_details", "last_error", "expired_at", "cancelled_at", "failed_at", "completed_at", "metadata", "usage"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('thread.run.step',):
            raise ValueError("must be one of enum values ('thread.run.step')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('message_creation', 'tool_calls',):
            raise ValueError("must be one of enum values ('message_creation', 'tool_calls')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('in_progress', 'cancelled', 'failed', 'completed', 'expired',):
            raise ValueError("must be one of enum values ('in_progress', 'cancelled', 'failed', 'completed', 'expired')")
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
        """Create an instance of RunStepObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of step_details
        if self.step_details:
            _dict['step_details'] = self.step_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_error
        if self.last_error:
            _dict['last_error'] = self.last_error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage
        if self.usage:
            _dict['usage'] = self.usage.to_dict()
        # set to None if last_error (nullable) is None
        # and model_fields_set contains the field
        if self.last_error is None and "last_error" in self.model_fields_set:
            _dict['last_error'] = None

        # set to None if expired_at (nullable) is None
        # and model_fields_set contains the field
        if self.expired_at is None and "expired_at" in self.model_fields_set:
            _dict['expired_at'] = None

        # set to None if cancelled_at (nullable) is None
        # and model_fields_set contains the field
        if self.cancelled_at is None and "cancelled_at" in self.model_fields_set:
            _dict['cancelled_at'] = None

        # set to None if failed_at (nullable) is None
        # and model_fields_set contains the field
        if self.failed_at is None and "failed_at" in self.model_fields_set:
            _dict['failed_at'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completed_at'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if usage (nullable) is None
        # and model_fields_set contains the field
        if self.usage is None and "usage" in self.model_fields_set:
            _dict['usage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RunStepObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "assistant_id": obj.get("assistant_id"),
            "thread_id": obj.get("thread_id"),
            "run_id": obj.get("run_id"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "step_details": RunStepObjectStepDetails.from_dict(obj.get("step_details")) if obj.get("step_details") is not None else None,
            "last_error": RunStepObjectLastError.from_dict(obj.get("last_error")) if obj.get("last_error") is not None else None,
            "expired_at": obj.get("expired_at"),
            "cancelled_at": obj.get("cancelled_at"),
            "failed_at": obj.get("failed_at"),
            "completed_at": obj.get("completed_at"),
            "metadata": obj.get("metadata"),
            "usage": RunStepCompletionUsage.from_dict(obj.get("usage")) if obj.get("usage") is not None else None
        })
        return _obj


