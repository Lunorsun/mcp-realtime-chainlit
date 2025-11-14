from typing import Dict, List

TEMPLATES = {
    "Pastel": {
        "surface": ["그 순간, 네 마음 속 가장 부드러웠던 생각은 무엇이었을까?"],
        "meaning": ["그 생각은 너에게 어떤 작은 위로를 건네고 싶어 했을까?"],
        "existential": ["이 감정이 너를 지금 이 순간으로 이끈 작은 실마리는 무엇일까?"],
    },
    "Warm Minimal": {
        "surface": ["그 순간 네가 가장 먼저 떠올린 생각은 무엇이었을까?"],
        "meaning": ["그 생각이 너에게 어떤 메시지를 전달하려 했을까?"],
        "existential": ["이 감정은 너의 오래된 패턴 중 어떤 부분과 닮아 있을까?"],
    },
    "Poetic": {
        "surface": ["그날의 너는 어떤 색을 띠고 있었을까?"],
        "meaning": ["그 감정은 너에게 어떤 은유를 속삭였을까?"],
        "existential": ["이 순간은 너의 이야기에서 어떤 장을 열고 닫았을까?"],
    },
    "Existential": {
        "surface": ["그 순간 네 안에서 가장 선명했던 생각은 무엇이었나?"],
        "meaning": ["그 생각은 네가 앞으로 어떤 선택을 하게 만들고 싶은가?"],
        "existential": ["이 감정이 너의 정체성에 어떤 흔적을 남길까?"],
    },
}


def generate_questions(
    analysis: Dict, events: Dict, tone: str = "Warm Minimal"
) -> Dict:
    tone_key = tone if tone in TEMPLATES else "Warm Minimal"
    tmpl = TEMPLATES[tone_key]

    # Surface 질문에는 사건 문장 중 첫 문장을 참조
    first_event = (
        events.get("events", [])[0]["text"] if events.get("events") else "그 사건"
    )

    q1 = tmpl["surface"][0]
    q2 = tmpl["meaning"][0]
    q3 = tmpl["existential"][0]

    # 약간의 맞춤형 변수 치환
    q1 = q1.replace(
        "그 순간", first_event if len(first_event) < 40 else first_event[:40] + "..."
    )

    epilogue = {
        "Pastel": "오늘 너는 자신의 마음에 조용히 손을 내밀었어. 그 작은 용기가 모여 내일이 된다는 걸 알아주면 좋겠다.",
        "Warm Minimal": "오늘 너는 스스로에게 작은 친절을 건넸다. 그걸 네가 먼저 알아주면 좋겠다.",
        "Poetic": "오늘의 감정은 한 폭의 그림처럼 네 안에 머물렀다. 그 색을 가만히 바라보자.",
        "Existential": "오늘의 선택들이 너를 조금 더 명확하게 만들었을지도 모른다. 그 흐름을 인지해도 좋아.",
    }.get(tone_key, "오늘 너는 자신의 하루를 조금 더 알아주었다.")

    return {"questions": [q1, q2, q3], "epilogue": epilogue}


if __name__ == "__main__":
    print(
        generate_questions(
            {"emotion": "불안"}, {"events": [{"text": "학교에서 긴장"}]}, "Pastel"
        )
    )
