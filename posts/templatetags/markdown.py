import markdown as md
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    """
    Convert Markdown text to HTML.

    Args:
        value (str): The Markdown text to be converted.

    Returns:
        str: The corresponding HTML string.
    """
    return md.markdown(value)


@register.filter()
@stringfilter
def safemarkdown(value):
    """
    Convert Markdown text to HTML and mark it as safe for rendering.

    Args:
        value (str): The Markdown text to be converted.

    Returns:
        django.utils.safestring.SafeString: The corresponding HTML string.
    """
    return mark_safe(markdown(value))
