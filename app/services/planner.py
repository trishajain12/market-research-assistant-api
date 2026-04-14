def generate_research_plan(topic: str):
    cleaned_topic = topic.strip()
    research_type = classify_topic(cleaned_topic)
    keywords = build_keywords(cleaned_topic, research_type)

    if research_type == "comparison":
        subquestions = [
            f"What are the core offerings of each side in {cleaned_topic}?",
            f"What are the main differences in pricing, features, or positioning in {cleaned_topic}?",
            f"What types of customers are best served by each option in {cleaned_topic}?",
            f"What are the strengths and weaknesses of each side in {cleaned_topic}?",
            f"What trends or market forces affect the comparison in {cleaned_topic}?"
        ]
        report_outline = [
            "Comparison Overview",
            "Core Offerings",
            "Target Customers",
            "Strengths and Weaknesses",
            "Market Implications"
        ]
        next_step = "Next, retrieve sources for both sides of the comparison."

    elif research_type == "market":
        subquestions = [
            f"What are the major trends shaping the {cleaned_topic}?",
            f"Who are the leading players in the {cleaned_topic}?",
            f"What customer needs are driving growth in the {cleaned_topic}?",
            f"What risks or barriers exist in the {cleaned_topic}?",
            f"What opportunities are emerging in the {cleaned_topic}?"
        ]
        report_outline = [
            "Market Overview",
            "Key Trends",
            "Leading Players",
            "Customer Demand",
            "Risks and Opportunities"
        ]
        next_step = "Next, retrieve market trend and competitor sources."

    elif research_type == "company":
        subquestions = [
            f"What are the main products and services related to {cleaned_topic}?",
            f"Who are the key competitors related to {cleaned_topic}?",
            f"What industries or customer groups are targeted by {cleaned_topic}?",
            f"What differentiates {cleaned_topic} from competitors?",
            f"What risks and growth opportunities affect {cleaned_topic}?"
        ]
        report_outline = [
            "Company Overview",
            "Products and Services",
            "Competitive Landscape",
            "Target Customers",
            "Risks and Opportunities"
        ]
        next_step = "Next, retrieve company, competitor, and industry sources."

    else:
        subquestions = [
            f"What are the most important concepts related to {cleaned_topic}?",
            f"What problems or needs are connected to {cleaned_topic}?",
            f"Who are the major players related to {cleaned_topic}?",
            f"What trends are influencing {cleaned_topic}?",
            f"What should be researched further about {cleaned_topic}?"
        ]
        report_outline = [
            "Overview",
            "Key Concepts",
            "Major Players",
            "Important Trends",
            "Further Questions"
        ]
        next_step = "Next, retrieve general background and trend sources."

    return {
        "topic": cleaned_topic,
        "research_type": research_type,
        "subquestions": subquestions,
        "report_outline": report_outline,
        "keywords": keywords,
        "next_step": next_step
    }


def classify_topic(topic: str):
    lowered = topic.lower()

    comparison_signals = [" vs ", "versus", "compare", "comparison"]
    market_signals = ["market", "industry", "sector", "trends", "forecast"]
    company_signals = [
        "ibm", "microsoft", "google", "amazon", "meta", "openai",
        "anthropic", "nvidia", "salesforce", "oracle", "intel"
    ]

    if any(signal in lowered for signal in comparison_signals):
        return "comparison"
    if any(signal in lowered for signal in market_signals):
        return "market"
    if any(signal in lowered for signal in company_signals):
        return "company"

    return "general"


def build_keywords(topic: str, research_type: str):
    words = topic.replace(",", "").split()
    base_keywords = [word for word in words if len(word) > 2]

    if research_type == "comparison":
        suggested_keywords = [
            topic,
            f"{topic} features",
            f"{topic} pricing",
            f"{topic} differences"
        ]
    elif research_type == "market":
        suggested_keywords = [
            topic,
            f"{topic} trends",
            f"{topic} growth",
            f"{topic} leading companies"
        ]
    elif research_type == "company":
        suggested_keywords = [
            topic,
            f"{topic} products",
            f"{topic} competitors",
            f"{topic} strategy"
        ]
    else:
        suggested_keywords = [
            topic,
            f"{topic} overview",
            f"{topic} trends",
            f"{topic} major players"
        ]

    combined = base_keywords + suggested_keywords

    seen = set()
    unique_keywords = []

    for keyword in combined:
        normalized = keyword.lower()
        if normalized not in seen:
            seen.add(normalized)
            unique_keywords.append(keyword)

    return unique_keywords[:7]