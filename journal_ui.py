import datetime
import traceback

import chainlit as cl
from chainlit.logger import logger

from analyzer import analyze_text
from emotion_trends import (
    get_emotion_flow,
    get_insight,
    get_weekly_summary,
    record_emotion,
)
from event_mapper import map_events
from patterns import analyze_patterns, save_entry
from questions import generate_questions
from recommendations import get_recommendation, get_selfcare_tip
from tone_config import get_emotion_emoji, get_intensity_bar

# 사용자가 선택한 톤 저장
SELECTED_TONE = "Pastel"


@cl.on_chat_start
async def start():
    # 초기 안내 메시지 (파스텔 감성)
    welcome = "오늘의 마음을 들여다보는 시간\n\n한 줄로 적어주세요. 당신의 하루가 무엇인지, 지금 어떤 기분인지.\n그 안에서 함께 의미를 찾아봐요.\n\n💡 /help 명령어로 모든 기능을 확인하세요"
    await cl.Message(content=welcome, author="system").send()

    # 톤 선택 버튼 (Chainlit 최신 버전 호환)
    tone_msg = cl.Message(content="어떤 톤으로 질문을 받고 싶으신가요?")
    tone_msg.actions = [
        cl.Action(
            name="select_tone",
            label="따뜻하고 부드러운 (기본)",
            payload={"tone": "Pastel"},
        ),
        cl.Action(
            name="select_tone", label="시적이고 은유적인", payload={"tone": "Poetic"}
        ),
        cl.Action(
            name="select_tone", label="깊고 철학적인", payload={"tone": "Existential"}
        ),
    ]
    await tone_msg.send()

    return True


