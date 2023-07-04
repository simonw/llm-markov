from click.testing import CliRunner
from llm.cli import cli
import pytest
import time


@pytest.mark.parametrize(
    "no_stream,delay",
    (
        (True, None),
        (False, 0),
        (False, 0.01),
        (False, 0.03),
    ),
)
@pytest.mark.parametrize("length", [10, 20])
def test_markov_prompt(length, no_stream, delay):
    runner = CliRunner()
    prompt = "the quick brown fox jumped over the lazy dog"
    args = [
        prompt,
        "-m",
        "markov",
        "-o",
        "length",
        str(length),
    ]
    if no_stream:
        args.append("--no-stream")
    if delay is not None:
        args.extend(
            [
                "-o",
                "delay",
                str(delay),
            ]
        )
    start = time.monotonic()
    result = runner.invoke(cli, args)
    end = time.monotonic()
    if no_stream:
        assert end - start < 0.1
    assert result.exit_code == 0, result.output
    words = result.output.strip().split()
    # ['lazy', 'dog', 'brown', 'fox', 'jumped', 'over', 'the', 'quick', 'brown']
    # Every word should be one of the original prompt
    prompt_words = prompt.split()
    for word in words:
        assert word in prompt_words
    assert len(words) == length
