import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


# ---------------- CONFIGURATION ----------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from the .env file")

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-3.8-flash"


# ---------------- GEMINI HELPER ----------------

def generate_with_retry(prompt: str) -> str:
    """
    Generate a response using Gemini.

    Temporary 503 server errors are retried up to 3 times.
    429 quota errors are not retried because retrying will
    not restore an exhausted API quota.
    """

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text

        except errors.ClientError as e:

            # 429 = API quota exhausted
            if getattr(e, "code", None) == 429:
                print("Gemini API quota exceeded.")
                raise

            raise

        except errors.ServerError:

            if attempt == 2:
                raise

            wait_time = 2 ** attempt

            print(
                f"Gemini temporarily unavailable. "
                f"Retrying in {wait_time} seconds..."
            )

            time.sleep(wait_time)

    raise RuntimeError("Gemini request failed.")


# ---------------- HOME PLANNER ----------------

def generate_home_recommendations(
    budget: int,
    room: str,
    items: str,
    style: str
) -> str:

    prompt = f"""
You are PocketSmart AI, a smart budget-friendly home interior recommendation assistant.

User details:
- Budget: ₹{budget}
- Room: {room}
- Required items: {items}
- Preferred style: {style}

Create practical recommendations that stay within the user's budget.

Include:

1. A short plan for the room.
2. Recommended items with approximate budget allocation.
3. Suggested quantity where appropriate.
4. Budget-friendly alternatives.
5. A final estimated total.
6. One short money-saving tip.

Important:
- Do not exceed the user's stated budget.
- Keep recommendations realistic for an Indian user.
- Make the response clear and easy to understand.
- Do not invent exact product prices.
- Do not claim current product availability.
"""

    try:

        return generate_with_retry(prompt)

    except (errors.ServerError, errors.ClientError):

        return f"""
HOME INTERIOR PLAN

Budget: ₹{budget}
Room: {room}
Style: {style}


BUDGET ALLOCATION

• Furniture: 40% of budget
• Lighting: 15% of budget
• Storage: 15% of budget
• Decor: 15% of budget
• Miscellaneous: 15% of budget


RECOMMENDATIONS

For a {style.lower()} {room.lower()}, prioritize essential furniture
and functional storage first.

Required items:

{items}

Choose simple, durable and budget-friendly options.
Prefer multipurpose furniture and compare prices before purchasing.


ESTIMATED TOTAL

Keep the total spending within ₹{budget}.


MONEY-SAVING TIP

Prioritize essential items first and add decorative pieces gradually.
"""


# ---------------- PARTY PLANNER ----------------

def generate_party_recommendations(
    budget: int,
    guests: int,
    event: str,
    venue: str,
    requirements: str
) -> str:

    prompt = f"""
You are PocketSmart AI, a smart budget-friendly party planning assistant.

Create a practical party plan for an Indian user.

Budget: ₹{budget}
Guests: {guests}
Event: {event}
Venue: {venue}
Requirements: {requirements}

Give the response in this format:

PARTY PLAN

A short description of the overall plan.


BUDGET BREAKDOWN

- Food:
- Decoration:
- Cake:
- Entertainment:
- Other expenses:


RECOMMENDATIONS

Give practical suggestions for the party.


MONEY-SAVING TIP

Give one useful money-saving tip.


FINAL ESTIMATED TOTAL

Give an estimated total that does not exceed ₹{budget}.

Important:
- Stay within the stated budget.
- Use approximate costs, not exact current prices.
- Keep the recommendations realistic for India.
- Make the response clear and easy to read.
"""

    try:

        return generate_with_retry(prompt)

    except (errors.ServerError, errors.ClientError):

        return f"""
PARTY PLAN

Budget: ₹{budget}
Guests: {guests}
Event: {event}
Venue: {venue}


BUDGET BREAKDOWN

• Food: 40% of budget
• Decoration: 15% of budget
• Cake: 10% of budget
• Entertainment: 10% of budget
• Other expenses: 25% of budget


RECOMMENDATIONS

Plan food quantities according to the number of guests.

Use simple decorations that can be reused.

Choose a reasonably sized cake and prioritize essential expenses.


MONEY-SAVING TIP

Prepare or arrange some decorations yourself and compare food
options before finalizing the order.


FINAL ESTIMATED TOTAL

Keep the total spending within ₹{budget}.
"""


# ---------------- JEWELRY PLANNER ----------------

def generate_jewelry_recommendations(
    budget: int,
    occasion: str,
    style: str,
    requirements: str
) -> str:

    prompt = f"""
You are PocketSmart AI, a smart budget-friendly jewelry recommendation assistant.

Create practical jewelry recommendations for an Indian user.

User details:

- Budget: ₹{budget}
- Occasion: {occasion}
- Preferred style: {style}
- Requirements: {requirements}

Include:

1. A suitable jewelry plan.
2. Recommended jewelry pieces with approximate budget allocation.
3. Suitable materials and styles.
4. Budget-friendly alternatives.
5. A final estimated total.
6. One money-saving tip.

Important:
- Do not exceed the user's stated budget.
- Keep recommendations realistic.
- Do not claim exact current product availability.
"""

    try:

        return generate_with_retry(prompt)

    except (errors.ServerError, errors.ClientError):

        return f"""
JEWELRY PLAN

Budget: ₹{budget}
Occasion: {occasion}
Style: {style}


SUGGESTED ALLOCATION

• Main jewelry piece: 50–60%
• Matching earrings: 20–25%
• Additional accessories: 10–15%
• Buffer: 10%


RECOMMENDATIONS

Choose versatile pieces that can be reused for multiple occasions.

Consider lightweight designs and budget-friendly materials.


MONEY-SAVING TIP

Prioritize the main jewelry piece and choose simple matching
accessories to stay within your budget.


FINAL ESTIMATED TOTAL

Keep the total spending within ₹{budget}.
"""