@cl.action_callback("select_tone")
async def on_select_tone(action):
    """톤 선택 버튼 콜백 핸들러"""
    global SELECTED_TONE
    tone_value = action.payload.get("tone", "Pastel")

    tone_names = {
        "Pastel": "따뜻하고 부드러운",
        "Poetic": "시적이고 은유적인",
        "Existential": "깊고 철학적인",
    }

    SELECTED_TONE = tone_value
    tone_desc = tone_names.get(tone_value, "파스텔")

    await cl.Message(
        content=f"톤이 '{tone_desc}'로 설정되었습니다. 이제 오늘의 마음을 적어주세요.",
        author="system",
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    try:
        user_text = message.content.strip()

        # 명령어 처리
        if user_text.startswith("/"):
            await handle_command(user_text)
            return

        if not user_text:
            await cl.ErrorMessage(content="짧게라도 한 줄 적어주세요.").send()
            return

        # 애니메이션/로딩 메시지
        loading = cl.Message(content="분석 중...", author="system")
        await loading.send()

        # 분석 파이프라인
        analysis = analyze_text(user_text)
        events = map_events(user_text)
        # 선택된 톤 사용
        q_and_epi = generate_questions(analysis, events, tone=SELECTED_TONE)

        # 감정 트렌드 기록
        record_emotion(analysis["emotion"], analysis["intensity"])

        # 카드 1: 감정 시그니처
        emoji = get_emotion_emoji(analysis["emotion"])
        intensity_bar = get_intensity_bar(analysis["intensity"])
        emo_card = f"**오늘의 감정 시그니처**\n\n{emoji} {analysis['emotion']}\n{intensity_bar}\n\n방향: {analysis['direction']}"
        await cl.Message(content=emo_card, author="system").send()

        # 카드 2: 사건 지도
        ev_texts = []
        for i, e in enumerate(events.get("events", []), start=1):
            ev_texts.append(
                f"  • {e['text']}\n    - 장소: {e['location']} | 원인: {e['cause']}"
            )
        ev_card = "**하루의 사건 흐름**\n\n" + "\n".join(ev_texts)
        await cl.Message(content=ev_card, author="system").send()

        # 카드 3: 3단계 질문
        qs = q_and_epi.get("questions", [])
        q_lines = [f"{i + 1}. {q}" for i, q in enumerate(qs)]
        q_card = "**성찰 질문 (3단계)**\n\n" + "\n\n".join(q_lines)
        await cl.Message(content=q_card, author="system").send()

        # 에필로그
        epi = q_and_epi.get("epilogue", "")
        await cl.Message(content=f"**에필로그**\n\n{epi}", author="system").send()

        # 카드 4: 감정별 권장사항
        rec = get_recommendation(analysis["emotion"])
        rec_card = f"**{rec['message']}**\n\n{get_selfcare_tip(analysis['emotion'])}"
        await cl.Message(content=rec_card, author="system").send()

        # 저장 및 패턴 분석
        entry = {
            "date": datetime.date.today().isoformat(),
            "text": user_text,
            "analysis": analysis,
            "events": events,
        }
        save_entry(entry)
        patterns = analyze_patterns()
        save_msg = f"**기록 저장됨**\n\n{patterns['summary']}"
        await cl.Message(content=save_msg, author="system").send()

        # 다시 기록하기 안내
        await cl.Message(
            content="원하면 다시 기록하세요 — 또 다른 순간, 또 다른 감정이 있으면 남겨주세요.",
            author="system",
        ).send()

    except Exception as e:
        logger.error(f"Error in journal flow: {e}")
        logger.error(traceback.format_exc())
        await cl.ErrorMessage(content=f"분석 중 오류가 발생했습니다: {e}").send()


async def handle_command(command: str):
    """명령어 처리."""
    global SELECTED_TONE

    cmd = command.lower().strip()
    
    if cmd == "/주간":
        summary = get_weekly_summary()
        await cl.Message(content=summary, author="system").send()
    
    elif cmd == "/흐름":
        flow = get_emotion_flow()
        await cl.Message(content=flow, author="system").send()
    
    elif cmd == "/통찰":
        insight = get_insight()
        await cl.Message(content=f"**이번 주 통찰**\n\n{insight}", author="system").send()
    
    elif cmd == "/톤변경":
        tone_msg = cl.Message(content="톤을 다시 선택해주세요:")
        tone_msg.actions = [
            cl.Action(
                name="select_tone",
                label="따뜻하고 부드러운",
                payload={"tone": "Pastel"}
            ),
            cl.Action(
                name="select_tone",
                label="시적이고 은유적인",
                payload={"tone": "Poetic"}
            ),
            cl.Action(
                name="select_tone",
                label="깊고 철학적인",
                payload={"tone": "Existential"}
            ),
        ]
        await tone_msg.send()
    
    elif cmd == "/help" or cmd == "/도움":
        help_msg = """**오늘의 자아 로그 - 사용 가이드**

**💬 기본 사용법**
감정, 하루, 기분을 한 줄로 적어주세요.
예) "오늘 프로젝트가 완료돼서 너무 뿌듯해"

**🎭 톤 선택**
따뜻하고 부드러운 (기본)
시적이고 은유적인
깊고 철학적인

**📊 분석 결과**
• 감정 시그니처: 오늘의 감정과 강도
• 사건 흐름: 하루의 주요 사건들
• 성찰 질문: 3단계 깊이 있는 질문
• 에필로그: 감정에 어울리는 마무리
• 자기돌봄: 감정별 따뜻한 조언

**🔧 명령어 모음**
/주간 - 이번 주 감정 요약 보기
/흐름 - 최근 5개 감정의 흐름 보기
/통찰 - 주간 감정 기반 통찰 받기
/톤변경 - 질문 톤 다시 선택하기
/help, /도움 - 이 안내 보기

**💡 팁**
• 여러 번 기록할수록 패턴 분석이 정확해집니다
• 같은 감정만 반복되지 않습니다
• 모든 기록은 자동 저장됩니다"""
        await cl.Message(content=help_msg, author="system").send()
    
    else:
        await cl.Message(
            content="사용 가능한 명령어:\n/주간 - 주간 감정 요약\n/흐름 - 최근 감정 흐름\n/통찰 - 감정 기반 통찰\n/톤변경 - 톤 다시 선택\n/help - 전체 안내 보기",
            author="system",
        ).send()