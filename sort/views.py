#!-*- conding: utf8 -*-
from random import randint

import openpyxl

from django.shortcuts import render
from sort.forms import UploadFileForm


def sorteador(request):
    """
    Renderiza a página inicial e o input file.
    :param request:
    :return:
    """
    form = UploadFileForm()

    return render(request, 'sort/sorteio.html', {'form': form})


def sorteio(request):
    """
    Função que carrega o arquivo xlsx, sorteia uma linha aleatoria e exibe dados das celulas da linha
    :param request:
    :return:
    """
    if "GET" == request.method:
        form = UploadFileForm()

        return render(request, 'sort/sorteio.html', {'form': form})
    else:
        file = request.FILES["file"]
        wb = openpyxl.load_workbook(file)

        sheetranges = wb['sheet1']

        numero_linhas = sheetranges.max_row
        linha_aleatoria = randint(2, numero_linhas)

        numero_sorteado = sheetranges['A' + str(linha_aleatoria)].value
        nome_sorteado = sheetranges['B' + str(linha_aleatoria)].value

        return render(request, 'sort/sorteio.html', {'numero': numero_sorteado, 'nome': nome_sorteado})
