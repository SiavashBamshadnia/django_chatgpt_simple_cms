import openai
from django.conf import settings


def send_prompt(prompt):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_title_from_content(content):
    chatgpt_response = send_prompt(
        f"Generate a title for this article. Do not use quotations:\n\n{content}"
    )
    return chatgpt_response


def generate_summary_from_content(content):
    chatgpt_response = send_prompt(
        f"Generate a summary for this article:\n\n{content}"
    )
    return chatgpt_response


def generate_content_from_title(text):
    chatgpt_response = send_prompt(
        f"Generate the article's content from this title in markdown format. start from h2:\n\n{text}"
    )
    return chatgpt_response


def generate_content_from_summary(text):
    chatgpt_response = send_prompt(
        f"Generate the article's content from this summary in markdown format. start from h2:\n\n{text}"
    )
    return chatgpt_response
