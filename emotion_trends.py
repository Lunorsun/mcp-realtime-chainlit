"""감정 트렌드 및 주간 분석 기능."""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
TRENDS_FILE = DATA_DIR / "emotion_trends.json"


def load_trends() -> dict:
    """감정 트렌드 데이터 로드."""
    if TRENDS_FILE.exists():
        with open(TRENDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"weekly": {}, "monthly": {}}


def save_trends(trends: dict):
    """감정 트렌드 데이터 저장."""
    DATA_DIR.mkdir(exist_ok=True)
    with open(TRENDS_FILE, "w", encoding="utf-8") as f:
        json.dump(trends, f, ensure_ascii=False, indent=2)


def record_emotion(emotion: str, intensity: int):
    """감정 기록."""
    trends = load_trends()
    today = datetime.now().strftime("%Y-%m-%d")
    week_key = datetime.now().strftime("%Y-W%V")

    if "weekly" not in trends:
        trends["weekly"] = {}
    if "monthly" not in trends:
        trends["monthly"] = {}

    if week_key not in trends["weekly"]:
        trends["weekly"][week_key] = []

    trends["weekly"][week_key].append(
        {"date": today, "emotion": emotion, "intensity": intensity}
    )

    save_trends(trends)


def get_weekly_summary() -> str:
    """주간 감정 요약."""
    trends = load_trends()
    week_key = datetime.now().strftime("%Y-W%V")

    if week_key not in trends.get("weekly", {}):
        return "아직 기록된 감정이 없습니다."

    week_data = trends["weekly"][week_key]
    emotions = [entry["emotion"] for entry in week_data]
    counter = Counter(emotions)

    summary_lines = ["**이번 주 감정 지도**\n"]
    for emotion, count in counter.most_common():
        bar = "●" * count
        summary_lines.append(f"{emotion}: {bar} ({count}회)")

    return "\n".join(summary_lines)


def get_emotion_flow() -> str:
    """최근 감정의 흐름 시각화."""
    trends = load_trends()
    week_key = datetime.now().strftime("%Y-W%V")

    if week_key not in trends.get("weekly", {}):
        return "아직 기록이 없습니다."

    week_data = trends["weekly"][week_key]
    if not week_data:
        return "오늘은 아직 기록이 없습니다."

    # 최근 5개 기록
    recent = week_data[-5:]
    flow_lines = ["**최근 감정 흐름** (최근 5개)\n"]

    for i, entry in enumerate(recent, 1):
        emotion = entry["emotion"]
        intensity = entry["intensity"]
        bar = "●" * intensity + "○" * (5 - intensity)
        flow_lines.append(f"{i}. {emotion} {bar}")

    return "\n".join(flow_lines)


def get_insight() -> str:
    """감정 데이터 기반 통찰."""
    trends = load_trends()
    week_key = datetime.now().strftime("%Y-W%V")

    if week_key not in trends.get("weekly", {}):
        return "아직 충분한 데이터가 없습니다."

    week_data = trends["weekly"][week_key]
    if len(week_data) < 2:
        return "더 많은 기록이 필요합니다."

    emotions = [entry["emotion"] for entry in week_data]
    most_common = Counter(emotions).most_common(1)[0][0]

    insights = {
        "성취": f"이번 주 너는 {len(week_data)}번 자신의 성취를 기록했어. 그 작은 성취들이 모여 큰 변화를 만들고 있어.",
        "기대": f"이번 주 너는 설레는 마음으로 {len(week_data)}번을 기록했어. 그 기대감이 너를 앞으로 나아가게 해.",
        "불안": f"이번 주 불안감을 {len(week_data)}번 마주했어. 그렇지만 모든 순간을 견뎌낸 너는 충분히 강해.",
        "고요": f"이번 주 {len(week_data)}번의 고요함 속에서 너는 충전하고 있었어.",
        "회피": f"이번 주 {len(week_data)}번 피하고 싶은 마음이 있었군. 천천히 마주해보는 것도 괜찮아.",
        "지침": f"이번 주 {len(week_data)}번 길을 찾으려 애썼어. 그 과정 자체가 너를 성장시키고 있어.",
    }

    return insights.get(most_common, "계속해서 자신의 감정을 기록해주세요.")
