from agent.browser import start_browser
from agent.observer import observe_page
from agent.decision_engine import decide
from agent.actions import search_topic
from agent.logger import log
import time

driver = start_browser()
driver.get("https://www.wikipedia.org/")

step = 1
max_steps = 5

while step <= max_steps:
    observation = observe_page(driver)
    decision = decide(observation)

    if decision == "SEARCH_TOPIC":
        log(step, observation, decision)
        search_topic(driver)

    elif decision == "ANALYZE_ARTICLE":
        log(
            step,
            observation,
            decision,
            insight=(
                "The article is long with many deep sections. "
                "A collapsible summary or reading-level indicator could improve usability."
            )
        )
        break

    else:
        log(step, observation, decision)
        break

    step += 1
    time.sleep(2)

driver.quit()
