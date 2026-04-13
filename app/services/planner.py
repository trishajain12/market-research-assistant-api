def generate_research_plan(topic: str):
    cleaned_topic = topic.strip()
    keywords = build_keywords(cleaned_topic)

    return {
        "topic": cleaned_topic,
        "subquestions": [
            f"What are the major products, services, or solutions in {cleaned_topic}?",
            f"Who are the main competitors related to {cleaned_topic}?",
            f"What customer needs or business problems does {cleaned_topic} address?",
            f"What current market trends are shaping {cleaned_topic}?",
            f"What are the biggest opportunities and risks in {cleaned_topic}?"
        ],
        "report_outline": [
            "Overview",
            "Products and Services",
            "Competitive Landscape",
            "Customer Needs",
            "Market Opportunities and Risks"
        ],
        "keywords": keywords
    }


def build_keywords(topic: str):
    words = topic.replace(",", "").split()
    base_keywords = [word for word in words if len(word) > 2]

    suggested_keywords = [
        topic,
        f"{topic} market",
        f"{topic} competitors",
        f"{topic} trends"
    ]

    combined = base_keywords + suggested_keywords

    seen = set()
    unique_keywords = []

    for keyword in combined:
        normalized = keyword.lower()
        if normalized not in seen:
            seen.add(normalized)
            unique_keywords.append(keyword)

    return unique_keywords[:6]