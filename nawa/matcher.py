import time
import random

def simulate_match(image_path: str) -> dict:
    """
    Dummy face‑match simulator.
    Returns a dict with (name, confidence, latency_ms).
    """
    t0 = time.time()

    # --- محاكاة زمن المطابقة بين 2‑3 ثوانٍ ---
    time.sleep(random.uniform(2.0, 3.0))
    latency = int((time.time() - t0) * 1000)

    # --- نتيجة وهمية ---
    result = {
        "name": "volunteer_001",
        "confidence": round(random.uniform(92.0, 99.5), 1),
        "latency_ms": latency
    }
    return result

