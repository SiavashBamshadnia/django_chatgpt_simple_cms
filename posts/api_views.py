from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from posts import chatgpt


@api_view(['POST'])
def generate_title_from_content(request: Request):
    content = request.data.get('content')

    if content:
        content = content.strip()

    if not content:
        raise ValidationError('Missing `content` parameter')

    chatgpt_response = chatgpt.generate_title_from_content(content)
    return Response(chatgpt_response)


@api_view(['POST'])
def generate_summary_from_content(request: Request):
    content = request.data.get('content')

    if content:
        content = content.strip()

    if not content:
        raise ValidationError('Missing `content` parameter')

    chatgpt_response = chatgpt.generate_summary_from_content(content)
    return Response(chatgpt_response)


@api_view(['POST'])
def generate_content_from_title(request: Request):
    title = request.data.get('title')

    if title:
        title = title.strip()

    if not title:
        raise ValidationError('Missing `title` parameter')

    chatgpt_response = chatgpt.generate_content_from_title(title)
    return Response(chatgpt_response)


@api_view(['POST'])
def generate_content_from_summary(request: Request):
    summary = request.data.get('summary')

    if summary:
        summary = summary.strip()

    if not summary:
        raise ValidationError('Missing `summary` parameter')

    chatgpt_response = chatgpt.generate_content_from_summary(summary)
    return Response(chatgpt_response)
