"""A local responder with an observable invocation log; no model service."""


def respond(question, calls):
    calls.append(question)
    return "Local demo: the published policy says annual leave is 20 days."
