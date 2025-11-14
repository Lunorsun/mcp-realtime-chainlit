import traceback

import chainlit as cl
from chainlit.logger import logger
from dotenv import load_dotenv

load_dotenv(override=True)

from groq_client import create_default_client


def _extract_text_from_groq_response(resp: dict) -> str:
    """Try common response shapes and return a text summary."""
    if not resp:
        return ""

    # Common keys to check
    if isinstance(resp, dict):
        # Groq model responses may include `output`, `outputs`, `choices`, or model-specific keys
        if "output" in resp and isinstance(resp["output"], str):
            return resp["output"]
        if "outputs" in resp and isinstance(resp["outputs"], list):
            parts = []
            for o in resp["outputs"]:
                if isinstance(o, str):
                    parts.append(o)
                elif isinstance(o, dict) and "content" in o:
                    parts.append(str(o["content"]))
            if parts:
                return "\n".join(parts)
        if "choices" in resp and isinstance(resp["choices"], list) and resp["choices"]:
            first = resp["choices"][0]
            # try common shapes
            if isinstance(first, dict):
                for k in ("text", "message", "content"):
                    if k in first and isinstance(first[k], str):
                        return first[k]
                # nested message content
                if "message" in first and isinstance(first["message"], dict):
                    msg = first["message"]
                    if "content" in msg and isinstance(msg["content"], str):
                        return msg["content"]

    # Fallback to stringifying the response
    try:
        return str(resp)
    except Exception:
        return ""


@cl.on_chat_start
async def start():
    logger.info("Chat session started (Groq backend)")
    try:
        # Create a Groq client and store it in the session
        groq = create_default_client()
        cl.user_session.set("groq_client", groq)
        return True
    except Exception as e:
        logger.error(f"Failed to initialize Groq client: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        await cl.ErrorMessage(content=f"Failed to initialize Groq client: {e}").send()
        return False


@cl.on_message
async def on_message(message: cl.Message):
    try:
        groq = cl.user_session.get("groq_client")
        if not groq:
            logger.error("Groq client not found in session")
            await cl.ErrorMessage(content="Groq client not initialized").send()
            return

        # Send the user's text to Groq and return the generated text
        resp = groq.generate(
            prompt=message.content, max_output_tokens=512, temperature=0.0
        )
        text = _extract_text_from_groq_response(resp)

        if not text:
            text = "(모델이 응답을 생성하지 못했습니다.)"

        reply = cl.Message(content=text, author="assistant")
        await reply.send()

    except Exception as e:
        logger.error(f"Error in on_message: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        await cl.ErrorMessage(content=f"Error processing message: {str(e)}").send()


@cl.on_audio_start
async def on_audio_start():
    # Audio streaming isn't supported with the simple Groq HTTP client.
    logger.info("Audio recording started - not supported with Groq HTTP backend")
    return False


@cl.on_audio_chunk
async def on_audio_chunk(chunk: cl.InputAudioChunk):
    # We don't support streaming audio to Groq via this simple client.
    logger.warning(
        "Received audio chunk but audio input is not supported with Groq backend"
    )


@cl.on_audio_end
async def on_audio_end():
    logger.info("Audio recording ended")
    return True


@cl.on_chat_end
@cl.on_stop
async def on_end():
    logger.info("Chat session ending")
    # Nothing to disconnect for the simple HTTP Groq client
