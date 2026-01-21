# disaster_ai.py

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import re
import time

# ---------------------------------------------------------
# Data models
# ---------------------------------------------------------
@dataclass
class DisasterContext:
    disaster_type: Optional[str] = None   # e.g., "Flood", "Cyclone", "Heatwave"
    state: Optional[str] = None           # e.g., "Tamil Nadu"
    district: Optional[str] = None        # e.g., "Chennai"
    risk_score: Optional[float] = None    # 0–100 if available
    year: Optional[int] = None

@dataclass
class AIResponse:
    title: str
    summary: str
    bullets: List[str]
    links: List[str]


# ---------------------------------------------------------
# Knowledge base (expand as needed)
# ---------------------------------------------------------
KB_FAQS: Dict[str, List[str]] = {
    "Flood": [
        "Move to higher ground immediately and avoid walking or driving through flood waters.",
        "Disconnect electrical appliances if safe; avoid contact with water near power sources.",
        "Carry essential documents, water, non-perishable food, flashlight, and first-aid kit.",
        "Follow official advisories from local disaster management authority and IMD updates.",
        "After flood: boil water, avoid contaminated areas, and report hazards to local authorities."
    ],
    "Cyclone": [
        "Secure windows and doors; bring outdoor items inside; prepare an emergency kit.",
        "Stay away from coastal areas and evacuate if instructed by authorities.",
        "Keep battery-powered radio/phone charged for official alerts.",
        "Do not go outside during the eye of the storm; conditions can worsen suddenly.",
        "After cyclone: watch for downed power lines, damaged structures, and avoid flood waters."
    ],
    "Heatwave": [
        "Stay hydrated; avoid direct sun during peak hours; wear light, loose clothing.",
        "Check on vulnerable people (elderly, children); never leave anyone in parked vehicles.",
        "Use ORS or electrolyte solutions if signs of dehydration appear.",
        "Limit strenuous activity; seek shade or cooled spaces.",
        "If symptoms of heatstroke (confusion, fainting), seek medical help immediately."
    ],
    "Drought": [
        "Conserve water; store safe drinking water; avoid wastage.",
        "Plan for rationing; prioritize essential uses; consider community water points.",
        "Protect livestock and crops with water-efficient practices.",
        "Follow local water authority advisories and schedules.",
        "Explore government relief schemes for drought-affected areas."
    ],
    "Landslide": [
        "Avoid steep slopes and unstable ground; evacuate if cracks or unusual sounds appear.",
        "Stay alert during/after heavy rain; do not return until authorities declare safety.",
        "Keep emergency kit ready; identify safe shelters.",
        "Report blocked drains or slope instability to local authorities.",
        "After landslide: watch for secondary slides and damaged infrastructure."
    ],
    "Storm Surge": [
        "Evacuate low-lying coastal areas when advised; avoid beaches and seawalls.",
        "Secure property; move valuables to higher floors.",
        "Monitor tide and surge warnings; follow coastal authority alerts.",
        "Do not drive through coastal flood waters.",
        "After surge: beware of contamination, debris, and structural damage."
    ],
    "Heavy Rain": [
        "Avoid waterlogged areas; check drainage; secure electrical connections.",
        "Carry rain gear and emergency supplies; plan travel carefully.",
        "Monitor local rainfall alerts and flood warnings.",
        "Do not shelter under isolated trees during lightning.",
        "After heavy rain: check for water contamination and structural issues."
    ],
    "Urban Flood": [
        "Avoid underpasses, basements, and low-lying roads; use elevated routes.",
        "Turn off power if water enters premises; avoid elevators.",
        "Keep emergency kit and waterproof bags for essentials.",
        "Follow municipal alerts on road closures and shelters.",
        "After urban flood: document damage for relief claims; disinfect living areas."
    ],
    "Flash Flood": [
        "Move to higher ground immediately; do not attempt to cross fast-moving water.",
        "Avoid driving; just 30 cm of water can float a car.",
        "Stay tuned to local alerts; conditions change rapidly.",
        "Keep emergency kit accessible at all times.",
        "After flash flood: avoid contaminated water and unstable ground."
    ]
}

