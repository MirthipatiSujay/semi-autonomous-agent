def decide(observation):
    url = observation["url"]

    if "/wiki/" in url and "wikipedia.org" in url:
        return "ANALYZE_ARTICLE"

    if url == "https://www.wikipedia.org/":
        return "SEARCH_TOPIC"

    return "NO_ACTION"
