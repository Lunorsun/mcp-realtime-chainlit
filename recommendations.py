"""감정별 맞춤 권장사항 및 자기돌봄 가이드."""

EMOTION_RECOMMENDATIONS = {
    "성취": {
        "emoji": "◆",
        "color": "#FFD700",
        "message": "오늘의 성공을 축하해",
        "advice": [
            "이 성취감을 마음속에 담아두고 어려울 때 기억해보세요.",
            "하던 일을 계속하면서도 작은 쉼표를 가져가세요.",
            "오늘의 경험을 누군가와 나눠보는 것도 좋아요.",
        ],
    },
    "기대": {
        "emoji": "▲",
        "color": "#FFB6C1",
        "message": "설레는 마음 그대로 이어가",
        "advice": [
            "이 기대감을 지키면서 현재 순간도 느껴보세요.",
            "작은 준비 하나씩 해나가는 것도 즐거움이에요.",
            "기대가 현실이 되면 더 소중할 거예요.",
        ],
    },
    "불안": {
        "emoji": "▼",
        "color": "#87CEEB",
        "message": "불안함도 감정의 일부일 뿐",
        "advice": [
            "불안감을 인정하고, 깊게 숨을 쉬어보세요.",
            "할 수 있는 작은 것부터 시작해보세요.",
            "혼자가 아니라는 것을 기억하세요.",
        ],
    },
    "고요": {
        "emoji": "★",
        "color": "#DDA0DD",
        "message": "이 평온함을 지켜주세요",
        "advice": [
            "지금의 고요함 속에서 충전해보세요.",
            "자신의 리듬대로 흘러가게 내려놓아보세요.",
            "이 순간을 감사하는 마음으로 느껴보세요.",
        ],
    },
    "회피": {
        "emoji": "●",
        "color": "#A9A9A9",
        "message": "피하고 싶은 마음도 이해해",
        "advice": [
            "무엇을 피하고 싶은지 차분히 들여다봐보세요.",
            "작은 한 걸음이라도 방향을 바꿔보세요.",
            "도움을 청하는 것도 용감한 선택이에요.",
        ],
    },
    "지침": {
        "emoji": "○",
        "color": "#F5F5DC",
        "message": "길을 찾아가는 과정도 아름다워",
        "advice": [
            "지금은 모르는 게 당연해요.",
            "하나씩 작게 시도해보세요.",
            "그 과정 자체가 너를 성장시켜요.",
        ],
    },
}


def get_recommendation(emotion: str) -> dict:
    """감정에 따른 맞춤 권장사항 반환."""
    return EMOTION_RECOMMENDATIONS.get(emotion, EMOTION_RECOMMENDATIONS["지침"])


def get_selfcare_tip(emotion: str) -> str:
    """감정별 자기돌봄 팁 반환."""
    rec = get_recommendation(emotion)
    advices = rec.get("advice", [])
    import random

    return random.choice(advices) if advices else "자신을 소중히 여겨주세요."
