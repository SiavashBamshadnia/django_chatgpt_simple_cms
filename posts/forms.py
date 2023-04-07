from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe


def generate_button(id, text):
    """
    Generates an HTML button element with a specific style and text.

   Args:
       id (str): The ID of the button element.
       text (str): The text to display on the button.

   Returns:
       str: An HTML button element.
   """
    return f'<button class="button" id={id} style="padding: 10px 15px; margin: 0 0 5px 5px; height: fit-content;">{text}</button>'


class TitleWidget(widgets.TextInput):
    """
    A custom form widget that displays a text input field with a "Generate from content" button.

    The "Generate from content" button creates a title from the content of the post using ChatGPT.
    """

    def render(self, *args, **kwargs):
        super_call = super().render(*args, **kwargs)
        return mark_safe(
            f'{super_call}'
            f'{generate_button("generate-title-from-content", "Generate from content")}')


class SummaryWidget(forms.Textarea):
    """
    A custom form widget that displays a textarea field with a "Generate from content" button.

    The "Generate from content" button creates a summary from the content of the post using ChatGPT.
    """

    def render(self, *args, **kwargs):
        self.attrs['class'] = 'vLargeTextField'
        super_call = super().render(*args, **kwargs)
        return mark_safe(
            f'{super_call}'
            f'{generate_button("generate-summary-from-content", "Generate from content")}')


class ContentWidget(forms.Textarea):
    """
    A custom form widget that displays a textarea field with two "Generate" buttons.

    The "Generate from title" button creates content from the title of the post.
    The "Generate from summary" button creates content from the summary of the post.
    """

    def render(self, *args, **kwargs):
        self.attrs['class'] = 'vLargeTextField'
        super_call = super().render(*args, **kwargs)
        return mark_safe(
            f'{super_call}'
            f'{generate_button("generate-content-from-title", "Generate from title")}'
            f'{generate_button("generate-content-from-summary", "Generate from summary")}')


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=TitleWidget)
    summary = forms.Field(widget=SummaryWidget, help_text='In markdown format')
    content = forms.Field(widget=ContentWidget, help_text='In markdown format')

    class Media:
        js = [
            'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js',  # To send HTTP requests
            'js/posts_change_form.js'
        ]
