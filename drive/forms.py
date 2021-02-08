from django import forms
from .views import AyenDrive


class UploadAyenFileForm(forms.Form):
    title = forms.CharField(max_length=128)
    file = forms.FileField()


class UploadAyenFileModelForm(forms.ModelForm):
    class Meta:
        model = AyenDrive
        fields = [ 'title', 'file' ]

    # make sure uploaded file is a powerpoint or pdf
    def clean_file(self):
        file = self.cleaned_data['file']
        print(file)
        file_name = file.name
        if not file_name.lower().endswith(('.pdf', '.pptx')):
            raise forms.ValidationError("only powerpoint or pdf files allowed")

        return file


class SearchAyenFileForm(forms.Form):
    keyword = forms.CharField()