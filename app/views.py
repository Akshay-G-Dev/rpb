from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
quotes = [
    ["I feel that the constitution is workable, \
it is flexible, and it is strong enough to hold the country together \
both in peacetime and in wartime. Indeed, if I may say so, \
if things go wrong under the new Constitution, the reason will not be that we had a bad Constitution. \
What we will have to say is that Man was vile.", "B.R. Ambedkar"],

    ["We are Indians, firstly and lastly.", "B. R. Ambedkar"],

    ["Always aim at complete harmony of thought and word and deed. Always aim at purifying your thoughts and everything will be well.", "Mahatma Gandhi"],

    ["A country's greatness lies in its undying ideals of love and sacrifice that inspire the mothers of the race", "Sarojini Naidu"],

    ["Even if I died in the service of the nation, I would be proud of it. Every drop of my blood… will contribute to the growth \
of this nation and make it strong and dynamic.", "Indira Gandhi"],

    ["The sanctity of law can be maintained only so as long as it is the expression of the will of the people", "Bhagat Singh"],

    ["We believe in peace and peaceful development, not only for ourselves but for people all over the world", "Lal Bahadur Shastri"],

    ["Citizenship consists in the service of the country.", "Jawaharlal Nehru"],


]

messages = [
    "Let us take an oath to our mother India that we will do everything that we can for our country's prosperity. Happy Republic Day from name",
    "Thousand salutes to our freedom fighters, who gave us freedom. Let's come together and make it more prosperous and great. Happy Republic Day from name",
    "East or West, India is the best, let us strive to make it even better. Wish you all a Happy Republic Day from name ",
    "Happy republic day from name ,Today was when India's constitution was made, and we got independence in real sense. Let us respect the day",
    "Freedom has come with the sacrifices of our freedom fighters, so let's pledge to protect it. Wish you and Happy Republic Day from name",
    "Never forget our great freedom fighters sacrifices. Follow their footsteps and make our country the best in the world. Happy Republic Day from name ",
    "Enjoy your freedom, but also respect the numerous sacrifices made by our leaders. Happy Republic Day from name ",
    "We got our Freedom after a lot of struggle and sacrifices. Let us cherish our independence. Wish you a Happy Republic Day from name ",
    "As we celebrate our independence, let us free or minds from deleterious thoughts. Wish you all a Happy Republic Day from name ",
]


def home(request):
    return render(request, 'home.html', {'quotes': list(enumerate(quotes)), 'messages': list(enumerate(messages))})


def pview(request, code, codeb, name):
    referer = request.META.get('HTTP_REFERER')
    quote = list(enumerate(quotes))[code][1][0]
    quote_writer = list(enumerate(quotes))[code][1][1]
    message = list(enumerate(messages))[codeb][1].replace('name',name).strip()
    '''
    import requests

    url = "http://api.lnkiy.com/url/shortener/createrandomurl"
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    


    data = '{"longUrl":'+request.get_full_path() +',"authKey":"GiyMMcA46HK0f6WvKMvbraJwbO0S1NYA2E","expiryDate": "24-09-2024 03:26:30"}'

    resp = requests.post(url, headers=headers, data=data)
    json_data = resp.text

    print(json_data)
    #print(data['result']['shortUrl'])
    '''
    return render(request, 'index.html', {'quote': quote, 'quote_writer': quote_writer, 'message': message, 'name': name,'referer':referer})


def sample(request):
    return render(request, 'example.html')

def formed(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        
        quote_code = int(data['quote'])
        message = int(data['message'])
        name = data['name']
        
        print(f"view/{quote_code}9{message}9{name} ")
        return redirect(f"view/{quote_code}9{message}9{name} ")

        