KB_LINKS: Dict[str, List[str]] = {
    "Flood": [
        "https://ndma.gov.in/what-we-do/disaster-management/floods",
        "https://imd.gov.in/"
    ],
    "Cyclone": [
        "https://ndma.gov.in/what-we-do/disaster-management/cyclones",
        "https://rsmcnewdelhi.imd.gov.in/"
    ],
    "Heatwave": [
        "https://ndma.gov.in/heat-wave-guidelines",
        "https://mausam.imd.gov.in/"
    ],
    "Drought": [
        "https://ndma.gov.in/what-we-do/disaster-management/droughts"
    ],
    "Landslide": [
        "https://ndma.gov.in/what-we-do/disaster-management/landslides"
    ],
    "Storm Surge": [
        "https://ndma.gov.in/what-we-do/disaster-management/cyclones"
    ],
    "Heavy Rain": [
        "https://imd.gov.in/"
    ],
    "Urban Flood": [
        "https://ndma.gov.in/what-we-do/disaster-management/floods"
    ],
    "Flash Flood": [
        "https://ndma.gov.in/what-we-do/disaster-management/floods"
    ]
}


# ---------------------------------------------------------
# Utility: intent detection & classification
# ---------------------------------------------------------
INTENT_PATTERNS = {
    "what": r"\b(what|guidelines|steps|prepare|kit|checklist)\b",
    "when": r"\b(when|time|schedule|season|monsoon|peak)\b",
    "how": r"\b(how|evacuate|respond|survive|protect|avoid)\b",
    "where": r"\b(where|shelter|safe|route|zone|coastal|low-lying)\b",
    "alerts": r"\b(alert|warning|advisory|update|imd|ndma)\b"
}

def detect_intent(text: str) -> str:
    t = text.lower()
    for intent, pattern in INTENT_PATTERNS.items():
        if re.search(pattern, t):
            return intent
    return "general"


def classify_risk_level(score: Optional[float]) -> str:
    if score is None:
        return "Unknown"
    if score >= 80:
        return "High"
    elif score >= 70:
        return "Moderate"
    else:
        return "Low"


# ---------------------------------------------------------
# Retrieval: simple keyword overlap
# ---------------------------------------------------------
def retrieve_guidance(disaster_type: Optional[str], query: str) -> List[str]:
    if not disaster_type or disaster_type not in KB_FAQS:
        # fallback: merge all and pick top items by keyword overlap
        all_items = []
        for dt, items in KB_FAQS.items():
            for it in items:
                score = keyword_overlap(it.lower(), query.lower())
                all_items.append((score, dt, it))
        all_items.sort(key=lambda x: x[0], reverse=True)
        return [it for _, _, it in all_items[:5]]
    # disaster-specific
    items = KB_FAQS[disaster_type]
    scored = [(keyword_overlap(it.lower(), query.lower()), it) for it in items]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [it for _, it in scored[:5]]


def keyword_overlap(a: str, b: str) -> int:
    wa = set(re.findall(r"\w+", a))
    wb = set(re.findall(r"\w+", b))
    return len(wa & wb)


# ---------------------------------------------------------
# Safety & guardrails
# ---------------------------------------------------------
def safety_filter(text: str) -> bool:
    # Block harmful or non-actionable content patterns
    blocked = [
        r"\bsuicide\b", r"\bself-harm\b", r"\bhurt others\b",
        r"\bviolence\b", r"\battack\b", r"\bkill\b"
    ]
    t = text.lower()
    return not any(re.search(p, t) for p in blocked)


