from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    context ={
        "articles":[
            {
            "title":"تیم کوک: به زمان بیشتری برای تکمیل ویژگی‌های سیری هوشمند نیاز داریم",
            "description":"تیم کوک می‌گوید در توسعه سیری هوشمند به پیشرفت‌هایی دست یافته‌اند.",
            "img":"https://static.digiato.com/digiato/2025/05/tim-cook-addresses-apples-delay-of-personalized-siri-features-2-910x600.jpg.webp"
        },
        {
            "title" : "شیائومی از اولین مدل هوش مصنوعی متن باز خود با قدرت استدلال و کدنویسی رونمایی کرد",
            "description":"مدل هوش مصنوعی MiMo-7B شیائومی می‌تواند در زمان کمتری تمرین ببیند و بدون افت کیفیت، سریع‌تر به درخواست‌های کاربران پاسخ دهد.",
            "img":"https://static.digiato.com/digiato/2025/05/0-910x600.jpg.webp"
        }
        ]
        ,
    }
    return render(request, "blog/home.html", context)  
def api(request):
    return(JsonResponse({"title":"hi"}))