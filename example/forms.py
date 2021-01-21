from django import forms
from .models import GeeksModel
from .models import FlashcardsModel

# creating a form


class GeeksForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]


# creating a form
class FlashcardsForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = FlashcardsModel

        # specify fields to be used
        fields = [
            "frontside",
            "backside",
            "answer",
        ]
