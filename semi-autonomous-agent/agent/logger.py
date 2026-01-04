def log(step, observation, decision, insight=None):
    print(f"\n[STEP {step}]")
    print(f"URL: {observation['url']}")
    print(f"Decision: {decision}")
    if insight:
        print(f"Insight: {insight}")
    print("-" * 50)
