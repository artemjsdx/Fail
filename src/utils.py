def current_datetime_utc():
    from datetime import datetime
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def split_text_for_tg(text: str, max_len: int = 3800) -> list:
    """Split text into chunks for Telegram (max 3800 chars)"""
    if len(text) <= max_len:
        return [text]
    chunks = []
    while text:
        chunks.append(text[:max_len])
        text = text[max_len:]
    return chunks

def gen_id(prefix: str = "") -> str:
    """Generate unique ID with optional prefix"""
    import uuid
    return f"{prefix}{str(uuid.uuid4())[:8]}" if prefix else str(uuid.uuid4())[:8]