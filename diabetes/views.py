from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from diabetes.models import Info,Pickle
import os

import pandas as pd
#import os
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import  matplotlib.pyplot as plt
import io
import base64
import pickle




def home(request):



	return render(request,"diabetes/home.html")





def  signupuser(request):


	if request.method=="GET":


		return render(request,"diabetes/signupuser.html")

	else:

		if request.POST["password1"] == request.POST["password2"]:

			try:

				user=User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])

				user.save()

				login(request,user)
				return redirect("home")

			except IntegrityError:

				error="The user name is already takne. Try another username"
				return render(request,"diabetes/signupuser.html",{"error":error})


		else:

			error="The Password did not match"
			return render(request,"diabetes/signupuser.html",{"error":error})






def logoutuser(request):

		logout(request)

		return redirect("home")



def loginuser(request):

	if request.method == "GET":

		return render(request,"diabetes/loginuser.html")

	else:

		user=authenticate(request,username=request.POST["username"],password=request.POST["password"])

		if user is None:

			return render(request,"diabetes/loginuser.html",{"error":"password and username don't match"})


		else:
			login(request,user)
            
			return redirect("home")


def storeinsulin(request):

	if request.method=="GET":

		return render(request,"diabetes/storeinsulin.html")


	else:

        
		info=Info(user=request.user,insulin=float(request.POST["insulin"]))
		info.save()
		print(request.user)
		return redirect("home")




def analyze(request):

	data=Info.objects.filter(user=request.user).values()
	data=pd.DataFrame(data)
	data=data.drop('user_id',axis=1)
	data=data.drop('id',axis=1)
	data['created']=pd.to_datetime(data['created'],format="%d/%m/%Y")
	plt.plot(data.loc[:,'created'],data.loc[:,'insulin'],c='green')
	plt.title("TIME vs DIABETES")
	plt.xticks(rotation=90)
	plt.xlabel('Date')
	plt.ylabel('Measurement')




	buffer = io.BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek(0)
	image_png = buffer.getvalue()
	buffer.close()

	graphic = base64.b64encode(image_png)
	graphic = graphic.decode('utf-8')
	plt.clf()
	plt.cla()
	plt.close()
	

	return render(request,"diabetes/analyze.html",{"df":data.to_html(),'graphic':graphic})



def predict(request):



	if request.method=='GET':


		return render(request,"diabetes/predict.html")



	else:

		data=Pickle.objects.all()[0]


		model=pickle.load(open(data.csv.path,'rb'))
		li=[]

		li.append(request.POST['age'])
		li.append(request.POST["gender"])
		li.append(request.POST["polyuria"])
		li.append(request.POST["Polydipsia"])
		li.append(request.POST["weightloss"])
		li.append(request.POST["weakness"])
		li.append(request.POST["Polyphagia"])
		li.append(request.POST["Genital thrush"])
		li.append(request.POST["visual blurring"])
		li.append(request.POST["Itching"])
		li.append(request.POST["Irritability"])
		li.append(request.POST["delayed healing"])
		li.append(request.POST["partial paresis"])
		li.append(request.POST["muscle stiffness"])
		li.append(request.POST["Alopecia"])
		li.append(request.POST["Obesity"])

		li1=[li]
		ans=model.predict(li1)
		ans=ans[0]

		return render(request,"diabetes/suggestion.html",{"answer":ans})


























	