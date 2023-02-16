from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    VERB = 0
    OBJECT = 1
    PREPOSITION = 2


@dataclass(frozen=True)
class Token:
    value: str
    role: Role


@dataclass(frozen=True)
class Pattern:
    tokens: list[Token]

    def match(self, tokens: list[Token]) -> dict[str, str] | None:
        if len(tokens) != len(self.tokens):
            return None

        return None


class Parser:

    def __init__(self) -> None:
        self.determiners = {'a', 'an', 'the'}
        self.prepositions = {'from'}

    def parse(self, string) -> list[Token]:
        sentence = []

        for word in string.split(' '):
            if not sentence:
                sentence.append(Token(word, Role.VERB))

            elif word in self.determiners:
                continue

            elif word in self.prepositions:
                sentence.append(Token(word, Role.PREPOSITION))

            elif sentence[-1].role is Role.OBJECT:
                last_token = sentence.pop()
                sentence.append(
                    Token(f'{last_token.value} {word}', Role.OBJECT))

            else:
                sentence.append(Token(word, Role.OBJECT))

        return sentence

    def parse_pattern(self, pattern: str) -> Pattern:

        sentence = []

        for word in pattern.split(' '):
            if not sentence:
                sentence.append(Token(word, Role.VERB))

            elif word in self.prepositions:
                sentence.append(Token(word, Role.PREPOSITION))

            elif word.isupper():
                sentence.append(Token(word, Role.OBJECT))

        return Pattern(sentence)
