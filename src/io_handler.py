import json
from pathlib import Path
from typing import Any
from pydantic import ValidationError
from .models import FunctionCall, FunctionDefinition, PromptInput


def load_functions(file: Path) -> list[FunctionDefinition]:
    """Load and validate the function definitions file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data: Any = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Error: file not found: {file}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Error: invalid JSON in {file}: {e}")
    except OSError as e:
        raise SystemExit(f"Error: cannot read {file}: {e}")

    if not isinstance(data, list):
        raise SystemExit(f"Error: {file} must contain a JSON array")

    functions: list[FunctionDefinition] = []
    for d in data:
        try:
            functions.append(FunctionDefinition.model_validate(d))
        except ValidationError as e:
            raise SystemExit(f"Error: invalid function definition: {e}")
    return functions


def load_prompts(file: Path) -> list[PromptInput]:
    """Load and validate the prompts file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data: Any = json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"Error: file not found: {file}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Error: invalid JSON in {file}: {e}")
    except OSError as e:
        raise SystemExit(f"Error: cannot read {file}: {e}")

    if not isinstance(data, list):
        raise SystemExit(f"Error: {file} must contain a JSON array")

    prompts: list[PromptInput] = []
    for d in data:
        try:
            prompts.append(PromptInput.model_validate(d))
        except ValidationError as e:
            raise SystemExit(f"Error: invalid prompt entry: {e}")
    return prompts


def save_results(file_path: Path, function_calls: list[FunctionCall]) -> None:
    """Write the function calls to the output JSON file."""
    results: list[dict[str, Any]] = []
    for call in function_calls:
        results.append(call.model_dump())

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as out_file:
            json.dump(results, out_file, indent=2)
    except OSError as e:
        raise SystemExit(f"Error: cannot write {file_path}: {e}")