# ---------------------------------------------------------
# Core: Disaster AI
# ---------------------------------------------------------
class DisasterAI:
    def __init__(self):
        self.rate_limit_window = 3.0  # seconds
        self._last_ts = 0.0

    def _rate_limit(self):
        now = time.time()
        if now - self._last_ts < self.rate_limit_window:
            time.sleep(self.rate_limit_window - (now - self._last_ts))
        self._last_ts = time.time()

    def answer(
        self,
        question: str,
        context: Optional[DisasterContext] = None
    ) -> AIResponse:
        self._rate_limit()

        if not safety_filter(question):
            return AIResponse(
                title="Safety notice",
                summary="I can’t assist with harmful requests. For disaster-related guidance, ask about preparedness, evacuation, or official alerts.",
                bullets=[
                    "Ask about safe evacuation steps.",
                    "Request official alert sources.",
                    "Seek guidance on emergency kits and shelters."
                ],
                links=[]
            )

        intent = detect_intent(question)
        dt = (context.disaster_type if context and context.disaster_type else None)
        risk_level = classify_risk_level(context.risk_score if context else None)

        guidance = retrieve_guidance(dt, question)
        links = KB_LINKS.get(dt, []) if dt in KB_LINKS else ["https://ndma.gov.in/", "https://imd.gov.in/"]

        title = self._compose_title(dt, intent, risk_level, context)
        summary = self._compose_summary(dt, intent, risk_level, context)
        bullets = self._compose_bullets(guidance, intent, risk_level, context)

        return AIResponse(
            title=title,
            summary=summary,
            bullets=bullets,
            links=links
        )

    def _compose_title(
        self,
        dt: Optional[str],
        intent: str,
        risk_level: str,
        context: Optional[DisasterContext]
    ) -> str:
        loc = self._format_location(context)
        base = dt or "Disaster"
        return f"{base} guidance {loc}—{risk_level} risk"

    def _compose_summary(
        self,
        dt: Optional[str],
        intent: str,
        risk_level: str,
        context: Optional[DisasterContext]
    ) -> str:
        loc = self._format_location(context)
        rl = risk_level if risk_level != "Unknown" else "current"
        intent_map = {
            "what": "Key actions you can take now.",
            "when": "Timing and typical risk windows.",
            "how": "Step-by-step response guidance.",
            "where": "Safe areas and shelter considerations.",
            "alerts": "Where to find official alerts and updates.",
            "general": "Essential preparedness and response tips."
        }
        return f"{intent_map.get(intent, 'Essential guidance')} {loc} Risk level: {rl}."

    def _compose_bullets(
        self,
        guidance: List[str],
        intent: str,
        risk_level: str,
        context: Optional[DisasterContext]
    ) -> List[str]:
        bullets = []
        # Risk-aware lead-in
        if risk_level == "High":
            bullets.append("**Priority:** Follow evacuation orders and avoid hazardous areas immediately.")
        elif risk_level == "Moderate":
            bullets.append("**Priority:** Prepare to move; monitor official alerts frequently.")
        else:
            bullets.append("**Priority:** Maintain preparedness and review emergency plans.")

        # Location-aware note
        loc = self._format_location(context)
        if loc.strip():
            bullets.append(f"**Location:** Tailor actions to local advisories {loc} and municipal guidance.")

        # Core guidance from KB
        for tip in guidance:
            bullets.append(f"**Action:** {tip}")

        # Official sources
        bullets.append("**Official alerts:** Check NDMA/IMD portals and local disaster management authority.")
        return bullets

    def _format_location(self, context: Optional[DisasterContext]) -> str:
        if not context:
            return ""
        parts = []
        if context.district:
            parts.append(context.district)
        if context.state:
            parts.append(context.state)
        return f"in {', '.join(parts)}" if parts else ""


# ---------------------------------------------------------
# Example usage (remove if importing as a module)
# ---------------------------------------------------------
if __name__ == "__main__":
    ai = DisasterAI()
    ctx = DisasterContext(disaster_type="Flood", state="Tamil Nadu", district="Chennai", risk_score=89)
    resp = ai.answer("What should I do right now?")
    print(resp.title)
    print(resp.summary)
    for b in resp.bullets:
        print("-", b)
    print("Links:", resp.links)
