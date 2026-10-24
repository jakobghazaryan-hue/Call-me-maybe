from .cli import parse_args
from .io_handler import load_functions, load_prompts


def main() -> None:
    args = parse_args()
    functions = load_functions(args.functions_definition)
    prompts = load_prompts(args.input)
    print(f"Loaded {len(functions)} functions, {len(prompts)} prompts")

if __name__ == "__main__":
    main()
