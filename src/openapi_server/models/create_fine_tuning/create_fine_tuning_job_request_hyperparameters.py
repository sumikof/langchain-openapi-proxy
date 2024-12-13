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




from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.create_fine_tuning.create_fine_tuning_job_request_hyperparameters_batch_size import CreateFineTuningJobRequestHyperparametersBatchSize
from openapi_server.models.create_fine_tuning.create_fine_tuning_job_request_hyperparameters_learning_rate_multiplier import CreateFineTuningJobRequestHyperparametersLearningRateMultiplier
from openapi_server.models.create_fine_tuning.create_fine_tuning_job_request_hyperparameters_n_epochs import CreateFineTuningJobRequestHyperparametersNEpochs
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateFineTuningJobRequestHyperparameters(BaseModel):
    """
    The hyperparameters used for the fine-tuning job.
    """ # noqa: E501
    batch_size: Optional[CreateFineTuningJobRequestHyperparametersBatchSize] = None
    learning_rate_multiplier: Optional[CreateFineTuningJobRequestHyperparametersLearningRateMultiplier] = None
    n_epochs: Optional[CreateFineTuningJobRequestHyperparametersNEpochs] = None
    __properties: ClassVar[List[str]] = ["batch_size", "learning_rate_multiplier", "n_epochs"]

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
        """Create an instance of CreateFineTuningJobRequestHyperparameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of batch_size
        if self.batch_size:
            _dict['batch_size'] = self.batch_size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of learning_rate_multiplier
        if self.learning_rate_multiplier:
            _dict['learning_rate_multiplier'] = self.learning_rate_multiplier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of n_epochs
        if self.n_epochs:
            _dict['n_epochs'] = self.n_epochs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateFineTuningJobRequestHyperparameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "batch_size": CreateFineTuningJobRequestHyperparametersBatchSize.from_dict(obj.get("batch_size")) if obj.get("batch_size") is not None else None,
            "learning_rate_multiplier": CreateFineTuningJobRequestHyperparametersLearningRateMultiplier.from_dict(obj.get("learning_rate_multiplier")) if obj.get("learning_rate_multiplier") is not None else None,
            "n_epochs": CreateFineTuningJobRequestHyperparametersNEpochs.from_dict(obj.get("n_epochs")) if obj.get("n_epochs") is not None else None
        })
        return _obj


