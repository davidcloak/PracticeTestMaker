from django.shortcuts import render
from django.http import HttpResponse

savedTest = {}
savedTest['Something'] = "nothing lol"
# to randamize change how the test is saved by switching from saving the whole display to saving a dictianary with saved cards
savedTest['nav'] = '<div style="height: 3.25em;"></div><nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark"><div class="container-fluid"><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarNav"><ul class="navbar-nav"><li class="nav-item"><a class="nav-link" href="/">Home</a></li><li class="nav-item"><a class="nav-link" href="/make">Make A Test</a></li><li class="nav-item"><a class="nav-link" href="/take">Take A Made Test</a></li></ul></div></div></nav>'

# Create your views here.
def home_page(request):
    return render(request, 'Home.html', savedTest)

def make_page(request):
    return render(request, 'MakeTest.html', savedTest)

def take_page(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        test = {}
        test["amount"] = "Saved Test"
        test["display"] = savedTest[name]
        test['name'] = name
        test['nav'] = savedTest['nav']
        return render(request, 'Test.html', test)
    else:
        return render(request, 'TakeTest.html', savedTest)


# DONE - redo the way tests are made so that awnsers names are no longer the same
# DONE - add div endings after the fact with the rest of the test being generated in a for loop
def test_page(request):
    display = ''
    if request.method == 'POST':
        test = {}
        test["amount"] = request.POST.get("QAmount")
        #savedTest['amount'] = test["amount"] #Saved
        num = test["amount"]

        display = '<input type="hidden" name="QAmount" value="'+str(num)+'">'

        for x in range(int(num)):
            qType = request.POST.get('qType'+str(x))
            #savedTest['qType'+str(x)] = qType #Saved
            if qType == 'Multi':
                question = request.POST.get('question'+str(x))
                display += '<div class="card"> <div class="card-body"> <h5 class="card-title">'+ question +'</h5>'
                
                #savedTest['question'+str(x)] = question #Saved

                amount = request.POST.get('qAmount'+str(x))
                
                display += '<input type="hidden" name="qType'+str(x)+'" value="'+qType+'">'
                display += '<input type="hidden" name="qAmount'+str(x)+'" value="'+amount+'">'
                correct = request.POST.get('correct'+str(x))
                display += '<input type="hidden" name="correct'+str(x)+'" value="'+correct+'">'
                display += '<input type="hidden" name="questionA'+str(x)+'" value="'+question+'">'
                
                display += '<input hidden type="radio" id="question-1" name="question'+str(x)+'" value="" checked>'

                for i in range(int(amount)+1):
                    awnsers = request.POST.get("awnser"+str(x)+str(i)+"[]")
                    #savedTest['awnser'+str(x)+str(i)] = awnsers #Saved
                    # display += '<h1>'+awnsers+' / '+amount+' / '+str(i)+'</h1>'
                    display += '<input type="radio" id="question'+str(i)+'" name="question'+str(x)+'" value="'+awnsers+'">'
                    display += '<label for="question'+str(i)+'">'+awnsers+'</label><br>'

                display += '</div> </div>'
            elif qType == 'Open':
                question = request.POST.get('question'+str(x))
                display += '<div class="card"> <div class="card-body"> <h5 class="card-title">'+ question +'</h5>'
                display += '<input type="hidden" name="qType'+str(x)+'" value="'+qType+'">'
                display += '<input type="hidden" name="questionA'+str(x)+'" value="'+question+'">'
                desired = request.POST.get('desired'+str(x))
                display += '<input type="hidden" name="desired'+str(x)+'" value="'+desired+'">'
                display += '<textarea name="awnser'+str(x)+'" row="4" cols="50"></textarea>'
                display += '</div> </div>'
        
        name = request.POST.get("name")
        savedTest[name] = display
        test['display'] = display
        test['name'] = name
        test['nav'] = savedTest['nav']
        return render(request, 'Test.html', test)
    else:
        test = {}
        test['nav'] = savedTest['nav']
        return render(request, 'Home.html', test)


def check(request):
    display = ''
    if request.method == 'POST':
        test = {}
        c = 0
        a = 0
        test["amount"] = request.POST.get("QAmount")
        #savedTest['amount'] = test["amount"] #Saved
        num = test["amount"]
        display += '<input type="hidden" name="QAmount" value="'+str(num)+'">'
        for x in range(int(num)):
            qType = request.POST.get('qType'+str(x))
            #savedTest['qType'+str(x)] = qType #Saved
            if qType == 'Multi':
                correct = request.POST.get('correct'+str(x))
                awnser = request.POST.get('question'+str(x))

                if awnser == correct:
                    a += 1
                    c += 1
                    question = request.POST.get('question'+str(x))
                    questionA = request.POST.get('questionA'+str(x))
                    display += '<div class="card"> <div class="card-body"> <h5 class="card-title">'+ questionA +'</h5>'

                    amount = request.POST.get('qAmount'+str(x))
                    
                    display += '<input type="hidden" name="qType'+str(x)+'" value="'+qType+'">'
                    display += '<input type="hidden" name="qAmount'+str(x)+'" value="'+amount+'">'
                    display += '<p style="color: green;">Selected Awnser: ' + awnser +' Correct: '+correct+'</p>'
                else:
                    a += 1
                    question = request.POST.get('question'+str(x))
                    display += '<div class="card"> <div class="card-body" style="background-color: rgba(255, 66, 82, 0.8);"> <h5 class="card-title">'+ question +'</h5>'

                    amount = request.POST.get('qAmount'+str(x))
                    
                    display += '<input type="hidden" name="qType'+str(x)+'" value="'+qType+'">'
                    display += '<input type="hidden" name="qAmount'+str(x)+'" value="'+amount+'">'
                    display += '<p>Selected Awnser: ' + awnser +' Correct: '+correct+'</p>'

                display += '</div> </div>'
            elif qType == 'Open':
                question = request.POST.get('questionA'+str(x))
                display += '<div class="card"> <div class="card-body"> <h5 class="card-title">'+ question +'</h5>'
                display += '<input type="hidden" name="questionA'+str(x)+'" value="'+question+'">'
                awnser = request.POST.get('awnser'+str(x))
                desired = request.POST.get('desired'+str(x))
                display += '<p name="desired'+str(x)+'" style="border: 0.15em solid black;"><strong>Desired Awnser:</strong> '+desired+'</p>'
                display += '<p name="awnser'+str(x)+'" style="border: 0.15em solid black;"><strong>Your Awnser:</strong> '+awnser+'</p>'
                display += '</div> </div>'
        
        name = request.POST.get("name")
        test['display'] = display
        test['name'] = name
        test['amount'] = 'Multiple Choise Correct: '+str(c)+'/'+str(a)
        test['nav'] = savedTest['nav']
        return render(request, 'result.html', test)

    return render(request, 'Home.html', savedTest)
