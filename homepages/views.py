from django.shortcuts import render
import sys
# Create your views here.
#home= lambda r: render(r,'home.html')
encode_if_necessary= lambda s: s.encode('utf-8') if isinstance(s, unicode) else s

def check_captcha(data,):
    import urllib2, urllib

    params = urllib.urlencode ({
            'privatekey': encode_if_necessary(data['private_key']),
            'remoteip' :  encode_if_necessary(data['ip']),
            'challenge':  encode_if_necessary(data['challenge']),
            'response' :  encode_if_necessary(data['captcha']),
            })
    print params

    request = urllib2.Request (
            url = "http://www.google.com/recaptcha/api/verify",
            data = params,
            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "User-agent": "reCAPTCHA Python"
                }
            )        
    httpresp = urllib2.urlopen (request)
    return_values = httpresp.read ().splitlines ();
    httpresp.close();
    return 'done' if return_values [0] == 'true' else return_values [1]
        
def home(request):
    d={'public_key':'6Ld66v0SAAAAAIc4y84nUvQxKv-DuWwyLfF3qaRP',"private_key":'6Ld66v0SAAAAABNA_lwWnubYUZTIpra00ttjZu7j'}
    if request.POST:
        # get a key from https://www.google.com/recaptcha/admin/create.
        d['captcha']= request.POST['recaptcha_response_field']
        d['challenge']=request.POST['recaptcha_challenge_field']

        f = sys._getframe()
        while f:
            if 'request' in f.f_locals:
                request = f.f_locals['request']
                if request:
                    remote_ip = request.META.get('REMOTE_ADDR', '')
                    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
                    ip = remote_ip if not forwarded_ip else forwarded_ip
                    d['ip'] =ip
                    break

            f = f.f_back
        d['flag']=check_captcha(d)


    return render(request,'home.html',d)