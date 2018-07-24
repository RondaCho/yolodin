from django import forms
from django.conf import settings


class TuiEditorWidget(forms.Textarea):
    template_name = 'widgets/tuieditor_widget.html'

    class Media:
        css = {
           'all': [
               'codemirror/lib/codemirror.css',
               'highlightjs/styles/github.css',
               'tui-editor/dist/tui-editor.css',
               'tui-editor/dist/tui-editor-contents.css',
           ],
        }
        js = [
               '//code.jquery.com/jquery-2.2.4.min.js',
               'tui-code-snippet/dist/tui-code-snippet.js',
               'markdown-it/dist/markdown-it.js',
               'to-mark/dist/to-mark.js',
               'codemirror/lib/codemirror.js',
               'highlightjs/highlight.pack.js',
               'squire-rte/build/squire.js',
               'tui-editor/dist/tui-editor-Editor.min.js',
            ]

    def build_attrs(self, *args, **kwargs):
       attrs = super().build_attrs(*args, **kwargs)
       attrs['style'] = 'display: none;'  # 있지만 보여지지 않게.
       return attrs


class LocationWidget(forms.TextInput):
    template_name = 'widgets/location_widget.html'

    class Media:
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
            'https://maps.googleapis.com/maps/api/js?key=' + settings.GOOGLE_MAP_API_KEY,  # FIXME: Google Maps Javascript API 키 적용
        ]

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['GOOGLE_MAP_API_KEY'] = settings.GOOGLE_MAP_API_KEY
        return context

    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs['readonly'] = True
        attrs['style'] = 'background-color:#eee; border: 0; width: 20rem;'
        return attrs


class PreviewClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/preview_clearable_file_input.html'

    class Media:
        js = [
            '//code.jquery.com/jquery-2.2.4.min.js',
        ]