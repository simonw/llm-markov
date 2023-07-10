from llm import Model, Prompt, hookimpl
import llm
from collections import defaultdict
from pydantic import field_validator
import random
import time
from typing import Optional


DEFAULT_LENGTH = 100
DEFAULT_DELAY = 0.02


@hookimpl
def register_models(register):
    register(Markov())


class Markov(Model):
    can_stream = True
    model_id = "markov"

    class Options(llm.Options):
        length: Optional[int] = None
        delay: Optional[float] = None

        @field_validator("length")
        def validate_length(cls, length):
            if length is None:
                return None
            if length < 2:
                raise ValueError("length must be >= 2")
            return length

        @field_validator("delay")
        def validate_delay(cls, delay):
            if delay is None:
                return None
            if not 0 <= delay <= 10:
                raise ValueError("delay must be between 0 and 10")
            return delay

    def execute(self, prompt, stream, response):
        length = prompt.options.length or DEFAULT_LENGTH
        delay = DEFAULT_DELAY
        if prompt.options.delay is not None:
            delay = prompt.options.delay

        if not stream:
            delay = 0

        transitions = defaultdict(list)
        all_words = prompt.prompt.split()
        for i in range(len(all_words) - 1):
            transitions[all_words[i]].append(all_words[i + 1])

        result = [all_words[0]]
        for _ in range(length):
            if transitions[result[-1]]:
                token = random.choice(transitions[result[-1]])
            else:
                token = random.choice(all_words)
            yield token + " "
            time.sleep(delay)
            result.append(token)

    def __str__(self):
        return "Markov: {}".format(self.model_id)
