"""Pydantic models for function definitions and function calls."""

from typing import Any

from pydantic import BaseModel


class ParameterType(BaseModel):
    """Type description of a parameter or a return value."""

    type: str


class FunctionDefinition(BaseModel):
    """A function that the LLM is allowed to call."""

    name: str
    description: str
    parameters: dict[str, ParameterType]
    returns: ParameterType


class PromptInput(BaseModel):
    """A single natural language prompt from the input file."""

    prompt: str


class FunctionCall(BaseModel):
    """One entry of the output file."""

    prompt: str
    name: str
    parameters: dict[str, Any]
