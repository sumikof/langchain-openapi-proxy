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




from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_server.models.chat_completion.chat_completion_functions import ChatCompletionFunctions
from openapi_server.models.chat_completion.chat_completion_request_message import ChatCompletionRequestMessage
from openapi_server.models.chat_completion.chat_completion_stream_options import ChatCompletionStreamOptions
from openapi_server.models.chat_completion.chat_completion_tool import ChatCompletionTool
from openapi_server.models.chat_completion.chat_completion_tool_choice_option import ChatCompletionToolChoiceOption
from openapi_server.models.create_chat_completion.create_chat_completion_request_audio import CreateChatCompletionRequestAudio
from openapi_server.models.create_chat_completion.create_chat_completion_request_function_call import CreateChatCompletionRequestFunctionCall
from openapi_server.models.create_chat_completion.create_chat_completion_request_model import CreateChatCompletionRequestModel
from openapi_server.models.create_chat_completion.create_chat_completion_request_prediction import CreateChatCompletionRequestPrediction
from openapi_server.models.create_chat_completion.create_chat_completion_request_response_format import CreateChatCompletionRequestResponseFormat
from openapi_server.models.create_chat_completion.create_chat_completion_request_stop import CreateChatCompletionRequestStop
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateChatCompletionRequest(BaseModel):
    """
    CreateChatCompletionRequest
    """ # noqa: E501
    messages: Annotated[List[ChatCompletionRequestMessage], Field(min_length=1)] = Field(description="A list of messages comprising the conversation so far. Depending on the [model](/docs/models) you use, different message types (modalities) are supported, like [text](/docs/guides/text-generation), [images](/docs/guides/vision), and [audio](/docs/guides/audio). ")
    # model: CreateChatCompletionRequestModel
    model: StrictStr
    store: Optional[StrictBool] = Field(default=False, description="Whether or not to store the output of this chat completion request for use in our [model distillation](/docs/guides/distillation) or [evals](/docs/guides/evals) products. ")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Developer-defined tags and values used for filtering completions in the [dashboard](https://platform.openai.com/chat-completions). ")
    frequency_penalty: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=-2)], Annotated[int, Field(le=2, strict=True, ge=-2)]]] = Field(default=0, description="Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.  [See more information about frequency and presence penalties.](/docs/guides/text-generation) ")
    logit_bias: Optional[Dict[str, StrictInt]] = Field(default=None, description="Modify the likelihood of specified tokens appearing in the completion.  Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. ")
    logprobs: Optional[StrictBool] = Field(default=False, description="Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.")
    top_logprobs: Optional[Annotated[int, Field(le=20, strict=True, ge=0)]] = Field(default=None, description="An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.")
    max_tokens: Optional[StrictInt] = Field(default=None, description="The maximum number of [tokens](/tokenizer) that can be generated in the chat completion. This value can be used to control [costs](https://openai.com/api/pricing/) for text generated via API.  This value is now deprecated in favor of `max_completion_tokens`, and is not compatible with [o1 series models](/docs/guides/reasoning). ")
    max_completion_tokens: Optional[StrictInt] = Field(default=None, description="An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](/docs/guides/reasoning). ")
    n: Optional[Annotated[int, Field(le=128, strict=True, ge=1)]] = Field(default=1, description="How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.")
    modalities: Optional[List[StrictStr]] = Field(default=None, description="Output types that you would like the model to generate for this request. Most models are capable of generating text, which is the default:  `[\"text\"]`  The `gpt-4o-audio-preview` model can also be used to [generate audio](/docs/guides/audio). To request that this model generate both text and audio responses, you can use:  `[\"text\", \"audio\"]` ")
    prediction: Optional[CreateChatCompletionRequestPrediction] = None
    audio: Optional[CreateChatCompletionRequestAudio] = None
    presence_penalty: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=-2)], Annotated[int, Field(le=2, strict=True, ge=-2)]]] = Field(default=0, description="Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.  [See more information about frequency and presence penalties.](/docs/guides/text-generation) ")
    response_format: Optional[CreateChatCompletionRequestResponseFormat] = None
    seed: Optional[Annotated[int, Field(le=-9223372036854775616, strict=True, ge=9223372036854775616)]] = Field(default=None, description="This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend. ")
    service_tier: Optional[StrictStr] = Field(default='auto', description="Specifies the latency tier to use for processing the request. This parameter is relevant for customers subscribed to the scale tier service:   - If set to 'auto', and the Project is Scale tier enabled, the system will utilize scale tier credits until they are exhausted.   - If set to 'auto', and the Project is not Scale tier enabled, the request will be processed using the default service tier with a lower uptime SLA and no latency guarentee.   - If set to 'default', the request will be processed using the default service tier with a lower uptime SLA and no latency guarentee.   - When not set, the default behavior is 'auto'.    When this parameter is set, the response body will include the `service_tier` utilized. ")
    stop: Optional[CreateChatCompletionRequestStop] = None
    stream: Optional[StrictBool] = Field(default=False, description="If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions). ")
    stream_options: Optional[ChatCompletionStreamOptions] = None
    temperature: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = Field(default=1, description="What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.  We generally recommend altering this or `top_p` but not both. ")
    top_p: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=1, description="An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or `temperature` but not both. ")
    tools: Optional[List[ChatCompletionTool]] = Field(default=None, description="A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported. ")
    tool_choice: Optional[ChatCompletionToolChoiceOption] = None
    parallel_tool_calls: Optional[StrictBool] = Field(default=True, description="Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.")
    user: Optional[StrictStr] = Field(default=None, description="A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](/docs/guides/safety-best-practices#end-user-ids). ")
    function_call: Optional[CreateChatCompletionRequestFunctionCall] = None
    functions: Optional[Annotated[List[ChatCompletionFunctions], Field(min_length=1, max_length=128)]] = Field(default=None, description="Deprecated in favor of `tools`.  A list of functions the model may generate JSON inputs for. ")
    __properties: ClassVar[List[str]] = ["messages", "model", "store", "metadata", "frequency_penalty", "logit_bias", "logprobs", "top_logprobs", "max_tokens", "max_completion_tokens", "n", "modalities", "prediction", "audio", "presence_penalty", "response_format", "seed", "service_tier", "stop", "stream", "stream_options", "temperature", "top_p", "tools", "tool_choice", "parallel_tool_calls", "user", "function_call", "functions"]

    @field_validator('modalities')
    def modalities_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('text', 'audio',):
                raise ValueError("each list item must be one of ('text', 'audio')")
        return value

    @field_validator('service_tier')
    def service_tier_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('auto', 'default',):
            raise ValueError("must be one of enum values ('auto', 'default')")
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
        """Create an instance of CreateChatCompletionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            # _dict['model'] = self.model.to_dict()
            _dict['model'] = self.model
        # override the default output from pydantic by calling `to_dict()` of prediction
        if self.prediction:
            _dict['prediction'] = self.prediction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of audio
        if self.audio:
            _dict['audio'] = self.audio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of response_format
        if self.response_format:
            _dict['response_format'] = self.response_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stop
        if self.stop:
            _dict['stop'] = self.stop.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stream_options
        if self.stream_options:
            _dict['stream_options'] = self.stream_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of tool_choice
        if self.tool_choice:
            _dict['tool_choice'] = self.tool_choice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of function_call
        if self.function_call:
            _dict['function_call'] = self.function_call.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in functions (list)
        _items = []
        if self.functions:
            for _item in self.functions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['functions'] = _items
        # set to None if store (nullable) is None
        # and model_fields_set contains the field
        if self.store is None and "store" in self.model_fields_set:
            _dict['store'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if frequency_penalty (nullable) is None
        # and model_fields_set contains the field
        if self.frequency_penalty is None and "frequency_penalty" in self.model_fields_set:
            _dict['frequency_penalty'] = None

        # set to None if logit_bias (nullable) is None
        # and model_fields_set contains the field
        if self.logit_bias is None and "logit_bias" in self.model_fields_set:
            _dict['logit_bias'] = None

        # set to None if logprobs (nullable) is None
        # and model_fields_set contains the field
        if self.logprobs is None and "logprobs" in self.model_fields_set:
            _dict['logprobs'] = None

        # set to None if top_logprobs (nullable) is None
        # and model_fields_set contains the field
        if self.top_logprobs is None and "top_logprobs" in self.model_fields_set:
            _dict['top_logprobs'] = None

        # set to None if max_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.max_tokens is None and "max_tokens" in self.model_fields_set:
            _dict['max_tokens'] = None

        # set to None if max_completion_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.max_completion_tokens is None and "max_completion_tokens" in self.model_fields_set:
            _dict['max_completion_tokens'] = None

        # set to None if n (nullable) is None
        # and model_fields_set contains the field
        if self.n is None and "n" in self.model_fields_set:
            _dict['n'] = None

        # set to None if modalities (nullable) is None
        # and model_fields_set contains the field
        if self.modalities is None and "modalities" in self.model_fields_set:
            _dict['modalities'] = None

        # set to None if prediction (nullable) is None
        # and model_fields_set contains the field
        if self.prediction is None and "prediction" in self.model_fields_set:
            _dict['prediction'] = None

        # set to None if audio (nullable) is None
        # and model_fields_set contains the field
        if self.audio is None and "audio" in self.model_fields_set:
            _dict['audio'] = None

        # set to None if presence_penalty (nullable) is None
        # and model_fields_set contains the field
        if self.presence_penalty is None and "presence_penalty" in self.model_fields_set:
            _dict['presence_penalty'] = None

        # set to None if seed (nullable) is None
        # and model_fields_set contains the field
        if self.seed is None and "seed" in self.model_fields_set:
            _dict['seed'] = None

        # set to None if service_tier (nullable) is None
        # and model_fields_set contains the field
        if self.service_tier is None and "service_tier" in self.model_fields_set:
            _dict['service_tier'] = None

        # set to None if stream (nullable) is None
        # and model_fields_set contains the field
        if self.stream is None and "stream" in self.model_fields_set:
            _dict['stream'] = None

        # set to None if stream_options (nullable) is None
        # and model_fields_set contains the field
        if self.stream_options is None and "stream_options" in self.model_fields_set:
            _dict['stream_options'] = None

        # set to None if temperature (nullable) is None
        # and model_fields_set contains the field
        if self.temperature is None and "temperature" in self.model_fields_set:
            _dict['temperature'] = None

        # set to None if top_p (nullable) is None
        # and model_fields_set contains the field
        if self.top_p is None and "top_p" in self.model_fields_set:
            _dict['top_p'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateChatCompletionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "messages": [ChatCompletionRequestMessage.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None,
            "model": CreateChatCompletionRequestModel.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "store": obj.get("store") if obj.get("store") is not None else False,
            "metadata": obj.get("metadata"),
            "frequency_penalty": obj.get("frequency_penalty") if obj.get("frequency_penalty") is not None else 0,
            "logit_bias": obj.get("logit_bias"),
            "logprobs": obj.get("logprobs") if obj.get("logprobs") is not None else False,
            "top_logprobs": obj.get("top_logprobs"),
            "max_tokens": obj.get("max_tokens"),
            "max_completion_tokens": obj.get("max_completion_tokens"),
            "n": obj.get("n") if obj.get("n") is not None else 1,
            "modalities": obj.get("modalities"),
            "prediction": CreateChatCompletionRequestPrediction.from_dict(obj.get("prediction")) if obj.get("prediction") is not None else None,
            "audio": CreateChatCompletionRequestAudio.from_dict(obj.get("audio")) if obj.get("audio") is not None else None,
            "presence_penalty": obj.get("presence_penalty") if obj.get("presence_penalty") is not None else 0,
            "response_format": CreateChatCompletionRequestResponseFormat.from_dict(obj.get("response_format")) if obj.get("response_format") is not None else None,
            "seed": obj.get("seed"),
            "service_tier": obj.get("service_tier") if obj.get("service_tier") is not None else 'auto',
            "stop": CreateChatCompletionRequestStop.from_dict(obj.get("stop")) if obj.get("stop") is not None else None,
            "stream": obj.get("stream") if obj.get("stream") is not None else False,
            "stream_options": ChatCompletionStreamOptions.from_dict(obj.get("stream_options")) if obj.get("stream_options") is not None else None,
            "temperature": obj.get("temperature") if obj.get("temperature") is not None else 1,
            "top_p": obj.get("top_p") if obj.get("top_p") is not None else 1,
            "tools": [ChatCompletionTool.from_dict(_item) for _item in obj.get("tools")] if obj.get("tools") is not None else None,
            "tool_choice": ChatCompletionToolChoiceOption.from_dict(obj.get("tool_choice")) if obj.get("tool_choice") is not None else None,
            "parallel_tool_calls": obj.get("parallel_tool_calls") if obj.get("parallel_tool_calls") is not None else True,
            "user": obj.get("user"),
            "function_call": CreateChatCompletionRequestFunctionCall.from_dict(obj.get("function_call")) if obj.get("function_call") is not None else None,
            "functions": [ChatCompletionFunctions.from_dict(_item) for _item in obj.get("functions")] if obj.get("functions") is not None else None
        })
        return _obj

