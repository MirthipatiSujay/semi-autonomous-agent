def observe_page(driver):
    return {
        "title": driver.title,
        "url": driver.current_url,
        "content": driver.page_source.lower()
    }
