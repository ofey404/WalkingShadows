import argparse
from pathlib import Path

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


def load_input(data_path: Path) -> str:
    with open(data_path / "input.txt") as f:
        return "\n".join(f.readlines())


def write_output(text: str, data_path: Path):
    with open(data_path / "output.txt", "wt") as f:
        f.write(text)


def main(data_path: Path, verbose: bool):
    print(f"## data path: {data_path}")
    llm = ChatOpenAI(
        temperature=0.9,
        model_name="gpt-4",
        verbose=True,
    )
    i = load_input(data_path)
    o = llm([HumanMessage(content=i)])
    write_output(o.content, data_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)  # positional argument
    parser.add_argument("-v", "--verbose", action="store_true")  # on/off flag
    args = parser.parse_args()
    main(Path(args.data), args.verbose)
