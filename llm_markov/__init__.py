from llm import Model, Prompt, hookimpl
import llm
from collections import defaultdict
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

    class Response(llm.Response):
        def iter_prompt(self, prompt):
            self._prompt_json = {"input": prompt.prompt}

            length = prompt.options.length or DEFAULT_LENGTH
            delay = DEFAULT_DELAY
            if prompt.options.delay is not None:
                delay = prompt.options.delay

            if not self.stream:
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
            self._response_json = {
                "generated": " ".join(result),
                "transitions": dict(transitions),
            }

    def execute(self, prompt: Prompt, stream: bool = True) -> Response:
        return self.Response(prompt, self, stream)

    def __str__(self):
        return "Markov: {}".format(self.model_id)
