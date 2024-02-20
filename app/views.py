from django.shortcuts import render
import random, scipy,math
from .models import Task, Kol
from math import factorial, exp
import numpy as np, sympy
from scipy.special import comb
from sympy import symbols, sqrt, cos, pi

import docx
from docx.shared import Pt
# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
import subprocess
from reportlab.lib.pagesizes import A4


from django.conf import settings
from django.core.mail import EmailMessage

def index(request):
    return render(request, 'app/index.html')
def vibor(request):
    tem = request.GET.get('nametema')
    sl = request.GET.get('slozhntema')
    ko = request.GET.get('kol')
    if not ko:
        numbers = []
        for i in Kol.objects.all():
            numbers.append(int(i.koli))
        if sl == 'ur1':
            if tem == 'klasopr':
                run = random.choice(['z1','z2','z3','z4'])
                if run=='z1':
                    s = ["Из "," собранных на заводе телевизоров "," бракованных. Эксперт проверяет один наугад выбранный телевизор. Найдите вероятность того, что проверяемый телевизор окажется бракованным."]
                    n = random.randint(10, 100)
                    m = random.randint(2, n//5)
                    s1 = s[0] + str(n) + s[1] + str(m) + s[2] + ' Ответ: ' + str(round(m/n, 2))
                if run=='z2':
                    s = ['Абонент забыл последние 2 цифры телефонного номера, но помнит, что они различны и образуют двузначное число, меньшее ','. С учетом этого он набирает наугад 2 цифры. Найти вероятность того, что это будут нужные цифры.']
                    a = random.randint(10,60)
                    s1 = s[0]+str(a)+s[1]+' Ответ: '+str(round(1/a, 2))
                if run=='z3':
                    s = ['В среднем из ',' садовых насосов ',' подтекают. Найти вероятность того, что один случайно выбранный для контроля насос не подтекает.']
                    n = random.randint(100, 500)
                    m = random.randint(2, n//50)
                    s1 = s[0]+str(n)+s[1]+str(m)+s[2]+' Ответ: '+str(round((n-m)/n, 3))
                if run=='z4':
                    s = ['Вероятность того, что новый DVD-проигрыватель в течении года поступит в гарантийный ремонт равна ','. В некотором городе из ',' проданных DVD-проигрывателей в течении года в гарантийную мастерскую поступило ','. На сколько отличается частота события "гарантийный ремонт" от его вероятности в этом городе?']
                    p = random.random()
                    n = random.randint(200, 2000)
                    m = random.randint(20, n//10)
                    s1 = s[0]+str(round(p,2))+s[1]+str(n)+s[2]+str(m)+s[3]+' Ответ: '+str(round(abs(m/n-round(p,3)),3))
            if tem == 'deistviya-nad-sob':
                run = random.choice(['z1','z2','z3','z4'])
                if run=='z1':
                    z = ['В ящике ',' мячиков одинаковых размеров: ',' красных, ',' синих и ',' белых. Вычислить вероятность того, что не глядя будет взят цветной (не белый) мячик.']
                    a = random.randint(2, 20)
                    b = random.randint(2, 20)
                    c = random.randint(2, 20)
                    n = a + b + c
                    s1 = z[0]+str(n)+z[1]+str(a)+z[2]+str(b)+z[3]+str(c)+z[4]+' Ответ: '+str(round((a+b)/n,2))
                if run=='z2':
                    z = ['Цель в тире разделена на 3 зоны. Вероятность того, что некий стрелок выстрелит в цель в первой зоне равна ',', во второй зоне – ',', в третьей зоне – ','. Найти вероятность того, что стрелок попадет в цель и вероятность того, что стрелок попадёт мимо цели.']
                    d = 2
                    while (d>=1):
                        a = round(random.random(),2)
                        b = round(random.random(),2)
                        c = round(random.random(),2)
                        d = round(a+b+c,2)
                    s1 = z[0]+str(a)+z[1]+str(b)+z[2]+str(c)+z[3]+' Ответ: '+str(d)+' '+str(round(1-d,2))
                if run=='z3':
                    z = ['На автогонках при заезде на первой автомашине вероятность победить ',', при заезде на второй автомашине ','. Найти: вероятность того, что победят обе автомашины, вероятность того, что победит хотя бы одна автомашина.']
                    a = round(random.random(), 2)
                    b = round(random.random(), 2)
                    j = a+b-a*b
                    s1 = z[0]+str(a)+z[1]+str(b)+z[2]+' Ответ: '+str(round(j,2))
                if run=='z4':
                    z = ['Монету бросают ',' раза подряд. Найти вероятность того, что все ',' раза выпадет герб.']
                    a = random.randint(2,4)
                    s1 = z[0]+str(a)+z[1]+str(a)+z[2]+' Ответ: '+str((1/2)**a)
            if tem == 'geom':
                run = random.choice(['z1','z2','z3'])
                if run=='z1':
                    z = ['Дана нитка длиной ',' см. Нитка рвется в случайном месте. Какова вероятность, что после обрыва имеется часть нитки длиной не менее ',' см.']
                    a = random.randint(3, 20)
                    b = random.randint(a // 2 + 1, a - 1)
                    n = a - b
                    s2 = round((n * 2) / a, 3)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + ' Ответ: ' + str(s2)
                if run=='z2':
                    z = ['Какова вероятность вашей встречи с другом, если вы договорились встретиться в определенном месте, с ',' до ', ' часов и ждете друг друга в течение ', ' минут?']
                    a = random.randint(0, 24)
                    b = a + 1
                    c = random.randint(1, 59)
                    m = 60
                    s2 = round((m * m - ((m - c) * (m - c))) / (m * m), 2)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(s2)
                if run=='z3':
                    z = ['На отрезок [', ';','] наудачу бросается случайная точка. Какова вероятность того, что она будет принадлежать промежутку [',';', ']?']
                    a = random.randint(0, 5)
                    b = random.randint(6, 10)
                    c = random.randint(a, 5)
                    d = random.randint(6, b)
                    s2 = round(((d - c) / (b - a)), 2)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + ' Ответ: ' + str(s2)
            if tem == 'slozh-umn-ver':
                run = random.choice(['z1','z2','z3'])
                if run=='z1':
                    m = ['Вероятность хотя бы одного попадания в цель при ', ' выстрелах равна ',
                         ' Найти вероятность попадания в цель при одном выстреле.']
                    q = random.randint(1, 10)
                    n = random.randint(1, 6)
                    f = round(1 - pow((1 - n / 10), q), 3)
                    s1 = m[0] + str(q) + m[1] + str(n / 10) + m[2] + ' Oтвет: ' + str(f)
                if run=='z2':
                    m = ['Для сигнализации об аварии установлены два независимо работающих сигнализатора. Вероятность того, что при аварии сигнализатор сработает, равна ',' для первого сигнализатора и ',' для второго. Найти вероятность того, что при аварии сработает только один сигнализатор.']
                    p1 = random.randint(1, 10) / 10
                    p2 = random.randint(1, 10) / 10
                    f = round(p1 * (1 - p2) + p2 * (1 - p1), 3)
                    s1 = m[0] + str(p1) + m[1] + str(p2) + m[2] + ' Ответ: ' + str(f)
                if run=='z3':
                    n = random.randint(2, 5)
                    a = [0] * n
                    for i in range(n):
                        a[i] = random.randint(1, 9) / 10
                    f = 1 - a[0]
                    for i in range(n):
                        f *= 1 - a[i]
                    f = f / (1 - a[0])
                    s1 = str(n) + ' учащихся на экзамене независимо друг от друга решают одну и ту же задачу. ' \
                                  'Вероятности ее решения этими учащимися равны:\n'
                    for i in range(n):
                        s1 += str(a[i]) + '\n'
                    s1 += 'Найдите вероятность того, что хотя бы один учащийся решит задачу. Oтвет: ' + str(round(1 - f, 3))
            if tem == 'fpv':
                run = random.choice(['z1','z2','z3'])
                if run == 'z1':
                    z = ['На первом заводе из каждых 100 лампочек производится в среднем ',' стандартных, на втором - ', ', на третьем - ',', а продукция этих заводов составляет соответственно ', '%, ', '% и ','% всех электролампочек, поставляемых в магазины некоторого района. Найти вероятность приобретения стандартной электролампочки.']
                    a = random.randint(50, 100)
                    b = random.randint(50, 100)
                    c = random.randint(50, 100)
                    d = random.randint(10, 50)
                    e = random.randint(10, 50)
                    n = 100 - (d + e)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + str(n) + z[6] + ' Ответ: ' + str(round((a / 100) * (d / 100) + (b / 100) * (e / 100) + (c / 100) * (n / 100), 2))
                if run == 'z2':
                    z = ['Из 1000 ламп ', ' принадлежат к 1 партии ',' - ко второй партии, остальные к третьей. В первой партии ', ' % брака, во второй - ',' %, в третьей - ',' %. Наудачу выбирается одна лампа. Определить вероятность того, что выбранная лампа - бракованная.']
                    a = random.randint(2, 500)
                    b = random.randint(2, 500)
                    c = random.randint(2, 10)
                    d = random.randint(2, 10)
                    e = random.randint(2, 10)
                    n = 1000 - (a + b)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + ' Ответ: ' + str(round((a / 1000) * (c / 100) + (b / 1000) * (d / 100) + (n / 1000) * (e / 100), 2))
                if run == 'z3':
                    z = ['Имеются три одинаковых на вид урны: в первой ', ' белых шара и ', ' черных, во второй - ',' белых и ', ' черных, в третьей - ',' белых шара. Некто подходит наугад к одной из урн и вынимает из нее один шар. Найти вероятность того, что этот шар будет белым.']
                    a = random.randint(2, 10)
                    b = random.randint(2, 10)
                    c = random.randint(2, 10)
                    d = random.randint(2, 10)
                    e = random.randint(2, 10)
                    n = a + b
                    m = c + d
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + ' Ответ: ' + str(round((1 / 3) * (a / n) + (1 / 3) * (c / n) + (1 / 3) * (e / e), 2))
            if tem == 'bayes':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    def calculateBayes(p_a, p_b_given_a, p_b_given_not_a):
                        p_not_a = 1 - p_a
                        p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
                        p_a_given_b = (p_b_given_a * p_a) / p_b
                        return p_a_given_b

                    p_a = round(random.uniform(0.8, 0.9), 2)
                    p_b_given_a = round(random.uniform(0.90, 0.97), 2)
                    p_b_given_not_a = round(random.uniform(0.02, 0.6), 2)
                    p_a_given_b = round(calculateBayes(p_a, p_b_given_a, p_b_given_not_a), 2)
                    problemCondition = f'Вы разрабатываете систему фильтрации спама для электронной почты. Известно, что {p_a * 100}% всех отправленных писем ' \
                    f'являются спамом. Ваша система имеет точность {p_b_given_a * 100}%,то есть она правильно помечает {p_b_given_not_a}% спам-писем как спам, ' \
                    f'и 5% легитимных писем помечает как спам. Определенное письмо было помечено как спам вашей системой. Какова вероятность того, что оно ' \
                    f'действительно является спамом?'
                    s1 = f'\n{problemCondition} Ответ: {p_a_given_b}'
                if run == 'z2':
                    def calculateBayes(prob_a, prob_b_given_a, prob_b_given_not_a):  # расчет формулы Байеса
                        return (prob_a * prob_b_given_a) / (
                                    (prob_a * prob_b_given_a) + ((1 - prob_a) * prob_b_given_not_a))

                    diseaseProb = round(random.uniform(0.01, 0.1), 2)  # вероятность поражения населения болезнью
                    diseasePositiveProb = round(random.uniform(0.8, 0.95),
                                                2)  # вероятность того, что тест распознает болезнь
                    diseasePositiveNotProb = round(random.uniform(0, 0.05),
                                                   2)  # вероятность того, что тест даст ложноположительный результат
                    ans = round(calculateBayes(diseaseProb, diseasePositiveProb, diseasePositiveNotProb),
                                2)  # вероятность того, что человек действительно болен
                    problemCondition = f'Есть определенная болезнь, которая поражает {int(diseaseProb * 100)}% населения. Существует тест, который правильно ' \
                    f'распознает болезнь в {int(diseasePositiveProb * 100)}% случаев, но также дает ложноположительные результаты в ' \
                    f'{int(diseasePositiveNotProb * 100)}% случаев на здоровых людях. Если человек получил положительный результат теста, какова вероятность того, ' \
                    f'что он действительно болен?'
                    s1 = f'\n{problemCondition} Ответ: {ans}'
                if run == 'z3':
                    def calculateBayes(hypothesisProb, groupNumProb, probA):
                        return hypothesisProb * groupNumProb / probA
                    def conditionalProbability(classicProb1, classicProb2, classicProb3, prob1, prob2, prob3):
                        return prob1 * classicProb1 + prob2 * classicProb2 + prob3 * classicProb3
                    def maximum(prob1, prob2, prob3):
                        probs = [prob1, prob2, prob3]
                        maximum, maxNum = -1, 0
                        for groupNumber, probability in enumerate(probs):
                            if probability > maximum:
                                maximum = probability
                                maxNum = groupNumber
                        return maximum, maxNum + 1
                    total = random.randint(25, 35)  # количество стрелков
                    groupOne = random.randint(6, 12)  # количество стрелков
                    groupTwo = random.randint(5, groupOne)  # в каждой
                    groupThree = total - groupOne - groupTwo  # группе
                    shooterInGroupOneProb = round(total / groupOne, 2)
                    shooterInGroupTwoProb = round(total / groupTwo, 2)
                    shooterInGroupThreeProb = round(total / groupThree, 2)
                    shooterInGroupOne = round(random.uniform(0.4, 0.75), 2)
                    shooterInGroupTwo = round(random.uniform(0.3, 0.85), 2)
                    shooterInGroupThree = round(random.uniform(0.4, 0.65), 2)
                    probA = round(
                        conditionalProbability(groupOne, groupTwo, groupThree, shooterInGroupOne, shooterInGroupTwo,
                                               shooterInGroupThree), 2)
                    probH1A = round(calculateBayes(shooterInGroupOneProb, shooterInGroupOne, probA), 3)
                    probH2A = round(calculateBayes(shooterInGroupTwoProb, shooterInGroupTwo, probA), 3)
                    probH3A = round(calculateBayes(shooterInGroupThreeProb, shooterInGroupThree, probA), 3)
                    maximum, maxNum = maximum(probH1A, probH2A, probH3A)
                    problemCondition = f'Из {total} стрелков {groupOne} попадает в цель с вероятностью {shooterInGroupOne}, {groupTwo} - с вероятностью ' \
                    f'{shooterInGroupTwo} и {groupThree} – с вероятностью {shooterInGroupThree}. Наудачу выбранный стрелок произвел выстрел, поразив цель. ' \
                    f'К какой из групп вероятнее всего принадлежал этот стрелок?'
                    s1 = f'\n{problemCondition} Ответ: {maxNum}'
            if tem == 'bern':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ["Пусть проводится n = "," независимых испытаний, в каждом из которых вероятность появления события A постоянна и равна p = ",
                         ". Найти вероятность того, что в данной серии испытаний событие A появится m = ", " раза."]
                    n = random.randint(2, 10)
                    m = random.randint(1, n)
                    p = round(random.uniform(0.1, 1), 2)
                    q = 1 - p
                    f = round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 3)
                    s1 = z[0] + str(n) + z[1] + str(p) + z[2] + str(m) + z[3] + ' Ответ: ' + str(f)
                if run == 'z2':
                    z = ["Пусть вероятность того, что телевизор потребует ремонта в течение гарантийного срока, равна ",
                         ". Найти вероятность того, что в течение гарантийного срока из ",
                         " телевизоров: а) не более одного потребует ремонта; б) хотя бы один не потребует ремонта."]
                    n = random.randint(2, 10)
                    p = round(random.uniform(0.1, 0.5), 2)
                    q = 1 - p
                    p_1 = round((factorial(n) / (factorial(1) * factorial(n - 1))) * (p ** 1) * (q ** (n - 1)), 5)
                    p_0 = q ** n
                    f1 = round(p_1 + p_0, 4)
                    f2 = round(1 - (p ** n), 4)
                    s1 = z[0] + str(p) + z[1] + str(n) + z[2] + " Ответ: a) " + str(f1) + " б) " + str(f2)
                if run == 'z3':
                    z = ["Семья собирается купить "," kinder сюрприза. Вероятность того, что сюрпризом будет машинка, равна ",
                         ". Вероятность того, что сюрпризом будет кукла, равна ", ". Какова вероятность того, что из "," Kinder Сюрпризов сын может достать ровно ",
                         " машинок?"]
                    n = random.randint(2, 10)
                    p = round(random.uniform(0.1, 1), 2)
                    q = round(1 - p, 2)
                    m = random.randint(1, n // 2)
                    f = round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                    s1 = z[0] + str(n) + z[1] + str(p) + z[2] + str(q) + z[3] + str(n) + z[4] + str(m) + z[5] + ' Ответ: ' + str(f)
            if tem == 'naiv':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Вероятность появления события в каждом испытании равна ','. Сколько нужно провести испытаний, чтобы наивероятнейшее число появлений события равнялось '
                        ,'? ']
                    p = (random.randint(1, 99)) / 100
                    k = random.randint(1, 20)
                    q = 1 - p
                    ma = (k + q) / p
                    mi = (k - p) / p
                    n = int(mi) - 1
                    while not (mi < n < ma):
                        n += 1
                    s1 = z[0] + str(p) + z[1] + str(k) + z[2] + 'Ответ: ' + str(n)
                if run == 'z2':
                    z = ['При автоматической наводке орудия вероятность попадания по быстро движущейся цели равна ','. Найти наивероятнейшее число попаданий при ',
                         ' выстрелах. ']
                    p = (random.randint(1, 99)) / 100
                    n = random.randint(1, 100)
                    q = 1 - p
                    mi = n * p - q
                    ma = n * p + p
                    k = int(mi) - 1
                    while not (mi < k < ma):
                        k += 1
                    s1 = z[0] + str(p) + z[1] + str(n) + z[2] + 'Ответ: ' + str(k)
                if run == 'z3':
                    z = ['Данные длительной проверки качества выпускаемых стандартных деталей показали, что в среднем брак составляет ',
                         '%. Определить наиболее вероятное число вполне исправных деталей в партии из ', ' штук. ']
                    proc = random.randint(1, 15)
                    q = proc / 100
                    p = 1 - q
                    n = random.randint(1, 300)
                    mi = n * p - q
                    ma = n * p + p
                    k = int(mi) - 1
                    while not (mi < k < ma):
                        k += 1
                    s1 = z[0] + str(proc) + z[1] + str(n) + z[2] + 'Ответ: ' + str(k)
            if tem == 'muavr-laplas':
                run = random.choice(['z1', 'z2'])
                if run == 'z1':
                    m = ['Вероятность рождения мальчика равна ', '. Найти вероятность того, что среди ',' новорожденных окажется ', ' мальчиков. ']
                    p = random.randint(45, 55) / 100
                    n = random.randint(7, 9) * 10
                    k = random.randint(40, 60)
                    q = 1 - p
                    f1 = abs(1 / pow(n * p * q, 1 / 2))
                    x = (k - n * p) / (pow(n * p * q, 1 / 2))
                    ex1 = math.e ** -((x ** 2) / 2) / ((math.pi * 2) ** (1 / 2))
                    otvet = round(f1 * ex1, 3)
                    while (otvet * 1000 == 0):
                        p = random.randint(45, 55) / 100
                        n = random.randint(7, 9) * 10
                        k = random.randint(40, 60)
                        q = 1 - p
                        f1 = abs(1 / pow(n * p * q, 1 / 2))
                        x = (k - n * p) / (pow(n * p * q, 1 / 2))
                        ex1 = math.e ** -((x ** 2) / 2) / ((math.pi * 2) ** (1 / 2))
                        otvet = round(f1 * ex1, 3)
                    s1 = m[0] + str(p) + m[1] + str(n) + m[2] + str(k) + m[3] + 'Ответ: ' + str(otvet)
                if run == 'z2':
                    m = ['На конвейер за смену поступает  ',' изделий. Вероятность того, что поступившая на конвейер деталь стандартна, равна  ',
                         '. Найти вероятность того, что стандартных деталей на конвейер за смену поступило ровно ']
                    p = random.randint(35, 45) / 100
                    n = random.randint(80, 110)
                    k = random.randint(30, 50)
                    q = 1 - p
                    f1 = abs(1 / pow(n * p * q, 1 / 2))
                    x = (k - n * p) / (pow(n * p * q, 1 / 2))
                    ex1 = math.e ** -((x ** 2) / 2) / ((math.pi * 2) ** (1 / 2))
                    otvet = round(f1 * ex1, 3)
                    while (otvet * 1000 == 0):
                        p = random.randint(35, 45) / 100
                        n = random.randint(80, 110)
                        k = random.randint(30, 50)
                        q = 1 - p
                        f1 = abs(1 / pow(n * p * q, 1 / 2))
                        x = (k - n * p) / (pow(n * p * q, 1 / 2))
                        ex1 = math.e ** -((x ** 2) / 2) / ((math.pi * 2) ** (1 / 2))
                        otvet = round(f1 * ex1, 3)
                    s1 = m[0] + str(n) + m[1] + str(p) + m[2] + str(k) + '. Ответ: ' + str(otvet)
            if tem == 'int-muavr-laplas':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Найти вероятность того, что если бросить монету ', ' раз, то орел выпадет от ', ' до ',' раз. ']
                    obsh = random.randint(100, 150)
                    orel = random.randint(int(obsh * 0.4), int(obsh * 0.7))
                    moneta = random.randint(int(obsh * 0.2), orel - 1)
                    p = 0.5
                    q = 1 - p
                    f1 = round((orel - obsh * p) / ((obsh * p * q) ** (0.5)), 2)
                    f2 = round((moneta - obsh * p) / ((obsh * p * q) ** (0.5)), 2)
                    f = (scipy.stats.norm.cdf(f1) - 0.5) - (scipy.stats.norm.cdf(f2) - 0.5)
                    while (int(f * 100) == 0):
                        obsh = random.randint(100, 150)
                        orel = random.randint(int(obsh * 0.4), int(obsh * 0.7))
                        moneta = random.randint(int(obsh * 0.2), orel - 1)
                        p = 0.5
                        q = 1 - p
                        f1 = round((orel - obsh * p) / ((obsh * p * q) ** (0.5)), 2)
                        f2 = round((moneta - obsh * p) / ((obsh * p * q) ** (0.5)), 2)
                        f = (scipy.stats.norm.cdf(f1) - 0.5) - (scipy.stats.norm.cdf(f2) - 0.5)
                    s1 = z[0] + str(obsh) + z[1] + str(moneta) + z[2] + str(orel) + z[3] + 'Ответ: ' + str(round(f,3))
                if run == 'z2':
                    z = ['Страховая компания заключила ',' договоров. Вероятность страхового случая по каждому из них в течение года составляет ',
                         '%. Найти вероятность, что таких случаев будет не более ', '. ']
                    n = random.randint(4000, 4500)
                    p = random.randint(2, 10) / 100
                    q = 1 - p
                    ma = random.randint(500, 900)
                    f1 = (ma - n * p) / ((n * p * q) ** 0.5)
                    f2 = (0 - n * p) / ((n * p * q) ** 0.5)
                    f = (scipy.stats.norm.cdf(f1) - 0.5) - (scipy.stats.norm.cdf(f2) - 0.5)
                    while (int(f * 100) == 0):
                        n = random.randint(40000, 45000)
                        p = random.randint(2, 10) / 100
                        q = 1 - p
                        ma = random.randint(500, 900)
                        f1 = (ma - n * p) / ((n * p * q) ** 0.5)
                        f2 = (0 - n * p) / ((n * p * q) ** 0.5)
                        f = (scipy.stats.norm.cdf(f1) - 0.5) - (scipy.stats.norm.cdf(f2) - 0.5)
                    s1 = z[0] + str(n) + z[1] + str(int(p * 100)) + z[2] + str(ma) + z[3] + 'Ответ: ' + str(round(f, 3))
                if run == 'z3':
                    z = ['Вероятность выхода из строя за смену одного станка равна ','. Определить вероятность выхода из строя от ', ' до ',
                         ' станков при наличии ', ' станков. ']
                    p = random.randint(10, 20) / 100
                    q = 1 - p
                    n = random.randint(100, 300)
                    m1 = random.randint(1, 5)
                    m2 = random.randint(m1 + 1, 20)
                    f1 = (m1 - n * p) / ((n * p * q) ** 0.5)
                    f2 = (m2 - n * p) / ((n * p * q) ** 0.5)
                    f = (scipy.stats.norm.cdf(f1) - 0.5) - (scipy.stats.norm.cdf(f2) - 0.5)
                    while (int(f * 100) == 0):
                        p = random.randint(10, 20) / 100
                        q = 1 - p
                        n = random.randint(100, 300)
                        m1 = random.randint(1, 5)
                        m2 = random.randint(m1 + 1, 20)

                        f1 = (m1 - n * p) / ((n * p * q) ** 0.5)
                        f2 = (m2 - n * p) / ((n * p * q) ** 0.5)
                        f = (scipy.stats.norm.cdf(f1) - 0.5) - (scipy.stats.norm.cdf(f2) - 0.5)
                    s1 = z[0] + str(p) + z[1] + str(m1) + z[2] + str(m2) + z[3] + str(n) + z[4] + 'Ответ: ' + str(round(abs(f), 3))
            if tem == 'puass':
                run = random.choice(['z1', 'z2','z3'])
                if run == 'z1':
                    z = ['Станок штампует детали. Вероятность того, что изготовленная деталь бракованная, равна ','. Какова вероятность того, что среди ',
                         ' деталей окажется ', ' бракованных']
                    n = random.randint(100, 200)
                    k = random.randint(2, 5)
                    p = round(random.uniform(0.02, 0.05), 2)

                    v = n * p
                    pys = round(((v ** k) / factorial(k)) * exp(-v), 5)
                    s1 = z[0] + str(p) + z[1] + str(n) + z[2] + str(k) + z[3] + ' Ответ: ' + str(pys)
                if run == 'z2':
                    z = ['Автобиография писателя издается тиражом в ',' экземпляров. Для каждой книги вероятность быть неправильно сброшюрованной равна ',
                         '. Найти вероятность того, что тираж содержать ровно ', ' бракованных книг.']
                    p = round(random.uniform(0.001, 0.005), 3)
                    n = random.randint(1000, 2000)
                    q = 1 - p
                    k = random.randint(2, 7)
                    v = n * p
                    pys = round(((v ** k) / factorial(k)) * exp(-v), 5)
                    s1 = z[0] + str(n) + z[1] + str(p) + z[2] + str(k) + z[3] + ' Ответ: ' + str(pys)
                if run == 'z3':
                    z = ["Вероятность изготовления нестандартной детали равна ", ". Найти вероятность того, что среди "," деталей окажется ", " нестандартных."]
                    p = round(random.uniform(0.002, 0.005), 3)
                    n = random.randint(1000, 2000)
                    k = random.randint(2, 7)
                    v = n * p
                    pys = round(((v ** k) / factorial(k)) * exp(-v), 5)
                    s1 = z[0] + str(p) + z[1] + str(n) + z[2] + str(k) + z[3] + ' Ответ: ' + str(pys)
            if tem == 'diskr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Бросают n = ',' игральных костей. Найти математическое ожидание суммы числа очков, которые выпадут на всех гранях.']
                    a = random.randint(2, 10)
                    s1 = z[0] + str(a) + z[1] + ' Ответ: ' + str((1 / 6 * (1 + 2 + 3 + 4 + 5 + 6)) * a)
                if run == 'z2':
                    z = ['Охотник стреляет по дичи до первого попадания, но успевает сделать не более четырех выстрелов. Вероятность попадания в цель при одном выстреле равна ',
                         ' . Найти дисперсию этой случайной величины.']
                    a = random.randint(1, 99) / 100
                    s1 = z[0] + str(a) + z[1] + ' Ответ: ' + str(round(0 * a + 1 * a * (1 - a) + 4 * a * (1 - a) * (1 - a) + 9 * a * (1 - a) * (1 - a) * (1 - a) + 16 * (1 - a) * (1 - a) * (1 - a) * (1 - a) - (0 * a + 1 * a * (1 - a) + 2 * a * (1 - a) * (1 - a) + 3 * a * (1 - a) * (1 - a) * (1 - a) + 4 * (1 - a) * (1 - a) * (1 - a) * (1 - a)) ** 2, 3))
                if run == 'z3':
                    z = ['Стрелок, имея 3 патрона, стреляет в цель до первого попадания. Вероятности попадения при первом, втором и третьем выстрелах соответственно ',', ',
                         ' и ', '. Чему равно математическое ожидание числа оставшихся патронов?']
                    a = random.randint(10, 90)
                    b = random.randint(10, 90)
                    c = random.randint(10, 90)
                    n = a / 100
                    m = b / 100
                    k = c / 100
                    s1 = z[0] + str(n) + z[1] + str(m) + z[2] + str(k) + z[3] + ' Ответ: ' + str(round((2 * n) + (1 * (1 - n) * m) + (0 * (1 - n) * (1 - m)), 3))
            if tem == 'nepr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run =='z1':
                    def exponentialDistribution(lambdaValue, x):
                        return 1 - (math.exp(-x[0] / lambdaValue) - math.exp(-x[1] / lambdaValue))
                    lambdaValue = round(random.uniform(0.5, 15), 2)
                    x = [0, random.randint(1, 10)]
                    probability = exponentialDistribution(lambdaValue, x)
                    problemCondition = f'Пусть X - случайная величина с экспоненциальным распределением с параметром lambda = {lambdaValue}. Найдите вероятность того, что X ' \
                    f'примет значение меньше или равное {x[1]}.'
                    s1 = f"\n{problemCondition}\n\nОтвет: {round(probability, 2)}"
                if run == 'z2':
                    def triangularDistribution(a, b, c):
                        mean = round((a + b + c) / 3, 2)
                        variance = round((a ** 2 + b ** 2 + c ** 2 - a * b - a * c - b * c) / 18, 2)
                        return mean, variance

                    # Пример использования функции
                    a = round(random.uniform(1, 15), 2)
                    b = round(random.uniform(1, 15), 2)
                    c = round(random.uniform(1, 15), 2)
                    mean, variance = triangularDistribution(a, b, c)
                    problemCondition = f'Пусть X - случайная величина с треугольным распределением на интервале [{a}, {b}] с максимальным значением в точке {c}. Найти ' \
                    f'математическое ожидание и дисперсию этой случайной величины.'
                    s1 = f'\n{problemCondition} Ответ: {mean} {variance}'
                if run == 'z3':
                    def uniformDistribution(a, b):
                        mean = round((a + b) / 2, 2)
                        variance = round(((b - a) ** 2) / 12, 2)
                        return mean, variance

                    a = round(random.uniform(1, 15), 2)
                    b = round(random.uniform(1, 15), 2)
                    mean, variance = uniformDistribution(a, b)
                    problemCondition = f'Пусть X - случайная величина с равномерным распределением на интервале [{a}, {b}]. Найти среднее значение (математическое ожидание) ' \
                    f'и дисперсию этой случайной величины.'
                    s1 = f'\n{problemCondition} Ответ: {mean} {variance}'
            if tem == 'norm':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Размер детали задан полем допуска ', '-', ' мм. Оказалось, что средний размер деталей равен ',' мм, а квадратичное отклонение ',
                         ' мм. Считая, что размер детали подчиняется закону нормального распределения, определить вероятность появления брака.']
                    a = random.randint(1, 10)
                    b = random.randint(11, 20)
                    c = random.randint(a + 2, 18)
                    d = random.randint(1, 9)
                    s2 = round((b - c) / d, 2)
                    s3 = round((a - c) / d, 2)
                    f = scipy.stats.norm.cdf(s2)
                    f1 = scipy.stats.norm.cdf(s3)
                    otvet = abs(f - f1)  # может быть отрицательным, поэтому берем модуль abs()
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + ' Ответ: ' + str(round(otvet, 3))
                if run == 'z2':
                    z = ['Требуется найти вероятность того, что нормально распределённая случайная величина, где a = ',' - математическое ожидание, σ = ',
                         ' - среднее квадратичное отклонение случайной величины X, принимает значения: меньше ']
                    a = random.randint(1, 10)  # мат ожидание
                    b = random.randint(1, 9)  # ско
                    c = random.randint(1, a)
                    s2 = round((c - a) / b, 2)
                    f = scipy.stats.norm.cdf(s2)
                    otvet = abs(f + 0.5)  # может быть отрицательным, поэтому берем модуль abs()
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + '. Ответ: ' + str(round(otvet, 3))
                if run == 'z3':
                    z = ['Случайная величина X имеет нормальное распределение с математическим ожиданием a = ',' и дисперсией D(x) = ',
                         '. Найти вероятность попадания этой случайной величины на интервал (',',', '). ']
                    a = random.randint(1, 10)
                    b = random.randint(2, 9)
                    c = random.randint(a + 1, 15)
                    d = random.randint(16, 20)
                    s2 = b ** (1 / 2)
                    s3 = round((d - a) / s2, 2)
                    s4 = round((c - a) / s2, 2)
                    f = scipy.stats.norm.cdf(s3)
                    f1 = scipy.stats.norm.cdf(s4)
                    otvet = round(abs(f - f1), 3)  # может быть отрицательным, поэтому берем модуль abs()
                    while (int(otvet * 1000) == 0):
                        a = random.randint(1, 10)
                        b = random.randint(2, 9)
                        c = random.randint(a + 1, 15)
                        d = random.randint(16, 20)

                        s2 = b ** (1 / 2)
                        s3 = round((d - a) / s2, 2)
                        s4 = round((c - a) / s2, 2)
                        f = scipy.stats.norm.cdf(s3)
                        f1 = scipy.stats.norm.cdf(s4)
                        otvet = round(abs(f - f1), 3)  # может быть отрицательным, поэтому берем модуль abs()
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + 'Ответ: ' + str(otvet)

            vop = int(request.GET.get('numbervop'))
            Task.objects.filter(nomer=vop).delete()
            Task(zadacha=s1, nomer=vop).save()
            return render(request, 'app/vibor.html',
                          {'task': s1, 'nametem': tem, 'slozh': sl, 'numbervop': vop, 'numbers': numbers})
        if sl == 'ur2':
            if tem == 'klasopr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['В лифт ', '-этажного дома на первом этаже зашли ', ' человека. И поехали. Найти вероятность того, что они выйдут на разных этажах.']
                    p = random.randint(6, 20)
                    h = random.randint(2, 5)
                    h1 = h
                    c = p - 1
                    n = c ** h
                    m = 1
                    while (h1 > 0):
                        m = m * (p - h1)
                        h1 = h1 - 1
                    f = round(m / n, 3)
                    s1 = z[0] + str(p) + z[1] + str(h) + z[2] + ' Ответ: ' + str(f)
                if run == 'z2':
                    z = ['В лифт ', '-этажного дома на первом этаже зашли ', ' человека. И поехали. Найти вероятность того, что они выйдут на одном этаже.']
                    n = 100000
                    while (n > 9000):
                        p = random.randint(6, 20)
                        h = random.randint(2, 5)
                        c = p - 1
                        n = c ** h
                    f = round(c / n, 3)
                    s1 = z[0] + str(p) + z[1] + str(h) + z[2] + ' Ответ: ' + str(f)
                if run == 'z3':
                    z = ['Подбрасывается k = ', ' монет. Найти вероятность того, что на ',' монетах выпадет орёл, а на остальных – решка.']
                    p = random.randint(3, 10)
                    h = random.randint(1, 9)
                    while (p < h):
                        p = random.randint(3, 10)
                        h = random.randint(1, 9)
                    n = 2 ** p
                    c = factorial(p) / (factorial(h) * factorial(p - h))
                    f = round(c / n, 3)
                    s1 = z[0] + str(p) + z[1] + str(h) + z[2] + ' Ответ: ' + str(f)
            if tem == 'deistviya-nad-sob':
                s1 = 'Задачи отсутствуют'
            if tem == 'geom':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['В треугольник со сторонами а = ', ', b = ', ', с = ',
                         ' вписан круг. Точка М произвольно ставится в треугольник. Найти вероятность того, что точка попадет в круг.']
                    a = random.randint(3, 9)
                    b = random.randint(3, 9)
                    c = random.randint(3, 9)
                    p = (a + b + c) / 2
                    s2 = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                    s3 = 3.14 * ((s2 / p) ** 2)

                    while (s2 == 0 or (s3 / s2) * 1000 == 0):
                        a = random.randint(3, 9)
                        b = random.randint(3, 9)
                        c = random.randint(3, 9)
                        p = (a + b + c) / 2
                        s2 = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                        s3 = 3.14 * ((s2 / p) ** 2)
                    s4 = round(s3 / s2, 3)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(s4)
                if run == 'z2':
                    z = [
                        'Какова вероятность того, что капля из протёкшей крыши попадет на стол, находящийся в комнате? Ширина комнаты – ',
                        ' м, длина комнаты – ', ' м, ширина стола – ', ' см, длина стола – ', 'cм.']
                    a = random.randint(2, 10)
                    b = random.randint(2, 10)
                    c = random.randint(20, 70)
                    d = random.randint(100, 300)
                    s2 = (c * d) / 10000
                    s3 = a * b
                    s4 = round(s2 / s3, 3)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + ' Ответ: ' + str(s4)
                if run == 'z3':
                    z = ['На дороге которая имеет длину ', ' км, на ', ' км находится автомобильный сервис, а на ',
                         ' км – закусочная. Какова вероятность того, что при поломке автомобиля, сервис окажется ближе нежели закусочная?']
                    a = random.randint(50, 100)
                    b = random.randint(10, a)
                    c = random.randint(b, a)

                    s2 = (c - b) / 2
                    s3 = b + s2
                    s4 = round(s3 / a, 3)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(s4)
            if tem == 'slozh-umn-ver':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    def probOfWinning(attempt):
                        return 0.5 ** (2 * attempt - 1)
                    P, n = 0, 1
                    while (n < k):
                        P += probOfWinning(n)
                        n += 1
                    problemCondition = f"""Два игрока A и B поочередно бросают монету. Выигравшим считается тот, у кого раньше выпадет герб. Первый бросок 
                    делает игрок A, второй – B, третий – A и т.д. Найти вероятность того, что A выиграл до {k} броска. Ответ округлить до 3 знака после запятой."""
                    ans = f" Ответ: {np.round(P, decimals=3)}"
                    s1 = problemCondition + ans
                if run == 'z2':
                    numOfAuditors = np.random.randint(10, 21)  # общее число аудиторов
                    qualifiedAuditors = np.random.randint(1, numOfAuditors + 1)  # число квалифицированных аудиторов
                    numOfProgrammers = np.random.randint(15, 26)  # общее число программистов
                    qualifiedProgrammers = np.random.randint(1,numOfProgrammers + 1)  # число квалифицированных программистов
                    auditorsGroup = np.random.randint(1, 6)  # необходимое количество аудиторов в группе
                    programmersGroup = np.random.randint(1, 5)  # необходимое количество программистов в группе
                    minimumAuditorsQualified = np.random.randint(1, 4)  # минимальное число квалифицированных аудиторов
                    minimumProgrammersQualified = np.random.randint(1,3)  # минимальное число квалифицированных программистов
                    if minimumAuditorsQualified > qualifiedAuditors:
                        minimumAuditorsQualified = qualifiedAuditors
                    if minimumProgrammersQualified > qualifiedProgrammers:
                        minimumProgrammersQualified = qualifiedProgrammers
                    def probabilityCalc():  # Вычисление вероятности
                        auditorsNeeded, auditorsNotHighQualified = [
                            comb(numOfAuditors, auditorsGroup),
                            comb(numOfAuditors - qualifiedAuditors, auditorsGroup)
                        ]
                        programmersNeeded, programmersNotHighQualified = [
                            comb(numOfProgrammers, programmersGroup),
                            comb(numOfAuditors - qualifiedProgrammers, programmersGroup)
                        ]
                        PnotA, PnotB = [
                            auditorsNotHighQualified / auditorsNeeded,
                            programmersNotHighQualified / programmersNeeded,
                        ]
                        pA, pB = [
                            1 - PnotA,
                            1 - PnotB
                        ]
                        return pA * pB
                    problemCondition = f"""В фирме работают {numOfAuditors} аудиторов, из которых {qualifiedAuditors} – высокой квалификации, 
                    и {numOfProgrammers} программистов, из которых {qualifiedProgrammers} высокой квалификации. В командировку надо отправить группу 
                    из {auditorsGroup} аудитор(-ов) и {programmersGroup} программист(-ов). Какова вероятность того, что в этой группе окажется по крайней 
                    мере {minimumAuditorsQualified} аудитор(-ов) высокой квалификации и хотя бы {minimumProgrammersQualified} программист(-ов) высокой 
                    квалификации, если набор группы проводился анонимным анкетированием и каждый специалист имел равные возможности поехать в командировку?"""
                    ans = f' Ответ: {np.round(probabilityCalc(), decimals=2)}'
                    s1 = problemCondition + ans
                if run == 'z3':
                    # Введем события
                    # А1 = (газеты доставлены своевременно в первое отделение),
                    # А2 = (газеты доставлены своевременно во второе отделение),
                    # А3 = (газеты доставлены своевременно в третье отделение),
                    PA1, PA2, PA3 = [
                        np.round(np.random.uniform(0.8, 0.96), decimals=2),
                        np.round(np.random.uniform(0.75, 0.94), decimals=2),
                        np.round(np.random.uniform(0.7, 0.86), decimals=2)
                    ]
                    # Найдем вероятность события Х = (только одно отделение получит газеты вовремя).
                    # Событие Х произойдет, если:
                    # или газеты доставлены своевременно в 1 отделение, и доставлены не вовремя во 2 и 3,
                    # или газеты доставлены своевременно в 2 отделение, и доставлены не вовремя во 1 и 3,
                    # или газеты доставлены своевременно в 3 отделение, и доставлены не вовремя во 1 и 2.
                    # Таким образом, X = A1*notA2*notA3 + A2*notA1*notA3 + A3*notA1*notA2
                    PnotA1, PnotA2, PnotA3 = [
                        1 - PA1,
                        1 - PA2,
                        1 - PA3
                    ]
                    ansA = f' Ответ: {np.round(PA1 * PnotA2 * PnotA3 + PA2 * PnotA1 * PnotA3 + PA3 * PnotA1 * PnotA2, decimals=2)}'
                    # Найдем вероятность события Y =(хотя бы одно отделение получит газеты с опозданием).
                    # Введем противоположное событие Y = (все отделения получат газеты вовремя).
                    PnotY = PA1 * PA2 * PA3
                    ansB = f' {np.round(1 - PnotY, decimals=2)}'
                    problemCondition = f"""Экспедиция издательства отправила газеты в три почтовых отделения. Вероятность своевременной доставки газет 
                    в первое отделение равна {PA1}, во второе - {PA2}, в третье - {PA3}. Найти вероятность следующих событий: а) только одно отделение получит 
                    газеты вовремя; б) хотя бы одно отделение получит газеты с опозданием."""
                    s1 = problemCondition + ansA + ansB
            if tem == 'fpv':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Сотрудники отдела маркетинга полагают, что в ближайшее время ожидается рост спроса на продукцию фирмы. Вероятность этого они оценивают в ',
                        '%. Консультационная фирма, занимающаяся прогнозом рыночной ситуации, подтвердила предположение о росте спроса. Положительные прогнозы '
                        'консультационной фирмы сбываются с вероятностью ',
                        '%, а отрицательные – с вероятностью ',
                        '%. Какова вероятность того, что рост спроса действительно произойдет?']
                    a = random.randint(70, 90)
                    b = random.randint(70, 90)
                    c = random.randint(70, 90)
                    n = a / 100
                    m = b / 100
                    k = c / 100
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(round(n * m + (1 - n) * k, 3))
                if run == 'z2':
                    z = ['В группе спортсменов лыжников в 2 раза больше, чем бегунов, а бегунов в 3 раза больше, чем велосипедистов. Вероятность выполнить норму для лыжника ',
                        '%, для бегуна ', '%, для велосипедиста - ',
                        '%. Найти вероятность того, что спортсмен, выбранный наугад, выполнит норму.']
                    a = random.randint(70, 90)
                    b = random.randint(70, 90)
                    c = random.randint(70, 90)
                    n = a / 100
                    m = b / 100
                    k = c / 100
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(round(0.6 * n + 0.1 * k + 0.3 * m, 3))
                if run == 'z3':
                    z = [
                        'В ящике содержится n деталей, изготовленных на заводе №1, m деталей – на заводе №2 и k деталей – на заводе №3. Вероятность того, что деталь, изготовленная на заводе №1, отличного качества, равна ',
                        '%; для деталей, изготовленных на заводах №2 и №3, эти вероятности соответственно равны ',
                        '% и ',
                        '%. Найти вероятность того, что извлеченная наудачу деталь окажется отличного качества, где n = ',
                        ', m = ', ' и k = ', '.']
                    a = random.randint(60, 90)
                    b = random.randint(60, 90)
                    c = random.randint(60, 90)
                    n = random.randint(10, 30)
                    m = random.randint(10, 30)
                    k = random.randint(10, 30)
                    f = a / 100
                    g = b / 100
                    h = c / 100
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(n) + z[4] + str(m) + z[5] + str(k) + z[6] + ' Ответ: '\
                         + str(round((n / (n + m + k)) * f + (m / (n + m + k)) * g + (k / (n + m + k)) * h, 3))
            if tem == 'bayes':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Три цеха завода производят однотипные детали, которые поступают на сборку в общий контейнер. Известно, что первый цех производит изделий в n1 = ',
                        ' раз больше второго цеха и в n2 = ',
                        ' раз больше третьего цеха. В первом цехе брак составляет ', '%, во втором – ',
                        '%, в третьем – ',
                        '%. Для контроля из контейнера берется одно изделие. Какова вероятность того, что изделие окажется стандартным (без брака).']
                    n1 = random.randint(2, 5)
                    n2 = random.randint(2, 5)
                    b1 = random.randint(1, 15) / 100
                    b2 = random.randint(1, 15) / 100
                    b3 = random.randint(1, 15) / 100
                    x = 1 / (n2 + (n2 / n1) + 1)
                    p1 = n2 * x
                    p2 = (n2 / n1) * x
                    p3 = x
                    p1_ = (100 - (b1 * 100)) / 100
                    p2_ = (100 - (b2 * 100)) / 100
                    p3_ = (100 - (b3 * 100)) / 100
                    p = round(p1 * p1_ + p2 * p2_ + p3 * p3_, 3)
                    s1 = z[0] + str(n1) + z[1] + str(n2) + z[2] + str(int(b1 * 100)) + z[3] + str(int(b2 * 100)) + z[4] + str(int(b3 * 100)) + z[5] + ' Ответ: '\
                         + str(p)
                if run == 'z2':
                    z = ['Однотипные приборы выпускаются 3 заводами в отношении ', ':', ':',
                         ', причѐм вероятность брака для этих заводов соответственно равны ', '; ', '; ',
                         '. Приобретѐнный прибор оказался бракованным. Какова вероятность того, что он изготовлен 3-м заводом.']
                    h1 = random.randint(1, 9)
                    h2 = random.randint(1, 9)
                    h3 = random.randint(1, 9)
                    b1 = random.randint(1, 15) / 100
                    b2 = random.randint(1, 15) / 100
                    b3 = random.randint(1, 15) / 100
                    p1 = h1 / (h1 + h2 + h3)
                    p2 = h2 / (h1 + h2 + h3)
                    p3 = h3 / (h1 + h2 + h3)
                    p = p1 * b1 + p2 * b2 + p3 * b3
                    p3_ = round((p3 * b3) / p, 3)
                    s1 = z[0] + str(h1) + z[1] + str(h2) + z[2] + str(h3) + z[3] + str(b1) + z[4] + str(b2) + z[5] + str(b3) + z[6] + ' Ответ: ' + str(p3_)
                if run == 'z3':
                    z = [
                        'Компания по страхованию автомобилей разделяет водителей по трѐм классам: класс А (мало рискует), класс В (рискует средне), класс С '
                        '(рискует сильно). Компания предполагает, что из всех водителей, застрахованных у неѐ, ',
                        '% принадлежат классу А, ', '% – классу В, ',
                        '% – классу С. Вероятность того, что в течение года водитель класса А попадѐт хотя бы в одну автокатастрофу, равна ',
                        '; для водителя класса В эта вероятность равна ', ', а для водителя класса С – ',
                        '. Мистер Джонс страхует свою машину у этой компании и в течение года попадает в автокатастрофу. Какова вероятность того, что он '
                        'относится к классу А?']
                    a = random.randint(2, 4) / 10
                    b = random.randint(3, 5) / 10
                    c = (100 - (a * 100 + b * 100)) / 100
                    p1 = random.randint(5, 8) / 100
                    p2 = random.randint(4, 6) / 100
                    p3 = random.randint(1, 5) / 100
                    p = p1 * a + p2 * b + p3 * c
                    pa_ = round((p1 * a) / p, 3)
                    s1 = z[0] + str(int(a * 100)) + z[1] + str(int(b * 100)) + z[2] + str(int(c * 100)) + z[3] + str(p1) + z[4] + str(p2) + z[5] + str(p3) + z[6] + ' Ответ: ' + str(pa_)
            if tem == 'bern':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Статистика аудиторских проверок компании утверждает, что вероятность обнаружения ошибки в каждом проверяемом документе равна ',
                        '. Какова вероятность, что из ', ' проверяемых документов ',
                        ' из них не будет содержать ошибки?']
                    a = random.randint(1, 9)
                    b = random.randint(8, 10)  # n
                    c = random.randint(1, b - 1)  # m
                    f1 = 1
                    f2 = 1
                    f3 = 1
                    n = b
                    m = c
                    w = b - c
                    s2 = a / 10  # q
                    s3 = 1 - s2  # p
                    while n > 1:
                        f1 = f1 * n
                        n = n - 1
                    while m > 1:
                        f2 = f2 * m
                        m = m - 1
                    while w > 1:
                        f3 = f3 * w
                        w = w - 1
                    s4 = f1 / (f2 * f3)
                    s5 = (s3) ** c
                    s6 = (s2) ** (b - c)
                    s7 = s4 * s5 * s6
                    while (int(s7 * 1000) == 0):
                        a = random.randint(1, 9)
                        b = random.randint(8, 10)  # n
                        c = random.randint(1, b - 1)  # m
                        f1 = 1
                        f2 = 1
                        f3 = 1
                        n = b
                        m = c
                        w = b - c
                        s2 = a / 10  # q
                        s3 = 1 - s2  # p
                        while n > 1:
                            f1 = f1 * n
                            n = n - 1
                        while m > 1:
                            f2 = f2 * m
                            m = m - 1
                        while w > 1:
                            f3 = f3 * w
                            w = w - 1
                        s4 = f1 / (f2 * f3)
                        s5 = (s3) ** c
                        s6 = (s2) ** (b - c)
                        s7 = s4 * s5 * s6
                    s1 = z[0] + str(s2) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(round(s7, 3))
                if run == 'z2':
                    z = ['В телеателье имеется ',
                         ' телевизоров. Для каждого телевизора вероятность того, что в данный момент он включен равна 0.',
                         ' .Найти вероятность, что в данный момент хотя бы один телевизор включен.']
                    a = random.randint(5, 10)  # n
                    b = random.randint(1, 9)
                    s2 = b / 10  # p
                    s3 = 1 - s2  # q
                    s4 = s3 ** a
                    s5 = 1 - s4
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + ' Ответ: ' + str(round(s5, 3))
                if run == 'z3':
                    z = ['В результате обследования были выделены семьи, имеющие по ', ' ребенка. Считая вероятности появления мальчика и девочки в семье '
                    'равными, определить вероятности появления в ней: а) ',' мальчика, б) ', ' девочек.']
                    a = random.randint(5, 6)
                    b = random.randint(1, 4)
                    c = random.randint(1, 4)
                    d = a - b
                    w = a - c
                    f1 = 1
                    f2 = 1
                    f3 = 1
                    f4 = 1
                    f5 = 1
                    s = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3]
                    p = 0.5
                    while a > 1:
                        f1 = f1 * a
                        a = a - 1
                    while b > 1:
                        f2 = f2 * b
                        b = b - 1
                    while c > 1:
                        f3 = f3 * c
                        c = c - 1
                    while d > 1:
                        f4 = f4 * d
                        d = d - 1
                    while w > 1:
                        f5 = f5 * w
                        w = w - 1
                    k2 = f1 / (f2 * f4)
                    s2 = k2 * 0.5 ** a
                    k3 = f1 / (f3 * f5)
                    s3 = k3 * 0.5 ** a
                    s1 = s + ' Ответ: ' + str(s2) + ' ' + str(s3)
            if tem == 'naiv':
                run = random.choice(['z1', 'z2', 'z3'])
                if run=='z1':
                    n = random.randint(5, 20)
                    p = random.randint(1, 9) / 10
                    s1 = 'Испытывается каждый из ' + str(n) + ' элементов некоторого устройства. Вероятность того, что элемент выдержит испытание, равна ' + str(
                        p) + '. Найти наивероятнейшее(ие) число(а) элементов, которые выдержат испытание. Ответ: '
                    q = 1 - p
                    ch = n * p - q
                    if (ch > 10):
                        if (ch % 10 != 0):
                            cel = False  # целостность числа
                            res = 1
                        else:
                            cel = True
                            res = 2
                    else:
                        if ((ch * 10) % 10 != 0):
                            cel = False
                            res = 1
                        else:
                            cel = True
                            res = 2

                    ch1 = n * p + p
                    res2 = (ch + 1) // 1
                    if (res == 2):
                        s1 = s1 + str(int(res2)) + ' ' + str(int(res2 + 1))
                    else:
                        s1 = s1 + str(int(res2))
                if run=='z2':
                    n = random.randint(5, 20)
                    p = random.randint(1, 9) / 10
                    s1 = 'Доля изделий высшего сорта на предприятии составляет ' + str(
                        int(p * 100)) + '%. Чему равно наивероятнейшее(ие) число(а) изделий высшего сорта в случайно отобранной партии из ' + str(
                        n) + ' изделий? Ответ: '
                    q = 1 - p
                    ch = n * p - q
                    if (ch > 10):
                        if (ch % 10 != 0):
                            cel = False  # целостность числа
                            res = 1
                        else:
                            cel = True
                            res = 2
                    else:
                        if ((ch * 10) % 10 != 0):
                            cel = False
                            res = 1
                        else:
                            cel = True
                            res = 2

                    ch1 = n * p + p
                    res2 = (ch + 1) // 1
                    if (res == 2):
                        s1 += str(int(res2)) + ' ' + str(int(res2 + 1))
                    else:
                        s1 += str(int(res2))
                if run=='z3':
                    n = random.randint(5, 20)
                    p = random.randint(1, 9) / 10
                    s1 = 'В результате многолетних наблюдений для некоторой местности было установлено, что вероятность выпадения дождя 3 сентября равна ' + str(
                        p) + '. Наивероятнейшее число дождей, выпавших 3-го сентября в ближайшие ' + str(
                        n) + ' лет равно? '
                    q = 1 - p
                    ch = n * p - q
                    if (ch > 10):
                        if (ch % 10 != 0):
                            cel = False  # целостность числа
                            res = 1
                        else:
                            cel = True
                            res = 2
                    else:
                        if ((ch * 10) % 10 != 0):
                            cel = False
                            res = 1
                        else:
                            cel = True
                            res = 2

                    ch1 = n * p + p
                    res2 = (ch + 1) // 1
                    if (res == 2):
                        s1 += str(int(res2)) + ' ' + str(int(res2 + 1))
                    else:
                        s1 += str(int(res2))
            if tem == 'muavr-laplas':
                s1 = 'Задачи отсутствуют'
            if tem == 'int-muavr-laplas':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Вероятность изготовления годной детали равна ', '. Произведено n = ',
                         ' деталей. Найти вероятность получения годных деталей: а) менее ', '; б) от ', ' до ', '?']
                    p_g = random.randint(5, 9) / 10
                    n = random.randint(200, 1000)
                    pa = random.randint(90, n // 2)
                    pb1 = random.randint(pa, pa + 100)
                    pb2 = random.randint(pb1 + 50, pb1 + 100)
                    q = 1 - p_g
                    a1 = round((pa - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                    a2 = round((0 - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                    fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                    b1 = round((pb2 - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                    b2 = round((pb1 - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                    fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                    while (int(fa * 100) == 0 or int(fb * 100) == 0):
                        p_g = random.randint(5, 9) / 10
                        n = random.randint(200, 1000)
                        pa = random.randint(90, n // 2)
                        pb1 = random.randint(pa, pa + 100)
                        pb2 = random.randint(pb1 + 50, pb1 + 100)
                        q = 1 - p_g
                        a1 = round((pa - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                        a2 = round((0 - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                        fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                        b1 = round((pb2 - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                        b2 = round((pb1 - n * p_g) / ((n * p_g * q) ** (0.5)), 2)
                        fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                    s1 = z[0] + str(p_g) + z[1] + str(n) + z[2] + str(pa) + z[3] + str(pb1) + z[4] + str(pb2) + z[5] + ' Ответ: ' + str(round(fa, 3)) + ' ' + str(round(fb, 3))
                if run == 'z2':
                    z = [
                        'Стоматологическая клиника распространяет рекламные листовки у входа в метро. Опыт показывает, что в одном случае из тысячи следует обращение в клинику. Найти вероятность того, что при распространении ',
                        ' тыс. листков число обращений будет: а) менее ', ', б) находиться в границах от ', ' до ',
                        '.']
                    p = 1 / 1000
                    q = 1 - p
                    n = random.randint(20, 90) * 1000
                    m = random.randint(40, 100)
                    m1 = m
                    m2 = random.randint(m1 + 20, m1 + 80)
                    a1 = (m - n * p) / ((n * p * q) ** (0.5))
                    a2 = (0 - n * p) / ((n * p * q) ** (0.5))
                    fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                    b1 = (m2 - n * p) / ((n * p * q) ** (0.5))
                    b2 = (m1 - n * p) / ((n * p * q) ** (0.5))
                    fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                    while (int(fa * 100) == 0 or int(fb * 100) == 0):
                        p = 1 / 1000
                        q = 1 - p
                        n = random.randint(20, 90) * 1000
                        m = random.randint(40, 100)
                        m1 = m
                        m2 = random.randint(m1 + 20, m1 + 80)
                        a1 = (m - n * p) / ((n * p * q) ** (0.5))
                        a2 = (0 - n * p) / ((n * p * q) ** (0.5))
                        fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                        b1 = (m2 - n * p) / ((n * p * q) ** (0.5))
                        b2 = (m1 - n * p) / ((n * p * q) ** (0.5))
                        fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                    s1 = z[0] + str(int(n / 1000)) + z[1] + str(m) + z[2] + str(m1) + z[3] + str(m2) + z[4] + ' Ответ: ' + str(round(fa, 3)) + ' ' + str(round(fb, 3))
                if run == 'z3':
                    z = ['В среднем ',
                         '% студентов первого курса продолжают дальнейшее обучение. Какова вероятность, что из ',
                         ' студентов первого курса перейдут на второй курс: a) от ', ' до ', ' человек?, б) более ',
                         ' человек?']
                    p = random.randint(6, 9) / 10
                    q = 1 - p
                    n = random.randint(700, 1500)
                    m1 = random.randint(n - 300, n - 200)
                    m2 = random.randint(m1, m1 + 100)
                    m = m1
                    b1 = (m2 - n * p) / ((n * p * q) ** (0.5))
                    b2 = (m1 - n * p) / ((n * p * q) ** (0.5))
                    fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                    a1 = (n - n * p) / ((n * p * q) ** (0.5))
                    a2 = (m - n * p) / ((n * p * q) ** (0.5))
                    fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                    while (int(fa * 100) == 0 or int(fb * 100) == 0):
                        p = random.randint(6, 9) / 10
                        q = 1 - p
                        n = random.randint(700, 1500)
                        m1 = random.randint(n - 300, n - 200)
                        m2 = random.randint(m1, m1 + 100)
                        m = m1
                        b1 = (m2 - n * p) / ((n * p * q) ** (0.5))
                        b2 = (m1 - n * p) / ((n * p * q) ** (0.5))
                        fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                        a1 = (n - n * p) / ((n * p * q) ** (0.5))
                        a2 = (m - n * p) / ((n * p * q) ** (0.5))
                        fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                    s1 = z[0] + str(int(p * 100)) + z[1] + str(n) + z[2] + str(m1) + z[3] + str(m2) + z[4] + str(m) + z[5] + ' Ответ: ' + str(round(fb, 3)) + ' ' + str(round(fa, 3))
            if tem == 'puass':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Звонки в диспетчерскую такси представляет собой поток со средней интенсивностью ',
                         ' вызовов в час. Найти вероятность того, что в течение ', ' минут будет хотя бы один звонок.']
                    m = random.randint(20, 100)
                    k = random.randint(2, 5)
                    v = (m / 60) * k
                    pys0 = round(((v ** 0) / factorial(0)) * exp(-v), 3)
                    pys = round(1 - pys0, 3)
                    s1 = z[0] + str(m) + z[1] + str(k) + z[2] + ' Ответ: ' + str(pys)
                if run == 'z2':
                    z = ['Среднее число самолетов, взлетающих с полевого аэродрома за одни сутки, равно ',
                         '. Найти вероятность того, что за ', ' часов взлетят не менее двух самолетов.']
                    n = random.randint(5, 20)
                    t = random.randint(2, 12)
                    while (24 % t != 0):
                        t = random.randint(2, 12)
                    k = t / 24
                    v = n * k
                    pys0 = round(((v ** 0) / factorial(0)) * exp(-v), 5)
                    pys1 = round(((v ** 1) / factorial(1)) * exp(-v), 5)
                    pys = round(1 - pys1 - pys0, 3)
                    s1 = z[0] + str(n) + z[1] + str(t) + z[2] + ' Ответ: ' + str(pys)
                if run =='z3':
                    z = ['Производственный брак составляет ', '%. Определить вероятность того, что в партии из ',
                         ' деталей будет не более двух.']
                    j = round(random.uniform(0.1, 0.5), 1)
                    n = random.randint(100, 900)
                    while (n % 100 != 0):
                        n = random.randint(100, 900)
                    p = j / 100
                    v = n * p
                    pys0 = round(((v ** 0) / factorial(0)) * exp(-v), 5)
                    pys1 = round(((v ** 1) / factorial(1)) * exp(-v), 5)
                    pys2 = round(((v ** 2) / factorial(2)) * exp(-v), 5)
                    pys = round(pys2 + pys1 + pys0, 3)
                    s1 = z[0] + str(j) + z[1] + str(n) + z[2] + ' Ответ: ' + str(pys)
            if tem == 'diskr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['Вероятность попадания в цель при одном выстреле равна ',
                         ' и уменьшается с каждым выстрелом на ',
                         '. Найти математическое ожидание, дисперсию и С.К.О. попадания в цель, если было сделано 3 выстрела']
                    a = random.randint(60, 90)
                    b = random.randint(5, 20)
                    f = a / 100
                    g = b / 100
                    h = f - g
                    j = h - g
                    c = 1 - f
                    d = 1 - h
                    e = 1 - j
                    s1 = z[0] + str(f) + z[1] + str(g) + z[2] + ' Ответ: ' + str(round((0 * c * d * e) + (1 * (f * d * e + c * h * e + c * d * j)) +
                    (2 * (c * h * j + f * d * j + f * h * e)) + (3 * f * h * j), 3)) + ' ' + str(round((0 * c * d * e) + (1 * (f * d * e + c * h * e + c * d * j)) +
                    (4 * (c * h * j + f * d * j + f * h * e)) + (9 * f * h * j) - ((0 * c * d * e) + (1 * (f * d * e + c * h * e + c * d * j)) + (2 * (c * h * j +
                    f * d * j + f * h * e)) + (3 * f * h * j)) ** 2,3)) + ' ' + str(round(((0 * c * d * e) + (1 * (f * d * e + c * h * e + c * d * j)) + (2 * (c *
                    h * j + f * d * j + f * h * e)) + (3 * f * h * j)) ** (1 / 2), 3))
                if run == 'z2':
                    z = [
                        'На переэкзаменовку по теории вероятностей явились 3 студента. Вероятность того, что первый сдаст экзамен, равна ',
                        ', второй - ', ', третий - ',
                        '. Вычислить математическое ожидание, дисперсию числа студентов, сдавших экзамен.']
                    m = random.randint(50, 90)
                    n = random.randint(50, 90)
                    k = random.randint(50, 90)
                    a = m / 100
                    b = n / 100
                    c = k / 100
                    d = 1 - a
                    e = 1 - b
                    f = 1 - c
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + ' Ответ: ' + str(round(0 * (d * e * f) + 1 * (a * e * f + d * b * f + d * e * c) + 2 *
                    (a * b * f + a * e * c + d * b * c) + 3 * (a * b * c), 3)) + ' ' + str(round((0 * (d * e * f) + 1 * (a * e * f + d * b * f + d * e * c) + 4 *
                    (a * b * f + a * e * c + d * b * c) + 9 * (a * b * c)) - (0 * (d * e * f) + 1 * (a * e * f + d * b * f + d * e * c) + 2 * (a * b * f + a * e *
                    c + d * b * c) + 3 * (a * b * c)) ** 2,3))
                if run == 'z3':
                    z = [
                        'В ящике содержится m стандартных и n бракованных детали. Вынимают детали последовательно до появления стандартной, не возвращая их обратно. '
                        'Случайной дискретной величиной является число извлеченных бракованных детелей. Вычислить математическое ожидание, дисперсию, среднее квадратическое'
                        ' отклонение. m=',
                        ', n=', '.']
                    m = random.randint(2, 9)
                    n = 10 - m
                    s1 = z[0] + str(m) + z[1] + str(n) + z[2] + ' Ответ: ' + str(round(0 * (m / 10) + 1 * (n / 10) * (m / 9) + 2 * (n / 10) * ((n - 1) / 9) *
                    (m / 8) + 3 * (n / 10) * ((n - 1) / 9) * ((n - 2) / 8) * (m / 7), 3)) + ' ' + str(round((0 * (m / 10) + 1 * (n / 10) * (m / 9) + 4 * (n / 10) *
                    ((n - 1) / 9) * (m / 8) + 9 * (n / 10) * ((n - 1) / 9) * ((n - 2) / 8) * (m / 7)) - (0 * (m / 10) + 1 * (n / 10) * (m / 9) + 2 * (n / 10) *
                    ((n - 1) / 9) * (m / 8) + 3 * (n / 10) * ((n - 1) / 9) * ((n - 2) / 8) * (m / 7)) ** 2,3)) + ' ' + str(round(((0 * (m / 10) + 1 *
                    (n / 10) * (m / 9) + 4 * (n / 10) * ((n - 1) / 9) * (m / 8) + 9 * (n / 10) * ((n - 1) / 9) * ((n - 2) / 8) * (m / 7)) - (0 * (m / 10) + 1 *
                    (n / 10) * (m / 9) + 2 * (n / 10) * ((n - 1) / 9) * (m / 8) + 3 * (n / 10) * ((n - 1) / 9) * ((n - 2) / 8) * (m / 7)) ** 2) ** (1 / 2), 3))
            if tem == 'nepr':
                run = random.choice(['z1', 'z2', 'z3'])
                if (run == 'z1' or run == 'z2'):
                    s1 = 'Задачи отсутствуют'
                if run == 'z3':
                    z = [
                        'Время в годах безотказной работы прибора подчинено показательному закону, т.е. плотность распределения этой случайной величины такова: f(t)=',
                        'e^(-',
                        't) при t>=0 и f(t)=0 при t<0. Определить вероятность того, что прибор проработает не более года. Определить вероятность того, что прибор '
                        'безотказно проработает 3 года. Определить среднее ожидаемое время безотказной работы прибора ']
                    a = random.randint(1, 5)
                    b = math.e
                    s1 = z[0] + str(a) + z[1] + str(a) + z[2] + ' Ответ: ' + str(round(b ** (0) - b ** ((-a) * 1), 3)) + ' ' + str(round(1 - (b ** (0) - b ** ((-a) *
                    3)), 3)) + ' ' + str(round(1 / a, 3))
            if tem == 'norm':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    str1 = 'Из пункта  ведётся стрельба из орудия вдоль прямой. Предполагается, что дальность полёта распределена нормально с математическим ожиданием '
                    str2 = 'м и средним квадратическим отклонением '
                    str3 = 'Определить (в процентах) сколько снарядов упадёт с перелётом от '
                    a = random.randint(9, 13) * 1000
                    q = random.randint(4, 8)
                    a1 = random.randint(1, 10)
                    b1 = random.randint(5, 10) * 10
                    A = a + a1
                    B = a + b1
                    F = scipy.stats.norm.cdf((B - a) / q) - scipy.stats.norm.cdf((A - a) / q)
                    s1 = str1 + str(a) + str2 + str(q) + 'м. ' + str3 + str(a1) + ' до ' + str(
                        b1) + 'м.' + ' Ответ: ' + str(round(F * 100, 3))
                if run == 'z2':
                    str1 = 'Станок изготовляет шарики для подшипников. Шарик считается годным, если отклонение X диаметра шарика от проектного размера по абсолютной ' \
                           'величине меньше '
                    str2 = ' мм. Считая, что случайная величина X распределена нормально со средним квадратическим отклонением σ =  '
                    str3 = ' мм, найти, сколько в среднем будет годных шариков среди ста изготовленных.'
                    a = random.randint(1, 10) / 10
                    q = random.randint(10, 90) / 100
                    # a1=1.4#random.randint(10,19)/10
                    # b1=1.6#random.randint(int(a1*10+1),20)/10
                    BILL = 2 * (scipy.stats.norm.cdf(a / q)) - 1
                    # F=scipy.stats.norm.cdf((B-a)/q)-scipy.stats.norm.cdf((A-a)/q)
                    s1 = str1 + str(a) + str2 + str(q) + str3 + ' Ответ: ' + str(round(BILL * 100, 3))
                if run == 'z3':
                    str1 = 'Дневная добыча угля в некоторой шахте распределена по нормальному закону с математическим ожиданием '
                    str2 = ' тонн и стандартным отклонением '
                    str3 = 'Найдите вероятность того, что в определенный день будут добыты по крайней мере '
                    a = random.randint(90, 100) * 10
                    q = random.randint(20, 40) * 10
                    Big = random.randint(101, 110) * 10
                    F = 1 - scipy.stats.norm.cdf((Big - a) / q)
                    s1 = str1 + str(a) + str2 + str(q) + ' тонн. ' + str3 + str(Big) + ' тонн угля.' + ' Ответ: ' + str(round(F, 3))
            vop = int(request.GET.get('numbervop'))
            Task.objects.filter(nomer=vop).delete()
            Task(zadacha=s1, nomer=vop).save()
            return render(request, 'app/vibor.html', {'task': s1, 'nametem': tem, 'slozh': sl, 'numbervop': vop, 'numbers': numbers})
        if sl == 'ur3':
            if tem == 'klasopr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['В ящике находится ', ' качественных и ', ' бракованных деталей. Наудачу извлекаются ',
                         ' детали. Найти вероятность того, что все детали будут качественными.']
                    p = random.randint(10, 50)
                    h = random.randint(1, 10)
                    c = random.randint(2, 3)
                    while (h >= (p / 3)):
                        h = random.randint(1, 10)
                    n = p + h
                    q = factorial(n) / (factorial(n - c) * factorial(c))
                    w = factorial(p) / (factorial(p - c) * factorial(c))
                    f = round(w / q, 3)
                    s1 = z[0] + str(p) + z[1] + str(h) + z[2] + str(c) + z[3] + ' Ответ: ' + str(f)
                if run == 'z2':
                    z = ['В ящике находится ', ' качественных и ', ' бракованных деталей. Наудачу извлекаются ',
                         ' детали. Найти вероятность того, что все детали будут бракованные.']
                    p = random.randint(10, 50)
                    h = random.randint(1, 10)
                    c = random.randint(2, 3)
                    while ((h >= (p / 3)) or (h <= c)):
                        h = random.randint(1, 10)
                    n = p + h
                    print(h, c)
                    q = factorial(n) / (factorial(n - c) * factorial(c))
                    w = factorial(h) / (factorial(h - c) * factorial(c))
                    f = round(w / q, 3)
                    while (int(f * 1000) == 0):
                        p = random.randint(10, 50)
                        h = random.randint(1, 10)
                        c = random.randint(2, 3)
                        while ((h >= (p / 3)) or (h <= c)):
                            h = random.randint(1, 10)
                        n = p + h
                        print(h, c)
                        q = factorial(n) / (factorial(n - c) * factorial(c))
                        w = factorial(h) / (factorial(h - c) * factorial(c))
                        f = round(w / q, 3)
                    s1 = z[0] + str(p) + z[1] + str(h) + z[2] + str(c) + z[3] + ' Ответ: ' + str(f)
                if run == 'z3':
                    z = ['В ящике находится ', ' качественных и ', ' бракованных деталей. Наудачу извлекаются ',
                         ' детали. Найти вероятность того, что ', ' детали будут качественные и ', ' бракованные.']
                    p = random.randint(10, 50)
                    h = random.randint(1, 10)
                    c = random.randint(2, 3)
                    m = random.randint(1, 2)
                    while (m >= c):
                        m = random.randint(1, 2)
                    c1 = c - m
                    c2 = c - c1
                    while (h >= (p / 3) or (h <= c2)):
                        h = random.randint(1, 10)
                    n = p + h
                    v1 = factorial(p) / (factorial(p - c1) * factorial(c1))
                    v2 = factorial(h) / (factorial(h - c2) * factorial(c2))
                    v = v1 * v2

                    q = factorial(n) / (factorial(n - c) * factorial(c))

                    f = round(v / q, 3)
                    s1 = z[0] + str(p) + z[1] + str(h) + z[2] + str(c) + z[3] + str(c1) + z[4] + str(c2) + z[5] + ' Ответ: ' + str(f)
            if tem == 'deistviya-nad-sob':
                s1 = 'Задачи отсутствуют'
            if tem == 'geom':
                s1 = 'Задачи отсутствуют'
            if tem == 'slozh-umn-ver':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Устройство состоит из четырех элементов, работающих независимо. Вероятности безотказной работы в течение месяца соответственно равны: ',
                        ' для первого элемента; ', ' для второго; ', ' для третьего и ',
                        ' для четвертого. Найти вероятность того, что в течение месяца будут безотказно работать: а) все 4 элемента; б) только один элемент; в) не менее двух элементов.']
                    p1 = random.randint(2, 9) / 10
                    p2 = random.randint(2, 9) / 10
                    p3 = random.randint(2, 9) / 10
                    p4 = random.randint(2, 9) / 10
                    q1 = 1 - p1
                    q2 = 1 - p2
                    q3 = 1 - p3
                    q4 = 1 - p4

                    a = p1 * p2 * p3 * p4
                    b = p1 * q2 * q3 * q4 + q1 * p2 * q3 * q4 + q1 * q2 * p3 * q4 + q1 * q2 * q3 * p4
                    c = 1 - (b + q1 * q2 * q3 * q4)
                    s1 = z[0] + str(p1) + z[1] + str(p2) + z[2] + str(p3) + z[3] + str(p4) + z[4] + ' Ответ: ' + str(round(a, 3)) + ' ' + \
                         str(round(b, 3)) + ' ' + str(round(c, 3))
                if run == 'z2':
                    z = [
                        'Стрелок произвел четыре выстрела по удаляющейся от него цели, причем вероятность попадания в цель в начале стрельбы равна ',
                        ', а после каждого выстрела уменьшается на ',
                        '. Вычислить вероятность того, что цель будет поражена: а) четыре раза; б) три раза; в) не менее трёх раз.']
                    e = random.randint(1, 10) / 100
                    p1 = random.randint(50, 90) / 100
                    p2 = p1 - e
                    p3 = p2 - e
                    p4 = p3 - e
                    q1 = 1 - p1
                    q2 = 1 - p2
                    q3 = 1 - p3
                    q4 = 1 - p4
                    a = p1 * p2 * p3 * p4
                    b = q1 * p2 * p3 * p4 + p1 * q2 * p3 * p4 + p1 * p2 * q3 * p4 + p1 * p2 * p3 * q4
                    c = a + b
                    s1 = z[0] + str(p1) + z[1] + str(e) + z[2] + ' Ответ: ' + str(round(a, 3)) + ' ' + str(round(b, 3)) + ' ' + str(round(c, 3))
                if run == 'z3':
                    z = ['В каждой из трех урн содержится k1 = ', ' черных и k2 = ',
                         ' белых шара. Из первой урны наудачу извлечен один шар и переложен во вторую урну, после чего из второй урны наудачу извлечен один шар и '
                         'переложен в третью урну. Найти вероятность того, что шар, наудачу извлеченный из третьей урны, окажется белым.']
                    b = random.randint(3, 20)
                    w = random.randint(3, 20)
                    pb = b / (b + w)
                    pw = w / (b + w)
                    p_1a = pb * ((b + 1) / (w + b + 1))
                    p_1b = pb * (w / (w + b + 1))
                    p_2a = pw * (b / (w + b + 1))
                    p_2b = pw * ((w + 1) / (w + b + 1))

                    p = p_1a * (w / (w + b + 1)) + p_1b * ((w + 1) / (w + b + 1)) + p_2a * (w / (w + b + 1)) + p_2b * (
                                (w + 1) / (w + b + 1))
                    s1 = z[0] + str(b) + z[1] + str(w) + z[2] + ' Ответ: ' + str(round(p, 3))
            if tem == 'fpv':
                run = random.choice(['z1', 'z2','z3'])
                if run == 'z1':
                    z = [
                        'В первой и в третьей группах одинаковое число студентов, а во второй – в 1,5 раза меньше, чем в первой. Количество отличников составляет ',
                        '% в первой,', '% во второй и ',
                        '% в третьей группе. Найти вероятность того, что случайно вызванный студент – отличник. Случайно вызванный студент оказался отличником. '
                        'Найти вероятность того, что студент учится в третьей группе.']
                    m = random.randint(3, 10)
                    n = random.randint(3, 10)
                    k = random.randint(3, 10)
                    a = m / 100
                    b = n / 100
                    c = k / 100
                    s1 = z[0] + str(m) + z[1] + str(n) + z[2] + str(k) + z[3] + ' Ответ: ' + str(round((3 / 8) * a + (1 / 4) * b + (3 / 8) * c, 3)) + ' ' +\
                         str(round((3 / 8) * c / ((3 / 8) * a + (1 / 4) * b + (3 / 8) * c), 3))
                if run == 'z2':
                    z = ['На склад поступило 2 партии изделий: первая – ', ' штук, вторая – ',
                         ' штук. Средний процент нестандартных изделий в первой партии составляет ',
                         '%, а во второй – ',
                         '%. Наудачу взятое со склада изделие оказалось стандартным. Найти вероятность того, что оно: а) из первой партии, б) из второй партии.']
                    k = random.randint(4, 7)
                    l = random.randint(3, 6)
                    m = random.randint(5, 20)
                    n = random.randint(5, 20)
                    a = k * 1000
                    b = l * 1000
                    c = m / 100
                    d = n / 100
                    pk = a / (a + b)
                    pl = b / (a + b)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(n) + z[3] + str(k) + z[4] + ' Ответ: ' + str(round(pk * c / (pk * c + pl * d), 3)) + \
                         ' ' + str(round(pl * d / (pk * c + pl * d), 3))
                if run == 'z3':
                    z = [
                        'Астрономический объект, за которым ведется наблюдение, может находиться в одном из двух состояний: Н1 или Н2. Априорные вероятности этих состояний P(Н1) = ',
                        ', Р (Н2) = ',
                        '. Наблюдение ведется независимо двумя обсерваториями. Первая обсерватория обычно дает правильные сведения о состоянии наблюдаемого объекта в ',
                        '% случаев, а в ', '% ошибается; вторая дает правильные сведения в ', '% случаев, а в ',
                        '% ошибается. Первая обсерватория сообщила, что объект находится в состоянии Н1, а вторая – что в состоянии Н2. Найти апостериорную вероятность состояния Н1. ']
                    m = random.randint(2, 8)
                    n = random.randint(70, 90)
                    k = random.randint(60, 90)
                    a = m / 10
                    b = 1 - a
                    c = n / 100
                    d = k / 100
                    l = 1 - c
                    o = 100 - n
                    p = 1 - d
                    g = 100 - k
                    s1 = z[0] + str(a) + z[1] + str(round(b,3)) + z[2] + str(n) + z[3] + str(o) + z[4] + str(k) + z[5] + str(g) + z[6] + ' Ответ: ' + str(round((a * c * p) /
                    (a * c * p + b * l * d), 3))
            if tem == 'bayes':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    H1 = random.randint(1, 9) / 10
                    H2 = 1 - H1
                    N1 = random.randint(1, 9) * 10
                    N2 = 100 - N1
                    N3 = random.randint(1, 9) * 10
                    if (N3 == N1) or (N3 == N2):
                        N3 = random.randint(1, 9) * 10

                    N4 = 100 - N3

                    txt1 = 'Астрономический объект, за которым ведется наблюдение, может находиться в одном из двух состояний: Н1 или Н2. ' \
                           'Априорные вероятности этих состояний P(Н1) = '
                    txt2 = ' Наблюдение ведется независимо двумя обсерваториями. Первая обсерватория обычно дает правильные сведения о состоянии ' \
                           'наблюдаемого объекта в '
                    txt3 = ' Первая обсерватория сообщила, что объект находится в состоянии Н1, а вторая – что в состоянии Н2. Найти апостериорную вероятность ' \
                           'состояния Н1. '
                    txt21 = ' вторая дает правильные сведения в '
                    s = txt1 + str(H1) + ', Р (Н2) = ' + str(H2) + txt2 + str(N1) + '% случаев, а в ' + str(
                        N2) + '% ошибается.' + txt21 + str(N3) + '% случаев, а в ' + str(N4) + '% ошибается.' + txt3

                    P1 = (N1 / 100) * (N4 / 100)
                    # print('P1 '+str(P1))
                    P2 = (N2 / 100) * (N3 / 100)
                    # print('P2 '+str(P2))
                    PP = H1 * P1 + H2 * P2
                    # print('PP '+str(PP))
                    PPP = (H1 * P1) / PP
                    s1 = s + 'Ответ: ' + str(round(PPP, 3))
                if run == 'z2':
                    H1 = random.randint(1, 4) * 10
                    # print('H1 '+str(H1))
                    H2 = random.randint(int(H1 / 10), 5) * 10
                    # print('H2 '+str(H2))
                    H3 = 100 - H1 - H2
                    # print('H3 '+str(H3))
                    N1 = random.randint(1, 10) / 100
                    # print('N1 '+str(N1))
                    N2 = random.randint(1, 10) / 100
                    # print('N2 '+str(N2))
                    N3 = random.randint(1, 10) / 100
                    # print('N3 '+str(N3))
                    txt1 = 'В учреждении три чиновника готовят копии документов. Первый чиновник обрабатывает '
                    txt2 = '%. У первого чиновника удельный вес ошибок составляет '
                    txt3 = '. В конце дня, выбрав случайно один из подготовленных документов, руководитель констатировал, что в нём есть ошибка (событие A). ' \
                           'Пользуясь формулой Байеса, выяснить, какова вероятность, что ошибку допустил первый чиновник, второй, третий.'
                    txt21 = ' вторая дает правильные сведения в '
                    s = txt1 + str(H1) + '% всех форм, второй - ' + str(H2) + '%, третий - ' + str(H3) + txt2 + str(
                        N1 / 100) + ', у второго – ' + str(N2) + ', у третьего – ' + str(N3) + txt3

                    P1 = ((H1 / 100) * N1)
                    P2 = ((H2 / 100) * N2)
                    P3 = ((H3 / 100) * N3)
                    P11 = (P1 / (P1 + P2 + P3))
                    P12 = (P2 / (P1 + P2 + P3))
                    P13 = (P3 / (P1 + P2 + P3))
                    s1 = s + ' Ответ: ' + str(round(P11, 3)) + ' ' + str(round(P12, 3)) + ' ' + str(round(P13, 3))
                if run == 'z3':
                    N1 = random.randint(1, 10) / 100
                    N2 = random.randint(1, 10) / 100
                    N3 = random.randint(1, 10) / 100
                    M1 = random.randint(1, 3)
                    M2 = random.randint(2, 4)

                    txt1 = 'На трех станках-автоматах обрабатываются однотипные детали, поступающие после обработки на общий конвейер. Первый станок дает '
                    txt2 = '. Производительность первого станка = '
                    txt21 = '. а) Каков процент брака на конвейере?'
                    txt22 = ' б) Каковы доли деталей каждого станка среди бракованных деталей на конвейере? '
                    s = txt1 + str(N1) + ' брака, второй – ' + str(N2) + ', третий – ' + str(N3) + txt2 + str(
                        M1) + 'x производительности второго, а производительность третьего = x/' + str(
                        M2) + txt21 + txt22
                    M2 = 1 / M2
                    P2 = 1 / (M1 + M2 + 1)
                    P1 = P2 * M1
                    P3 = P2 * M2
                    PA = P1 * N1 + P2 * N2 + P3 * N3
                    s1 = s + 'Ответ: а) ' + str(round(PA, 3))
                    PB1 = (P1 * N1 / PA)
                    PB2 = (P2 * N2 / PA)
                    PB3 = (P3 * N3 / PA)
                    s1 += ' б) в общей массе бракованных деталей на конвейере доля первого станка составляет - ' + str(round(PB1, 3)) + ', второго – ' +\
                          str(round(PB2, 3)) + ', третьего – ' + str(round(PB3, 3))

            if tem == 'bern':
                run = random.choice(['z1', 'z2','z3'])
                if run == 'z1':
                    z = ["В телеателье имеется ",
                         " телевизоров. Для каждого телевизора вероятность того, что в данный момент он включен, равна ",
                         ". Найти вероятность того, что в данный момент включены не менее ", " телевизоров."]
                    n = random.randint(5, 15)  # всего телевизоров
                    m0 = random.randint(3, 6)  # вероятностное число включенный телевизоров
                    while (n < m0):
                        m0 = random.randint(3, 6)
                    p = round(random.uniform(0.3, 0.7), 1)  # вероятность того, что телевизор включен
                    q = 1 - p
                    m = m0 - 1
                    f = round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                    while (1):
                        m -= 1
                        f += round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                        if (m == 0):
                            break
                    f1 = round(1 - f, 3)
                    s1 = z[0] + str(n) + z[1] + str(p) + z[2] + str(m0) + z[3] + " Ответ: " + str(f1)
                if run == 'z2':
                    z = ["Для вычислительной лаборатории приобретено ",
                         " компьютеров, причем вероятность брака для одного компьютера равна ",
                         ". Какова вероятность, что придется заменить более ", " компьютеров."]
                    n = random.randint(6, 15)  # всего компьютеров
                    m0 = random.randint(2, 6)  # возможное количество компьютеров, подлежащих замене
                    while (n - 4 < m0):
                        m0 = random.randint(2, 6)
                    p = round(random.uniform(0.1, 0.5), 1)  # вероятность брака
                    q = 1 - p
                    m = m0
                    f = round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                    while (1):
                        m -= 1
                        f += round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                        if (m == 0):
                            break
                    f1 = round(1 - f, 3)
                    s1 = z[0] + str(n) + z[1] + str(p) + z[2] + str(m0) + z[3] + " Ответ: " + str(f1)
                if run == 'z3':
                    z = ["Частица пролетает последовательно мимо ",
                         " счетчиков. Каждый счетчик независимо от остальных отмечает ее пролѐт с вероятностью ",
                         ". Частица считается зарегистрированной, если она отмечена не менее чем ",
                         " счетчиками. Найти вероятность зарегистрировать частицу."]
                    n = random.randint(5, 12)  # общее количество счетчиков
                    m0 = random.randint(2, 6)  # вероятное количество счетчиков, зарегистрировавших частицу
                    while ((n - 3 < m0) or (m0 < n - 8)):
                        m0 = random.randint(2, 6)
                    p = round(random.uniform(0.3, 0.8), 1)  # вероятность регистрации частицы для каждого счетчика
                    q = 1 - p
                    m = m0 - 1
                    f = round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                    while (1):
                        m -= 1
                        f += round((factorial(n) / (factorial(m) * factorial(n - m))) * (p ** m) * (q ** (n - m)), 5)
                        if (m == 0):
                            break
                    f1 = round(1 - f, 3)
                    s1 = z[0] + str(n) + z[1] + str(p) + z[2] + str(m0) + z[3] + " Ответ: " + str(f1)
            if tem == 'naiv':
                s1 = 'Задачи отсутствуют'
            if tem == 'muavr-laplas':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = ['В среднем ',
                         '% студентов первого курса продолжают дальнейшее обучение. Какова вероятность, что из ',
                         ' студентов первого курса перейдут на второй курс: а) ровно ', ' человек? б) ровно ',
                         ' человек? в) ровно ', ' человек?']
                    a = random.randint(80, 95)
                    b = random.randint(600, 1000)
                    c = random.randint(400, b - 50)
                    d = random.randint(c, b - 100)
                    e = random.randint(d, b - 50)
                    s = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5]
                    s2 = a / 100
                    s3 = 1 - s2
                    s4 = 1 / ((b * s2 * s3) ** 0.5)
                    s5 = c - (b * s2)
                    s6 = s5 * s4
                    f = math.e ** -((s6 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s7 = round(f * s4, 3)
                    s8 = d - (b * s2)
                    s9 = s8 * s4
                    f1 = math.e ** -((s9 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s10 = round(f1 * s4, 3)
                    s11 = e - (b * s2)
                    s12 = s11 * s4
                    f2 = math.e ** -((s12 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s13 = round(f2 * s4, 3)
                    while ((int(s7 * 1000) == 0) or (int(s10 * 1000) == 0) or (int(s13 * 1000) == 0)):
                        a = random.randint(80, 95)
                        b = random.randint(600, 1000)
                        c = random.randint(400, b - 50)
                        d = random.randint(c, b - 50)
                        e = random.randint(d, b - 50)
                        s = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5]
                        s2 = a / 100
                        s3 = 1 - s2
                        s4 = 1 / ((b * s2 * s3) ** 0.5)
                        s5 = c - (b * s2)
                        s6 = s5 * s4
                        f = math.e ** -((s6 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s7 = round(f * s4, 3)
                        s8 = d - (b * s2)
                        s9 = s8 * s4
                        f1 = math.e ** -((s9 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s10 = round(f1 * s4, 3)
                        s11 = e - (b * s2)
                        s12 = s11 * s4
                        f2 = math.e ** -((s12 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s13 = round(f2 * s4, 3)
                    s1 = s + ' Ответ: ' + str(s7) + ' ' + str(s10) + ' ' + str(s13)
                if run == 'z2':
                    z = ['На факультете ',
                         ' студентов. Вероятность дня рождения каждого студента в данный день равна 1/365. Вычислить вероятность того, что найдутся а) ',
                         ' б) ', ' в) ', ' студента, у которых дни рождения совпадают. ']
                    b = random.randint(500, 1000)
                    c = random.randint(2, 4)
                    d = random.randint(5, 7)
                    e = random.randint(8, 10)
                    s = z[0] + str(b) + z[1] + str(c) + z[2] + str(d) + z[3] + str(e) + z[4]
                    s2 = 1 / 365
                    s3 = 1 - s2
                    s4 = (c - b / 365) / ((b * s2 * s3) ** 0.5)
                    f = math.e ** -((s4 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s5 = 1 / ((b * s2 * s3) ** 0.5)
                    s6 = round(f * s5, 3)
                    s7 = (d - b / 365) / ((b * s2 * s3) ** 0.5)
                    f1 = math.e ** -((s7 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s8 = 1 / ((b * s2 * s3) ** 0.5)
                    s9 = round(f1 * s8, 3)
                    s10 = (e - b / 365) / ((b * s2 * s3) ** 0.5)
                    f2 = math.e ** -((s10 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s11 = 1 / ((b * s2 * s3) ** 0.5)
                    s12 = round(f2 * s11, 3)
                    while ((int(s6 * 1000) == 0) or (int(s9 * 1000) == 0) or (int(s12 * 1000) == 0)):
                        b = random.randint(500, 1000)
                        c = random.randint(2, 4)
                        d = random.randint(5, 7)
                        e = random.randint(8, 10)
                        s = z[0] + str(b) + z[1] + str(c) + z[2] + str(d) + z[3] + str(e) + z[4]
                        s2 = 1 / 365
                        s3 = 1 - s2
                        s4 = (c - b / 365) / ((b * s2 * s3) ** 0.5)
                        f = math.e ** -((s4 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s5 = 1 / ((b * s2 * s3) ** 0.5)
                        s6 = round(f * s5, 3)
                        s7 = (d - b / 365) / ((b * s2 * s3) ** 0.5)
                        f1 = math.e ** -((s7 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s8 = 1 / ((b * s2 * s3) ** 0.5)
                        s9 = round(f1 * s8, 3)
                        s10 = (e - b / 365) / ((b * s2 * s3) ** 0.5)
                        f2 = math.e ** -((s10 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s11 = 1 / ((b * s2 * s3) ** 0.5)
                        s12 = round(f2 * s11, 3)
                    s1 = s + ' Ответ: ' + str(s6) + ' ' + str(s9) + ' ' + str(s12)
                if run == 'z3':
                    z = [
                        'По результатам проверок налоговыми инспекциями установлено, что в среднем каждое второе малое предприятие региона имеет нарушение финансовой дисциплины.'
                        ' Найти вероятность того, что из ',
                        ' зарегистрированных в регионе малых предприятий имеют нарушения финансовой дисциплины: а) ровно ',
                        ' человек? б) ровно ', ' человек? в) ровно ', ' человек?']
                    b = random.randint(800, 1500)
                    c = random.randint(400, b - 200)
                    d = random.randint(c, b - 100)
                    e = random.randint(d, b - 50)
                    s = z[0] + str(b) + z[1] + str(c) + z[2] + str(d) + z[3] + str(e) + z[4]
                    s2 = 0.5
                    s3 = 1 - s2
                    s4 = 1 / ((b * s2 * s3) ** 0.5)
                    s5 = c - (b * s2)
                    s6 = s5 * s4
                    f = math.e ** -((s6 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s7 = f * s4
                    s8 = d - (b * s2)
                    s9 = s8 * s4
                    f1 = math.e ** -((s9 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s10 = f1 * s4
                    s11 = e - (b * s2)
                    s12 = s11 * s4
                    f2 = math.e ** -((s12 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                    s13 = f2 * s4
                    while ((int(s7 * 1000) == 0) or (int(s10 * 1000) == 0) or (int(s13 * 1000) == 0)):
                        b = random.randint(800, 1500)
                        c = random.randint(400, b - 200)
                        d = random.randint(c, b - 100)
                        e = random.randint(d, b - 50)
                        s = z[0] + str(b) + z[1] + str(c) + z[2] + str(d) + z[3] + str(e) + z[4]
                        s2 = 0.5
                        s3 = 1 - s2
                        s4 = 1 / ((b * s2 * s3) ** 0.5)
                        s5 = c - (b * s2)
                        s6 = s5 * s4
                        f = math.e ** -((s6 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s7 = f * s4
                        s8 = d - (b * s2)
                        s9 = s8 * s4
                        f1 = math.e ** -((s9 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s10 = f1 * s4
                        s11 = e - (b * s2)
                        s12 = s11 * s4
                        f2 = math.e ** -((s12 ** 2) / 2) / ((math.pi * 2) ** 0.5)
                        s13 = f2 * s4
                    s1 = s + ' Ответ: ' + str(round(s7, 3)) + ' ' + str(round(s10, 3)) + ' ' + str(round(s13, 3))
            if tem == 'int-muavr-laplas':
                run = random.choice(['z1', 'z2','z3'])
                if run == 'z1':
                    z = [
                        'При обследовании уставных фондов банков установлено, что пятая часть банков имеют уставный фонд свыше 100 млн руб. Найти вероятность того, что среди ',
                        ' банков имеют уставный фонд свыше 100 млн руб.: а) не менее ', '; б) от ', ' до ',
                        ' включительно; в) не более ', '.']
                    p = 0.2
                    n = random.randint(630, 1000)
                    q = 1 - p
                    ma = random.randint(n // 5, n // 3)
                    a1 = (n - n * p) / ((n * p * q) ** (0.5))
                    a2 = (ma - n * p) / ((n * p * q) ** (0.5))
                    fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                    mb = random.randint(60, ma - 10)
                    b1 = (mb - n * p) / ((n * p * q) ** (0.5))
                    b2 = (ma - n * p) / ((n * p * q) ** (0.5))
                    fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                    mc = random.randint(100, n // 3)
                    c1 = (mc - n * p) / ((n * p * q) ** (0.5))
                    c2 = (0 - n * p) / ((n * p * q) ** (0.5))
                    fc = (scipy.stats.norm.cdf(c1) - 0.5) - (scipy.stats.norm.cdf(c2) - 0.5)
                    while ((int(fb * 100) == 0) or (int(fa * 100) == 0) or (int(fc * 100) == 0)):
                        p = 0.2
                        n = random.randint(630, 1000)
                        q = 1 - p
                        ma = random.randint(n // 5, n // 3)
                        a1 = (n - n * p) / ((n * p * q) ** (0.5))
                        a2 = (ma - n * p) / ((n * p * q) ** (0.5))
                        fa = (scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5)
                        mb = random.randint(60, ma - 10)
                        b1 = (mb - n * p) / ((n * p * q) ** (0.5))
                        b2 = (ma - n * p) / ((n * p * q) ** (0.5))
                        fb = (scipy.stats.norm.cdf(b1) - 0.5) - (scipy.stats.norm.cdf(b2) - 0.5)
                        mc = random.randint(100, n // 3)
                        c1 = (mc - n * p) / ((n * p * q) ** (0.5))
                        c2 = (0 - n * p) / ((n * p * q) ** (0.5))
                        fc = (scipy.stats.norm.cdf(c1) - 0.5) - (scipy.stats.norm.cdf(c2) - 0.5)
                    s1 = z[0] + str(n) + z[1] + str(ma) + z[2] + str(mb) + z[3] + str(ma) + z[4] + str(mc) + z[5] + ' Ответ: ' + str(abs(round(fa, 3))) + ' ' \
                         + str(abs(round(fb, 3))) + ' ' + str(abs(round(fc, 3)))
                if run == 'z2':
                    z = ['При установившемся технологическом процессе фабрика выпускает в среднем ',
                         '% продукции первого сорта. Чему равна вероятность того, что в партии из ',
                         ' изделий число первосортных заключено: a) между ', ' и ', '; б) между ', ' и ',
                         '; в) между ', ' и ', '?']

                    def laplas(n, p, a, b):
                        q = 1 - p
                        a1 = (b - n * p) / ((n * p * q) ** (0.5))
                        a2 = (a - n * p) / ((n * p * q) ** (0.5))
                        return ((scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5))

                    n = random.randint(1000, 1500)
                    p = random.randint(1, 99) / 100
                    a1 = random.randint(100, n // 6)
                    b1 = random.randint(a1, n // 5)
                    a2 = b1
                    b2 = random.randint(a2, a2 + 100)
                    a3 = b2
                    b3 = random.randint(a3, a3 + 100)
                    f1 = abs(round(laplas(n, p, a1, b1), 3))
                    f2 = abs(round(laplas(n, p, a2, b2), 3))
                    f3 = abs(round(laplas(n, p, a3, b3), 3))
                    while ((int(f1 * 100) == 0) or (int(f2 * 100) == 0) or (int(f3 * 100) == 0)):
                        n = random.randint(1000, 1500)
                        p = random.randint(1, 99) / 100
                        a1 = random.randint(100, n // 6)
                        b1 = random.randint(a1, n // 5)
                        a2 = b1
                        b2 = random.randint(a2, a2 + 100)
                        a3 = b2
                        b3 = random.randint(a3, a3 + 100)
                        f1 = abs(round(laplas(n, p, a1, b1), 3))
                        f2 = abs(round(laplas(n, p, a2, b2), 3))
                        f3 = abs(round(laplas(n, p, a3, b3), 3))
                    s1 = z[0] + str(int(p * 100)) + z[1] + str(n) + z[2] + str(a1) + z[3] + str(b1) + z[4] + str(a2) + z[5] + str(b2) + z[6] + str(a3) + z[7] + str(b3) + z[8] + \
                         ' Ответ: ' + str(f1) + ' ' + str(f2) + ' ' + str(f3)
                if run == 'z3':
                    z = ['Вероятность запомнить одно слово на уроке в процессе изучения иностранного языка равна p = ',
                         '. Найти вероятности: из n = ', '; n = ', '; n = ', ' новых слов ученик запомнит не менее ',
                         '.']

                    def laplas(n, p, a):
                        q = 1 - p
                        a1 = (n - n * p) / ((n * p * q) ** (0.5))
                        a2 = (a - n * p) / ((n * p * q) ** (0.5))
                        return ((scipy.stats.norm.cdf(a1) - 0.5) - (scipy.stats.norm.cdf(a2) - 0.5))

                    n1 = random.randint(50, 60)
                    n2 = random.randint(60, 70)
                    n3 = random.randint(70, 80)
                    p = random.randint(50, 99) / 100
                    m = int(n1 * 0.8)
                    f1 = abs(round(laplas(n1, p, m), 3))
                    f2 = abs(round(laplas(n2, p, m), 3))
                    f3 = abs(round(laplas(n3, p, m), 3))
                    s1 = z[0] + str(p) + z[1] + str(n1) + z[2] + str(n2) + z[3] + str(n3) + z[4] + str(m) + z[5] + ' Ответ: ' + str(f1) + ' ' + str(f2) + ' ' + str(f3)
            if tem == 'puass':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Производители заклепок для крепления обшивки самолета гарантируют, что в среднем только одна заклепка из ',
                        ' не выдержит экстремальных нагрузок и лопнет. Какова вероятность того, что из ',
                        ' использованных при постройке самолета выйдут из строя а) ровно ', ' заклепок; б) не менее ',
                        ' заклепок; в) не более ', ' заклепок?']
                    n = random.randint(10, 16) * 1000
                    m = random.randint(1, 9) * 1000
                    while ((n % m != 0) or (m == 1000 and n > 13000)):
                        m = random.randint(1, 9) * 1000
                    p = 1 / m
                    v = n * p
                    k = random.randint(2, 8)
                    pys = round(((v ** k) / factorial(k)) * exp(-v), 5)
                    k0 = k
                    pys01 = 1
                    while (k0 != 0):
                        k0 -= 1
                        pys0 = round(((v ** k0) / factorial(k0)) * exp(-v), 5)
                        pys01 -= pys0
                    k0 = k
                    pys02 = 0
                    while (k0 >= 0):
                        pys0 = round(((v ** k0) / factorial(k0)) * exp(-v), 5)
                        pys02 += pys0
                        k0 -= 1

                    s1 = z[0] + str(m) + z[1] + str(n) + z[2] + str(k) + z[3] + str(k) + z[4] + str(k) + z[5] + ' Ответ: ' + str(round(pys, 3)) + ' ' + str(round(pys01, 3)) \
                         + ' ' + str(round(pys02, 3))
                if run == 'z2':
                    z = [
                        'В семье слесаря Осипа Хангриева на Рождество принято лепить большое количество пельменей, причем в каждый ',
                        ' пельмень для улучшения настроения едока подкладывается чесночный зубчик. Какова вероятность того, что после поедания ',
                        ' пельменей настроение Осипа поднимется а) на ', ' пункта б) не менее ', ' в) не более ', '?']
                    n = random.randint(20, 70)
                    m = random.randint(5, 15)
                    while (m % 5 != 0):
                        m = random.randint(5, 15)
                    k = random.randint(2, 4)
                    while ((n / m < 4) or (n / m > 10)):
                        n = random.randint(20, 70)
                    v = n * (1 / m)
                    pys = round(((v ** k) / factorial(k)) * exp(-v), 5)
                    k0 = k
                    pys01 = 1
                    while (k0 != 0):
                        k0 -= 1
                        pys0 = round(((v ** k0) / factorial(k0)) * exp(-v), 5)
                        pys01 -= pys0
                    k0 = k
                    pys02 = 0
                    while (k0 >= 0):
                        pys0 = round(((v ** k0) / factorial(k0)) * exp(-v), 5)
                        pys02 += pys0
                        k0 -= 1

                    s1 = z[0] + str(m) + z[1] + str(n) + z[2] + str(k) + z[3] + str(k) + z[4] + str(k) + z[5] + ' Ответ: ' + str(round(pys, 3)) + ' ' +\
                         str(round(pys01, 3)) + ' ' + str(round(pys02, 3))
                if run == 'z3':
                    z = ['Среднее число автомобилей, проходящих таможенный досмотр в течение часа, равно ',
                         '. Найти вероятность того, что: а) за ', ' часа пройдут досмотр от ', ' до ',
                         ' автомобилей; б) за полчаса успеет пройти досмотр только ',
                         ' автомобиль(я); в) за час успеет пройти не менее ', ' автомобиля.']
                    n = random.randint(3, 6)
                    t = random.randint(2, 4)
                    m0 = random.randint(5, 8)
                    m1 = random.randint(9, 12)
                    while ((m1 - m0 < 2) or (m1 - m0 > 4)):
                        m1 = random.randint(9, 12)
                    m2 = random.randint(1, 3)
                    m3 = random.randint(2, 5)
                    v = t * n  # среднее количество автомобилей, проходящих таможенный досмотр, в течение t часов
                    m = m0
                    pys01 = 0
                    while (m <= m1):
                        pys0 = round(((v ** m) / factorial(m)) * exp(-v), 5)
                        pys01 += pys0
                        m += 1
                    v = 0.5 * n
                    pys02 = round(((v ** m2) / factorial(m2)) * exp(-v), 5)
                    m03 = m3
                    pys03 = 1
                    while (m03 != 0):
                        m03 -= 1
                        pys0 = round(((v ** m03) / factorial(m03)) * exp(-v), 5)
                        pys03 -= pys0
                    s1 = z[0] + str(n) + z[1] + str(t) + z[2] + str(m0) + z[3] + str(m1) + z[4] + str(m2) + z[5] + str(m3) + z[6] + ' Ответ: ' +\
                         str(round(pys01, 3)) + ' ' + str(round(pys02, 3)) + ' ' + str(round(pys03, 3))
            if tem == 'diskr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Два баскетболиста делают по три броска в корзину. Вероятность попадания для первого баскетболиста равна ',
                        ', для второго – ',
                        '. Пусть X - разность между числом удачных бросков первого и второго баскетболистов. Вычислить математическое ожидание, дисперсию и '
                        'среднее квадратичное отклонение.']
                    m = random.randint(60, 90)
                    n = random.randint(70, 90)
                    k = m / 100
                    o = 1 - k
                    l = n / 100
                    t = 1 - l
                    a = 1 * (k ** 0) * (o ** 3)
                    b = 3 * (k ** 1) * (o ** 2)
                    c = 3 * (k ** 2) * (o ** 1)
                    d = 1 * (k ** 3) * (o ** 0)
                    e = 1 * (l ** 0) * (t ** 3)
                    f = 3 * (l ** 1) * (t ** 2)
                    g = 3 * (l ** 2) * (t ** 1)
                    h = 1 * (l ** 3) * (t ** 0)
                    p0 = a * e + b * f + c * g + d * h
                    p1 = b * e + c * f + d * g
                    p2 = c * e + d * f
                    p3 = d * e
                    p11 = a * f + b * g + c * h
                    p22 = a * g + b * h
                    p33 = a * h
                    mx = (-3) * p33 + (-2) * p22 + (-1) * p11 + 0 * p0 + 1 * p1 + 2 * p2 + 3 * p3
                    dx = (9 * p33 + 4 * p22 + 1 * p11 + 0 * p0 + 1 * p1 + 2 * p2 + 3 * p3) - (mx ** 2)
                    cko = dx ** (1 / 2)
                    s1 = z[0] + str(k) + z[1] + str(l) + z[2] + ' Ответ: ' + str(round(mx, 3)) + ' ' + str(round(dx, 3)) + ' ' + str(round(cko, 3))
                if run == 'z2':
                    z = [' По цели производится 4 выстрела. Вероятность попадания при этом растет так: ', ', ', ', ',
                         ', ', '. X - число попаданий. Найти вероятность того, что X ≥1.']
                    m = random.randint(10, 29)
                    n = random.randint(30, 45)
                    k = random.randint(46, 64)
                    l = random.randint(65, 80)
                    m1 = m / 100
                    n1 = n / 100
                    k1 = k / 100
                    l1 = l / 100
                    a = 1 - m1
                    b = 1 - n1
                    c = 1 - k1
                    d = 1 - l1
                    p4 = m1 * n1 * k1 * l1
                    p3 = m1 * n1 * k1 * d + m1 * n1 * c * l1 + m1 * b * k1 * l1 + a * n1 * k1 * l1
                    p2 = m1 * n1 * c * d + m1 * b * k1 * d + m1 * b * c * l1 + a * n1 * k1 * d + a * n1 * c * l1 + a * b * k1 * l1
                    p1 = m1 * b * c * d + a * n1 * c * d + a * b * k1 * d + a * b * c * l1
                    p0 = a * b * c * d
                    s1 = z[0] + str(m1) + z[1] + str(n1) + z[2] + str(k1) + z[3] + str(l1) + z[4] + ' Ответ: ' + str(round(1 - p0, 3))
                if run == 'z3':
                    z = [
                        'Число иногородних судов, прибывающих ежедневно под погрузку в определенный порт – случайная величина X , заданная так: p0 = ',
                        '; p1 = ', '; p2 = ', '; p3 = ', '; p4 = ', '; p5 = ',
                        '. Если в заданный день прибывает больше трех судов, то порт берет на себя ответственность за издержки вследствие необходимости нанимать '
                        'дополнительных водителей и грузчиков. Чему равна вероятность того, что порт понесет дополнительные расходы? Найдите математическое ожидание, '
                        'дисперсию и среднее квадратическое отклонение случайной величины X.']
                    a = random.randint(0, 15)
                    b = random.randint(0, 25)
                    c = random.randint(0, 30)
                    d = random.randint(0, 10)
                    e = random.randint(0, 15)
                    a = a / 100
                    b = b / 100
                    c = c / 100
                    d = d / 100
                    e = e / 100
                    f = round((1 - a - b - c - d - e), 3)
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + str(f) + z[6] + ' Ответ: ' + str(round(e + f, 3)) + \
                         ' ' + str(round(0 * a + 1 * b + 2 * c + 3 * d + 4 * e + 5 * f, 3)) + ' ' + str(round(0 * a + 1 * b + 4 * c + 9 * d + 16 * e + 25 * f, 3)) +\
                         ' ' + str(round((0 * a + 1 * b + 4 * c + 9 * d + 16 * e + 25 * f) ** (1 / 2), 3))
            if tem == 'nepr':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    lowerLimit = np.random.randint(3, 5)
                    upperLimit = np.random.randint(7, 9)
                    x = symbols('x')
                    expr = x ** 2
                    MX, DX = [
                        round(sympy.Integral(expr, (x, lowerLimit, upperLimit)).doit(), 3),
                        round(sympy.Integral(expr * x ** 2, (x, lowerLimit, upperLimit)).doit(), 3)
                    ]
                    StandardDeviation = round(sympy.sqrt(DX), 3)
                    problemCondition = f"""Случайная величина X задана функцией распределения F(x):
                    \t0\tпри x <= {lowerLimit},
                    \tx**2\tпри {lowerLimit} < x < {upperLimit},
                    \t1\tпри x > {upperLimit}.
                    Найти математическое ожидание, дисперсию, среднее квадратическое отклонение. Ответ округлить до трех знаков после запятой."""
                    ans = f' Ответ: {round(MX, 3)} {round(DX, 3)} {round(StandardDeviation, 3)}'
                    s1 = problemCondition + ans
                if run == 'z2':
                    randomNumerator = np.random.randint(13, 17)
                    lowerLimit = pi
                    upperLimit = 3 * pi / 2
                    x = symbols('x')
                    expr = -cos(x)
                    pX, MX, DX = [
                        round(sympy.Integral(expr, (x, pi, randomNumerator * pi / 12)).doit(), 3),
                        round(sympy.Integral(expr, (x, lowerLimit, upperLimit)).doit(), 3),
                        round(sympy.Integral(expr * x ** 2, (x, lowerLimit, upperLimit)).doit(), 3)
                    ]
                    problemCondition = f""" Случайная величина X задана дифференциальной функцией распределения:
                    \t0\tпри x <= pi,
                    \t-cos(x)\tпри pi < x <= 3pi/2,
                    \t0\tпри x > 3/2pi.
                    Найти: 1) вероятность попадания случайной величины X в интервал [pi, {randomNumerator}pi/12], 2) математическое ожидание и дисперсию случайной величины X."""
                    ans = f' Ответ: {round(pX, 3)} {round(MX, 3)} {round(DX, 3)}'
                    s1 = problemCondition + ans
                if run == 'z3':
                    lowerLimit = np.random.randint(1, 3)
                    upperLimit = np.random.randint(8, 10)
                    x = symbols('x')
                    expr = exp(x) / 10
                    MX, DX = [
                        sympy.Integral(expr, (x, lowerLimit, upperLimit)).doit(),
                        sympy.Integral(expr * x ** 2, (x, lowerLimit, upperLimit)).doit()
                    ]
                    problemCondition = f""" Случайная величина X задана дифференциальной функцией распределения:
                    \t0\tпри x <= {lowerLimit},
                    \t1/10*e^(x)\tпри {lowerLimit} < x <= {upperLimit},
                    \t0\tпри x > {upperLimit}.
                    Найти математическое ожидание и дисперсию случайной величины X."""
                    ans = f' Ответ: {round(MX, 3)} {round(DX, 3)}'
                    s1 = problemCondition + ans
            if tem == 'norm':
                run = random.choice(['z1', 'z2', 'z3'])
                if run == 'z1':
                    z = [
                        'Дневная добыча угля в некоторой шахте распределена по нормальному закону с математическим ожиданием ',
                        ' т и стандартным отклонением ',
                        ' т. Найдите вероятность того, что в определенный день будут добыты, по крайней мере, ',
                        ' т угля. Определите долю рабочих дней, в которые будет добыто от ', ' т до ', ' т угля.']
                    a = random.randint(700, 800)
                    b = random.randint(50, 80)
                    c = random.randint(a + 20, 850)
                    d = random.randint(a - 50, 800)
                    e = random.randint(d + 20, a + 100)

                    s2 = round((c - a) / b, 2)
                    f = scipy.stats.norm.cdf(s2)
                    otvet = abs(f)  # может быть отрицательным, поэтому берем модуль abs()
                    s3 = round((e - a) / b, 2)
                    s4 = round((d - a) / b, 2)
                    f2 = scipy.stats.norm.cdf(s3)
                    f3 = scipy.stats.norm.cdf(s4)
                    otvet1 = abs(f2 - f3)  # может быть отрицательным, поэтому берем модуль abs()
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + ' Ответ: ' + str(round(otvet, 3)) + ' ' +\
                         str(round(otvet1, 3))
                if run=='z2':
                    z = ['Коробки с конфетами упаковываются автоматически. Их средняя масса равна ',
                         ' г, стандартное отклонение равно ',
                         ' т. Найдите вероятность того, что масса коробок, а) по крайней мере, ', ' г. б)от ', ' до ',
                         ' г.']
                    a = random.randint(400, 600)
                    b = random.randint(20, 30)
                    c = random.randint(a - 100, 590)
                    d = random.randint(300, 400)
                    e = random.randint(d + 20, a + 100)
                    s2 = round((c - a) / b, 2)
                    f = scipy.stats.norm.cdf(s2)
                    otvet = abs(f)  # может быть отрицательным, поэтому берем модуль abs()
                    s3 = round((e - a) / b, 2)
                    s4 = round((d - a) / b, 2)
                    f2 = scipy.stats.norm.cdf(s3)
                    f3 = scipy.stats.norm.cdf(s4)
                    otvet1 = abs(f2 - f3)  # может быть отрицательным, поэтому берем модуль abs()
                    while (int(otvet * 1000) == 0) or ((int(otvet1 * 1000) == 0)):
                        a = random.randint(400, 600)
                        b = random.randint(20, 30)
                        c = random.randint(a - 100, 590)
                        d = random.randint(300, 400)
                        e = random.randint(d + 20, a + 100)
                        s2 = round((c - a) / b, 2)
                        f = scipy.stats.norm.cdf(s2)
                        otvet = abs(f)  # может быть отрицательным, поэтому берем модуль abs()
                        s3 = round((e - a) / b, 2)
                        s4 = round((d - a) / b, 2)
                        f2 = scipy.stats.norm.cdf(s3)
                        f3 = scipy.stats.norm.cdf(s4)
                        otvet1 = abs(f2 - f3)  # может быть отрицательным, поэтому берем модуль abs()
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + ' Ответ: ' + \
                         str(round(otvet, 3)) + ' ' + str(round(otvet1, 3))
                if run == 'z3':
                    z = ['Вес пойманной рыбы подчиняется нормальному закону. Cредняя масса равна ',
                         ' г, стандартное отклонение равно ', ' г. Найдите вероятность того, что вес одной рыбы а) от ',
                         ' до ', ' г. б) не более ', '.']
                    a = random.randint(200, 400)
                    b = random.randint(20, 30)
                    c = random.randint(a - 100, 400)
                    d = random.randint(100, 250)
                    e = random.randint(d + 20, a + 100)
                    s2 = round((c - a) / b, 2)
                    f = scipy.stats.norm.cdf(s2)
                    otvet = round(abs(f), 3)  # может быть отрицательным, поэтому берем модуль abs()
                    s3 = round((e - a) / b, 2)
                    s4 = round((d - a) / b, 2)
                    f2 = scipy.stats.norm.cdf(s3)
                    f3 = scipy.stats.norm.cdf(s4)
                    otvet1 = round(abs(f2 - f3), 3)  # может быть отрицательным, поэтому берем модуль abs()
                    while (int(otvet * 1000) == 0) or ((int(otvet1 * 1000) == 0)):
                        a = random.randint(200, 400)
                        b = random.randint(20, 30)
                        c = random.randint(a - 100, 400)
                        d = random.randint(100, 250)
                        e = random.randint(d + 20, a + 100)
                        s2 = round((c - a) / b, 2)
                        f = scipy.stats.norm.cdf(s2)
                        otvet = round(abs(f), 3)  # может быть отрицательным, поэтому берем модуль abs()
                        s3 = round((e - a) / b, 2)
                        s4 = round((d - a) / b, 2)
                        f2 = scipy.stats.norm.cdf(s3)
                        f3 = scipy.stats.norm.cdf(s4)
                        otvet1 = round(abs(f2 - f3), 3)  # может быть отрицательным, поэтому берем модуль abs()
                    s1 = z[0] + str(a) + z[1] + str(b) + z[2] + str(c) + z[3] + str(d) + z[4] + str(e) + z[5] + ' Ответ: ' +\
                         str(otvet) + ' ' + str(otvet1)
            vop = int(request.GET.get('numbervop'))
            Task.objects.filter(nomer=vop).delete()
            Task(zadacha=s1, nomer=vop).save()
            return render(request, 'app/vibor.html',
                          {'task': s1, 'nametem': tem, 'slozh': sl, 'numbervop': vop, 'numbers': numbers})
        else:
            return render(request, 'app/vibor.html', {'numbers': numbers})
    if ko:
        Kol.objects.all().delete()
        numbers = []
        for i in range(1, int(ko) + 1):
            Kol(koli=i, foli=str(i)).save()
            numbers.append(i)
        Task.objects.all().delete()
        return render(request, 'app/vibor.html',{'kol': ko, 'numbers': numbers})


def Shablon(request, A4=None):
    sohr_tasks = Task.objects.order_by('nomer')
    doc = docx.Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    for i in sohr_tasks:
        doc.add_paragraph(str(i))
    doc.save('app/static/vendor/files/Задачи.docx')

    MyFontObject = ttfonts.TTFont('Arial', 'arial.ttf')
    pdfmetrics.registerFont(MyFontObject)
    MyCanvas = canvas.Canvas("app/static/vendor/files/hello.pdf", pagesize=A4)
    MyCanvas.setFont("Arial", 14)

    def obrez(text):
        text1 = text.split()
        kol_slov_v_text = len(text1)
        itog = []
        while kol_slov_v_text > 0:
            slova1 = 0
            ma = 65
            count = 0
            stroka = []
            izmen = len(text1)
            for i in range(izmen):
                l = len(text1[i])
                if count + l < ma:
                    count += l
                    stroka.append(text1[i])
                    slova1 += 1
                else:
                    break
            kol_slov_v_text -= slova1
            itog.append(' '.join(stroka))
            text1 = text1[slova1:]
        return itog
    c_gl = 800
    for i in sohr_tasks:
        c = c_gl
        text = str(i)
        text_2 = obrez(text)

        for j in range(len(text_2)):
            MyCanvas.drawString(50, c, text_2[j])
            c -= 25
        c_gl -= 25 * (len(text_2)+1)
    MyCanvas.save()

    if request.method == 'POST':
        email = request.POST['email']
        msg = EmailMessage('Задачи для подготовки',' ', 'settings.EMAIL_HOST_USER', [email])
        msg.attach_file('app/static/vendor/files/Задачи.docx')
        msg.send()
    #subprocess.run(["open", "-a", "Google Chrome", 'hello.pdf'])
    return render(request, 'app/Shablon.html',{'sohr': sohr_tasks})

def teor(request):
    return render(request, 'app/teor.html')



