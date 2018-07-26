from django import forms

from .models import FacePhoto


class FaceIdentifyForm(forms.ModelForm):
    class Meta:
        model = FacePhoto
        fields = [
            "user_name",
            "photo",
            "threshold",
            "res_n",
        ]
