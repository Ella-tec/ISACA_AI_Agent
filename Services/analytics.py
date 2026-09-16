from typing import List, Dict

def calculate_accuracy(logs: List[Dict]) -> float:
    """
    Calculates how many answers were high-confidence.
    High confidence = confidence >= 0.7
    """
    if not logs:
        return 0.0

    high_conf = [l for l in logs if l.get("confidence", 0) >= 0.7]
    return len(high_conf) / len(logs)


def count_escalations(logs: List[Dict]) -> int:
    """
    Counts how many interactions required escalation.
    """
    return sum(1 for l in logs if l.get("escalation_required", False))


def average_confidence(logs: List[Dict]) -> float:
    """
    Calculates the average confidence score.
    """
    if not logs:
        return 0.0

    total = sum(l.get("confidence", 0) for l in logs)
    return total / len(logs)


def user_question_count(logs: List[Dict], user_id: str) -> int:
    """
    Counts how many questions a specific user asked.
    """
    return sum(1 for l in logs if l.get("user_id") == user_id)
