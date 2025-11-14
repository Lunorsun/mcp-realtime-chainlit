import re
from typing import Dict, List

LOCATION_KEYWORDS = ["학교", "집", "회사", "카페", "거리", "지하철", "버스"]


def _split_sentences(text: str) -> List[str]:
    # 매우 간단한 문장 분리 (한국어에서 문장부호 기준)
    parts = re.split(r"[\.\!\?\n]+", text)
    return [p.strip() for p in parts if p.strip()]


def map_events(text: str) -> Dict:
    """Return structured events and a simple relation summary."""
    sents = _split_sentences(text)
    events = []
    for s in sents:
        loc = None
        for kw in LOCATION_KEYWORDS:
            if kw in s:
                loc = kw
                break
        # 원인 추출: '때문에', '그래서', '때문' 등
        cause = None
        m = re.search(r"(.+?)(?:때문에|때문|그래서|때문에|때문에\s*)(.+)", s)
        if m:
            # best-effort 구문
            cause = m.group(1).strip()
        events.append({"text": s, "location": loc or "-", "cause": cause or "-"})

    # 관계: 순차적 흐름으로 연결
    relations = []
    for i in range(len(events) - 1):
        relations.append(f"Event {i + 1} -> Event {i + 2}")

    return {"events": events, "relations": relations}


if __name__ == "__main__":
    print(map_events("학교에서 시험 때문에 긴장했어. 집에 와서는 혼자 쉬었어."))
