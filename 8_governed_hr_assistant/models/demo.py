"""Local demonstration only; no LLM or employee system is called."""


def respond(question, calls):
    calls.append(question)
    return "Local demo: annual leave is 20 days under the fictional policy."
