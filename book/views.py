from django.shortcuts import render
from django.http import HttpResponse


def one(request):
    return HttpResponse('人生没有白走的路，每一步都算数')

def two(request):
    return HttpResponse('Человек есть тайна, её надо разгадать')


def three(request):
    return HttpResponse('Do not wait for the perfect moment; create it yourself')
