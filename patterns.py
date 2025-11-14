import json
from pathlib import Path
from typing import Dict, List

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
PATTERNS_FILE = DATA_DIR / "patterns.json"


def _load() -> List[Dict]:
    if not PATTERNS_FILE.exists():
        return []
    try:
        return json.loads(PATTERNS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save(all_entries: List[Dict]):
    PATTERNS_FILE.write_text(
        json.dumps(all_entries, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def save_entry(entry: Dict):
    all_entries = _load()
    all_entries.append(entry)
    _save(all_entries)


def analyze_patterns() -> Dict:
    entries = _load()
    if not entries:
        return {"summary": "저장된 항목이 없습니다.", "details": {}}

    # 가장 빈번한 감정
    freq = {}
    for e in entries:
        emo = e.get("analysis", {}).get("emotion", "?")
        freq[emo] = freq.get(emo, 0) + 1

    most = max(freq.items(), key=lambda x: x[1])
    summary = f"최근 기록에서 '{most[0]}' 감정이 가장 자주 나타납니다 ({most[1]}회)."

    return {"summary": summary, "frequencies": freq, "count": len(entries)}


if __name__ == "__main__":
    save_entry({"date": "2025-11-14", "analysis": {"emotion": "불안"}, "text": "예시"})
    print(analyze_patterns())
