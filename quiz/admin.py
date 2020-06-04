from django.contrib import admin
from .models import Quiz, MCImage, ChooseSentenceQuestion, ChooseWordQuestion, PosNegQuestion, ResponseQuestion

admin.site.register(Quiz)
admin.site.register(MCImage)
admin.site.register(ChooseSentenceQuestion)
admin.site.register(ChooseWordQuestion)
admin.site.register(PosNegQuestion)
admin.site.register(ResponseQuestion)
