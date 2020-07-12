from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.utils import timezone


# Create your views here.
def index(request):
    # pybo 목록 출력
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # pybo 목록 출력
    # question = Question.objects.get(id=question_id) --> 404 오류 페이지 출력  -> 못얻으면 404리턴
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    # pybo 질문등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # 입력된 값이 유효한지 확인
            question = form.save(commit=False) # 모델을 저장하지 않고 객체만 리턴받기 위해 commit=False 추가
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
