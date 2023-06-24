from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
import datetime

# Create your views here.
from Remote_User.models import review_Model,ClientRegister_Model,usertweets_Model


def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:

            enter = ClientRegister_Model.objects.get(username=username, password=password)
            request.session["userid"] = enter.id
            request.session["tcity"] = enter.city
            return redirect('ViewYourProfile')
        except:
            pass

    return render(request,'RUser/login.html')



def Register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        actype='Normal'
        reason = 'Nothing'

        ut = 'Normal'
        fur = 'Nothing'

        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city,actype=actype,Reason=reason,utype=ut,fureason=fur)

        return render(request, 'RUser/Register.html')
    else:

        return render(request,'RUser/Register.html')


def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})

def Review(request,pk):
    userid = request.session['userid']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username

    objs = usertweets_Model.objects.get(id=pk)
    tname = objs.names

    datetime_object = datetime.datetime.now()

    result = ''

    se = 'se'
    if request.method == "POST":
        uname = request.POST.get('uname')
        tname1 = request.POST.get('tname')
        feedback = request.POST.get('feedback')
        cmd = request.POST.get('review')


        if '#' in cmd:
            startingpoint = cmd.find('#')
            a = cmd[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
        # return redirect('')

        for f in cmd.split():
            if f in ('good', 'nice', 'better', 'best', 'excellent', 'extraordinary', 'happy', 'won', 'love', 'greate'):
                se = 'Positive'
            elif f in ('worst', 'waste', 'poor', 'error', 'imporve', 'bad'):
                se = 'Neagtive'

            elif f in ('fuck', 'booms', 'suck', 'hottie', 'babe', 'beefy', 'hot'):
                se = 'Sexual'
                obj = get_object_or_404(ClientRegister_Model, id=userid)

                obj.utype = 'Fake User'
                obj.fureason = 'Reviewed with Sexual Message '
                obj.save(update_fields=['utype', 'fureason'])



            elif f in ('shut up', 'blast', 'kill', 'shoot', 'kick', 'kick out', 'murder'):
                se = 'Offensive'
                obj = get_object_or_404(ClientRegister_Model, id=userid)
                obj.utype = 'Fake User'
                obj.fureason = 'Reviewed with Offensice Fake Message '
                obj.save(update_fields=['utype', 'fureason'])


            elif f in ('ridicules', 'nasty', 'horrible', 'bore', 'unhappy'):
                se = 'Hateful'

            elif f in ('stupid', 'bastard', 'brutal', 'blady'):
                se = 'Volgar'
                obj = get_object_or_404(ClientRegister_Model, id=userid)

                obj.utype = 'Fake User'
                obj.fureason = 'Reviewed with Volgar Message '
                obj.save(update_fields=['utype', 'fureason'])

        review_Model.objects.create(uname=uname , ureview=cmd,sanalysis=se,dt=datetime_object,tname=tname1 ,feedback=feedback)

    return render(request,'RUser/Review.html', {'objc':username,'objc1':tname,'result': result, 'se': se})

def Post_Tweet(request):
    userid = request.session['userid']
    tcity = request.session['tcity']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username
    cmd=''
    uname=''
    tname=''
    uname1 = ''
    tname1 = ''
    result = ''
    pos = []
    neg = []
    oth = []
    se = 'se'
    if request.method == "POST":

        uname = request.POST.get('uname')
        tname = request.POST.get('tname')
        uses = request.POST.get('uses')
        cmd = request.POST.get('tdesc')
        tcity1 = request.POST.get('city')



        if '#' in cmd:
            startingpoint = cmd.find('#')
            a = cmd[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
            # return redirect('')

        for f in cmd.split():
            if f in ('good', 'nice', 'better', 'best', 'excellent', 'extraordinary', 'happy', 'won', 'love', 'greate'):
                se='Positive'
            elif f in ('worst', 'waste', 'poor', 'error', 'imporve', 'bad'):
                se = 'Neagtive'

            elif f in ('fuck','booms','suck','hottie','babe','beefy','hot'):
                se='Sexual'
                obj = get_object_or_404(ClientRegister_Model, id=userid)
                obj.actype = 'Spam Account'
                obj.Reason = 'Tweeted with Sexual Word'
                obj.save(update_fields=['actype', 'Reason'])


            elif f in ('shut up','blast','kill','shoot','kick','kick out','murder'):
                se = 'Offensive'
                obj = get_object_or_404(ClientRegister_Model, id=userid)
                obj.actype = 'Spam Account'
                obj.Reason = 'Tweeted with Offensive Word'
                obj.save(update_fields=['actype','Reason'])

            elif f in ('ridicules', 'nasty', 'horrible', 'bore', 'unhappy'):
                se = 'Hateful'

            elif f in ('stupid','bastard','brutal','blady'):
                se = 'Volgar'
                obj = get_object_or_404(ClientRegister_Model, id=userid)
                obj.actype = 'Spam Account'
                obj.Reason = 'Tweeted with Volgar Word'

                obj.save(update_fields=['actype', 'Reason'])

        usertweets_Model.objects.create(userId=userObj,uname=uname ,tcity=tcity1 ,uses=uses, tdesc=cmd, topics=result, sanalysis=se,
                                        senderstatus='process',names=tname)


    return render(request,'RUser/Post_Tweet.html', {'objc':username,'tloc':tcity,'result': result, 'se': se})

def ViewAllTweets(request):
    userid = request.session['userid']
    obj = usertweets_Model.objects.all()

    return render(request,'RUser/ViewAllTweets.html',{'list_objects': obj})

def Viewreviews(request):

    obj = review_Model.objects.all()

    return render(request,'RUser/Viewreviews.html',{'list_objects': obj})




def ratings(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = usertweets_Model.objects.get(id=pk)
    unid = objs.id
    vot_count = usertweets_Model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.ratings
        vott1 = vott + 1
        obj = get_object_or_404(usertweets_Model, id=unid)
        obj.ratings = vott1
        obj.save(update_fields=["ratings"])
        return redirect('ViewAllTweets')

    return render(request,'RUser/ratings.html',{'objs':vott1})


def dislikes(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = usertweets_Model.objects.get(id=pk)
    unid = objs.id
    vot_count = usertweets_Model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.dislikes
        vott1 = vott - 1
        obj = get_object_or_404(usertweets_Model, id=unid)
        obj.dislikes = vott1
        obj.save(update_fields=["dislikes"])
        return redirect('ViewAllTweets')
    return render(request,'RUser/dislikes.html',{'objs':vott1})



def ViewTrending(request):
    topic = usertweets_Model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return render(request, 'RUser/ViewTrending.html', {'objects': topic})