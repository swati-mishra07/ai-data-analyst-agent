import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Create client only if API key exists
client = None
if api_key:
    client = OpenAI(api_key=api_key)


def generate_insights(summary):
    """
    Generate AI insights from dataset summary.
    If OpenAI API fails, return basic summary analysis instead.
    """

    # Fallback if API key missing
    if client is None:
        return f"""
OpenAI API key not found.

Basic Dataset Summary:
{summary}
"""

    try:
        prompt = f"""
You are a professional data scientist.

Analyze the dataset summary below and provide:

1. Key patterns
2. Important trends
3. Potential anomalies
4. Business insights

Dataset Summary:
{summary}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an data analyst."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.5,
        )

        insights = response.choices[0].message.content
        return insights

    except Exception as e:

        # Handle quota errors
        if "insufficient_quota" in str(e) or "429" in str(e):
            return f"""
OpenAI quota exceeded.

Basic Dataset Summary:
{summary}
"""

        # General fallback
        return f"""
AI analysis failed.

Basic Dataset Summary:
{summary}
"""
