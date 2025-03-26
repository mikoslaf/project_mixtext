from django.shortcuts import render

from pesel_validator.forms import UploadPeselForm
from pesel_validator.utils import pesel_get_date, pesel_get_gender, pesel_is_vaild


def pesel_validator(request):
    form = UploadPeselForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        pesel = form.cleaned_data['pesel']
        if pesel_is_vaild(pesel):
            date_of_birth = pesel_get_date(pesel)
            gender = pesel_get_gender(pesel)
            return render(request, 'pesel_validator/pesel_form.html', {'form': form, 'gender': gender, 'date_of_birth': date_of_birth})

        return render(request, 'pesel_validator/pesel_form.html', {'form': form, 'error': 'Invalid PESEL.'})

    return render(request, 'pesel_validator/pesel_form.html', {'form': form})