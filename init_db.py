import sqlite3

conn = sqlite3.connect('db/schemes.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS schemes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    language TEXT,
    keywords TEXT,
    eligibility TEXT,
    documents TEXT,
    steps TEXT,
    contact TEXT,
    video_url TEXT,
    apply_links TEXT
)
''')

# Sample data: Hindi and Telugu (plus all languages for Aadhar Card with video)
schemes = [
    # Aadhaar Card (all languages)
    ('Aadhar Card', 'hi', 'aadhar,आधार', 'भारतीय नागरिक', 'पहचान और निवास प्रमाण', 'आधार केंद्र पर जाएं या ऑनलाइन आवेदन करें', 'टोल फ्री: 1947', 'https://www.youtube.com/watch?v=ld-aM5DPVj8', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'te', 'aadhar,ఆధార్', 'భారతీయ పౌరుడు', 'ఒక గుర్తింపు మరియు నివాస రుజువు', 'ఆధార్ కేంద్రాన్ని సందర్శించండి లేదా ఆన్‌లైన్‌లో దరఖాస్తు చేయండి', 'టోల్ ఫ్రీ: 1947', 'https://www.youtube.com/watch?v=yJEXuiabE0s', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'bn', 'aadhar,আধার', 'ভারতীয় নাগরিক', 'পরিচয় এবং ঠিকানার প্রমাণ', 'আধার কেন্দ্র যান বা অনলাইনে আবেদন করুন', 'টোল ফ্রি: 1947', 'https://www.youtube.com/watch?v=SyZ1PKtvHWI', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'mr', 'aadhar,आधार', 'भारतीय नागरिक', 'ओळख आणि निवासाचा पुरावा', 'आधार केंद्रात जा किंवा ऑनलाइन अर्ज करा', 'टोल फ्री: 1947', 'https://www.youtube.com/watch?v=cShZPApQ51k', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'ta', 'aadhar,ஆதார்', 'இந்திய குடிமகன்', 'அடையாளம் மற்றும் முகவரி சான்று', 'ஆதார் மையத்திற்கு செல்லவும் அல்லது ஆன்லைனில் விண்ணப்பிக்கவும்', 'டோல் ஃப்ரீ: 1947', 'https://www.youtube.com/watch?v=AhbqgdArjbg', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'gu', 'aadhar,આધાર', 'ભારતીય નાગરિક', 'ઓળખ અને રહેઠાણ પુરાવો', 'આધાર કેન્દ્ર પર જાઓ અથવા ઓનલાઈન અરજી કરો', 'ટોલ ફ્રી: 1947', 'https://www.youtube.com/watch?v=JkMdmcQLxas', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'kn', 'aadhar,ಆಧಾರ್', 'ಭಾರತೀಯ ನಾಗರಿಕ', 'ಗುರುತಿನ ಮತ್ತು ನಿವಾಸದ ಪುರಾವೆ', 'ಆಧಾರ್ ಕೇಂದ್ರಕ್ಕೆ ಹೋಗಿ ಅಥವಾ ಆನ್ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ', 'ಟೋಲ್ ಫ್ರೀ: 1947', 'https://www.youtube.com/watch?v=r5JYqyoMGtA', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'ml', 'aadhar,ആധാർ', 'ഇന്ത്യൻ പൗരൻ', 'അടയാളവും താമസ തെളിവും', 'ആധാർ കേന്ദ്രത്തിൽ പോകുക അല്ലെങ്കിൽ ഓൺലൈനിൽ അപേക്ഷിക്കുക', 'ടോൾ ഫ്രീ: 1947', 'https://www.youtube.com/watch?v=lsqGWiU8-C8', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'or', 'aadhar,ଆଧାର', 'ଭାରତୀୟ ନାଗରିକ', 'ପରିଚୟ ଏବଂ ବାସସ୍ଥାନ ପ୍ରମାଣ', 'ଆଧାର କେନ୍ଦ୍ରକୁ ଯାଆନ୍ତୁ କିମ୍ବା ଅନଲାଇନ୍ ଆବେଦନ କରନ୍ତୁ', 'ଟୋଲ ଫ୍ରି: 1947', 'https://www.youtube.com/watch?v=OeUiyVOxy7k', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'pa', 'aadhar,ਆਧਾਰ', 'ਭਾਰਤੀ ਨਾਗਰਿਕ', 'ਪਛਾਣ ਅਤੇ ਨਿਵਾਸ ਸਬੂਤ', 'ਆਧਾਰ କੇਂਦਰ ଜਾନ୍ତୁ ବା ଅନଲାଇନ୍ ଆବେଦନ କରନ୍ତୁ', 'ਟੋਲ ਫਰੀ: 1947', 'https://www.youtube.com/watch?v=0gsv3ghmdto', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'as', 'aadhar,আধাৰ', 'ভাৰতীয় নাগৰিক', 'পরিচয় আৰু বাসগৃহ প্ৰমাণ', 'আধাৰ কেন্দ্ৰলৈ যাওক বা অনলাইন আবেদন কৰক', 'টোল ফ্রি: 1947', 'https://www.youtube.com/watch?v=YdLJ7ZB9OG0', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'ur', 'aadhar,آدھار', 'بھارتی شہری', 'شناخت اور رہائش کا ثبوت', 'آدھار مرکز جائیں یا آن لائن درخواست دیں', 'ٹول فری: 1947', 'https://www.youtube.com/watch?v=AN5WDJfUT3I', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    ('Aadhar Card', 'en', 'aadhar,aadhar card', 'Indian citizen', 'Identity and address proof', 'Visit Aadhar center or apply online', 'Toll Free: 1947', 'https://www.youtube.com/watch?v=CdE8jB7u6f4', 'https://uidai.gov.in/enrolment-update/enrolment-by-registrars.html'),
    # PAN Card (all languages)
    ('PAN Card', 'en', 'pan,pan card', 'Indian citizen', 'Identity proof, address proof, DOB proof', 'Apply online via NSDL or UTIITSL', 'Helpline: 1800-XXXX', 'https://www.youtube.com/watch?v=pan_video', 'https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html; https://www.pan.utiitsl.com/PAN/newA.do'),
    # Ration Card (all languages)
    ('Ration Card', 'hi', 'ration,राशन', 'BPL परिवार, वैध आधार', 'आधार कार्ड, निवास प्रमाण', 'ऑनलाइन आवेदन करें या स्थानीय कार्यालय जाएं', 'टोल फ्री: 1800-XXXX', 'https://www.youtube.com/watch?v=B_9EGlW-xeI', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'te', 'ration,బియ్యం', 'బీపీఎల్ కుటుంబం, చెల్లుబాటు అయ్యే ఆధార్', 'ఆధార్ కార్డు, నివాస రుజువు', 'ఆన్‌లైన్‌లో దరఖాస్తు చేయండి లేదా స్థానిక కార్యాలయాన్ని సందర్శించండి', 'టోల్ ఫ్రీ: 1800-YYYY', 'https://www.youtube.com/watch?v=9Ww-BzpoSrk', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'bn', 'ration,রেশন', 'BPL পরিবার, বৈধ আধার', 'আধার কার্ড, ঠিকানার প্রমাণ', 'অনলাইনে আবেদন করুন বা স্থানীয় অফিসে যান', 'টোল ফ্রি: 1800-BENG', 'https://www.youtube.com/watch?v=OgjT9KQFlOk', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'mr', 'ration,रेशन', 'BPL कुटुंब, वैध आधार', 'आधार कार्ड, निवासाचा पुरावा', 'ऑनलाइन अर्ज करा किंवा कार्यालयात जा', 'टोल फ्री: 1800-MARA', 'https://www.youtube.com/watch?v=UklQIRwGb6A', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'ta', 'ration,ரேஷன்', 'BPL குடும்பம், செல்லுபடியாகும் ஆதார்', 'ஆதார் கார்டு, முகவரி சான்று', 'ஆன்லைனில் விண்ணப்பிக்கவும் அல்லது அலுவலகம் செல்லவும்', 'டோல் ஃப்ரீ: 1800-TAMI', 'https://www.youtube.com/watch?v=Zhpn7CeT3Ws', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'gu', 'ration,રેશન', 'BPL પરિવાર, માન્ય આધાર', 'આધાર કાર્ડ, રહેઠાણ પુરાવો', 'ઓનલાઇન અરજી કરો અથવા સ્થાનિક કચેરીમાં જાઓ', 'ટોલ ફ્રી: 1800-GUJA', 'https://www.youtube.com/watch?v=bkW4jijNa5I', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'kn', 'ration,ರೇಷನ್', 'BPL ಕುಟುಂಬ, ಮಾನ್ಯ ಆಧಾರ್', 'ಆಧಾರ್ ಕಾರ್ಡ್, ನಿವಾಸದ ಪುರಾವೆ', 'ಆನ್ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಅಥವಾ ಸ್ಥಳೀಯ ಕಚೇರಿಗೆ ಹೋಗಿ', 'ಟೋಲ್ ಫ್ರೀ: 1800-KANN', 'https://www.youtube.com/watch?v=_PEm4TcfU9s', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'ml', 'ration,റേഷൻ', 'BPL കുടുംബം, സാധുവായ ആധാർ', 'ആധാർ കാർഡ്, താമസ തെളിവ്', 'ഓൺലൈനിൽ അപേക്ഷിക്കാം അല്ലെങ്കിൽ പ്രാദേശിക ഓഫീസിൽ പോകാം', 'ടോൾ ഫ്രീ: 1800-MALA', 'https://www.youtube.com/watch?v=ClYrGmTWTzY', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'or', 'ration,ରାସନ', 'BPL ପରିବାର, ବୈଧ ଆଧାର', 'ଆଧାର କାର୍ଡ, ବାସସ୍ଥାନ ପ୍ରମାଣ', 'ଅନଲାଇନ୍ ଆବେଦନ କରନ୍ତୁ କିମ୍ବା ସ୍ଥାନୀୟ କାର୍ଯ୍ୟାଳୟକୁ ଯାଆନ୍ତୁ', 'ଟୋଲ ଫ୍ରି: 1800-ODIA', 'https://www.youtube.com/watch?v=sBIclndANoI', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'pa', 'ration,ਰਾਸ਼ਨ', 'BPL ਪਰਿਵਾਰ, ਵੈਧ ਆਧਾਰ', 'ਆਧਾਰ ਕਾਰਡ, ਨਿਵਾਸ ਸਬੂਤ', 'ਆਨਲਾਈਨ ਅਰਜ਼ੀ ਦਿਓ ਜਾਂ ਸਥਾਨਕ ਦਫ਼ਤਰ ਜਾਓ', 'ਟੋਲ ਫਰੀ: 1800-PUNJ', 'https://www.youtube.com/watch?v=9UOONu12U7I', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'as', 'ration,ৰেচন', 'BPL পৰিয়াল, বৈধ আধাৰ', 'আধাৰ কাৰ্ড, বাসগৃহ প্ৰমাণ', 'অনলাইন আবেদন কৰক বা স্থানীয় কাৰ্যালয়লৈ যাওক', 'টোল ফ্রি: 1800-ASSA', 'https://www.youtube.com/watch?v=6hTDfJbLbi8', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'ur', 'ration,راشن', 'BPL خاندان، درست آدھار', 'آدھار کارڈ، رہائش کا ثبوت', 'آن لائن درخواست دیں یا مقامی دفتر جائیں', 'ٹول فری: 1800-URDU', 'https://www.youtube.com/watch?v=NGS-iLvMDrM', 'https://nfsa.gov.in/portal/apply_ration_card'),
    ('Ration Card', 'en', 'ration,ration card', 'BPL family, valid Aadhar', 'Aadhar card, residence proof', 'Apply online or visit local office', 'Toll Free: 1800-ENGL', 'https://www.youtube.com/watch?v=TD1l4pcaYpI', 'https://nfsa.gov.in/portal/apply_ration_card'),
    # Pension (all languages)
    ('Pension', 'hi', 'pension,पेंशन', '60 वर्ष से ऊपर, निवासी', 'आधार कार्ड, आय प्रमाण', 'ऑनलाइन आवेदन या कार्यालय', 'हेल्पलाइन: 1800-ZZZZ', 'https://www.youtube.com/watch?v=2e7ZpPyE3zk', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'te', 'pension,పెన్షన్', '60 ఏళ్లు పైబడిన వారు, నివాసి', 'ఆధార్, ఆదాయ రుజువు', 'ఆన్‌లైన్‌లో దరఖాస్తు చేయండి లేదా కార్యాలయం', 'హెల్ప్‌లైన్: 1800-AAAA', 'https://www.youtube.com/watch?v=jslFQLLJVIo', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'bn', 'pension,পেনশন', '৬০ বছরের ঊর্ধ্বে, বাসিন্দা', 'আধার কার্ড, আয়ের প্রমাণ', 'অনলাইনে আবেদন করুন বা অফিসে যান', 'হেল্পলাইন: 1800-BENG', 'https://www.youtube.com/watch?v=8FEpiAWb8oM', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'mr', 'pension,पेंशन', '६० वर्षांवरील, रहिवासी', 'आधार कार्ड, उत्पन्नाचा पुरावा', 'ऑनलाइन अर्ज करा किंवा कार्यालयात जा', 'हेल्पलाइन: 1800-MARA', 'https://www.youtube.com/watch?v=SaLjvjbEdNI', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'ta', 'pension,பென்ஷன்', '60 வயதுக்கு மேற்பட்டவர்கள், குடியிருப்பாளர்', 'ஆதார் கார்டு, வருமான சான்று', 'ஆன்லைனில் விண்ணப்பிக்கவும் அல்லது அலுவலகம் செல்லவும்', 'ஹெல்ப்லைன்: 1800-TAMI', 'https://www.youtube.com/watch?v=nXhzPMgJmX0', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'gu', 'pension,પેન્શન', '60 વર્ષથી ઉપર, રહેવાસી', 'આધાર કાર્ડ, આવક પુરાવો', 'ઓનલાઇન અરજી કરો અથવા કચેરીમાં જાઓ', 'હેલ્પલાઇન: 1800-GUJA', 'https://www.youtube.com/watch?v=QxQYtCGQIXM', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'kn', 'pension,ಪಿಂಚಣಿ', '60 ವರ್ಷ ಮೇಲ್ಪಟ್ಟವರು, ನಿವಾಸಿ', 'ಆಧಾರ್ ಕಾರ್ಡ್, ಆದಾಯದ ಪುರಾವೆ', 'ಆನ್ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಅಥವಾ ಕಚೇರಿಗೆ ಹೋಗಿ', 'ಹೆಲ್ಪ್‌ಲೈನ್: 1800-KANN', 'https://www.youtube.com/watch?v=J9rsx7v4J5s', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'ml', 'pension,പെൻഷൻ', '60 വയസ്സിന് മുകളിൽ, താമസക്കാരൻ', 'ആധാർ കാർഡ്, വരുമാന തെളിവ്', 'ഓൺലൈനിൽ അപേക്ഷിക്കാം അല്ലെങ്കിൽ ഓഫീസിൽ പോകാം', 'ഹെൽപ്‌ലൈൻ: 1800-MALA', 'https://www.youtube.com/watch?v=RGmZc_QKvYw', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'or', 'pension,ପେନ୍ସନ୍', '60 ବର୍ଷ ଉପରେ, ବାସିନ୍ଦା', 'ଆଧାର କାର୍ଡ, ଆୟ ପ୍ରମାଣ', 'ଅନଲାଇନ୍ ଆବେଦନ କରନ୍ତୁ କିମ୍ବା କାର୍ଯ୍ୟାଳୟକୁ ଯାଆନ୍ତୁ', 'ହେଲ୍ପଲାଇନ୍: 1800-ODIA', 'https://www.youtube.com/watch?v=88_9RYRpPHg', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'pa', 'pension,ਪੈਨਸ਼ਨ', '60 ਸਾਲ ਤੋਂ ਉੱਪਰ, ਨਿਵਾਸੀ', 'ਆਧਾਰ ਕਾਰਡ, ਆਮਦਨ ਸਬੂਤ', 'ਆਨਲਾਈਨ ਅਰਜ਼ੀ ਦਿਓ ਜਾਂ ਦਫ਼ਤਰ ਜਾਓ', 'ਹੈਲਪਲਾਈਨ: 1800-PUNJ', 'https://www.youtube.com/watch?v=dK99nozOVDk', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'as', 'pension,পেঞ্চন', '৬০ বছৰৰ ওপৰ, বাসিন্দা', 'আধাৰ কাৰ্ড, আয়ৰ প্ৰমাণ', 'অনলাইন আবেদন কৰক বা কাৰ্যালয়লৈ যাওক', 'হেল্পলাইন: 1800-ASSA', 'https://www.youtube.com/watch?v=h4Bh-k57ma4', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'ur', 'pension,پنشن', '60 سال سے زیادہ عمر، رہائشی', 'آدھار کارڈ، آمدنی کا ثبوت', 'آن لائن درخواست دیں یا دفتر جائیں', 'ہیلپ لائن: 1800-URDU', 'https://www.youtube.com/watch?v=1_AvGlGjSG0', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
    ('Pension', 'en', 'pension,pension', 'Above 60 years, resident', 'Aadhar card, income proof', 'Apply online or at office', 'Helpline: 1800-ENGL', 'https://www.youtube.com/watch?v=aWyflNm33B4', 'https://pensionersportal.gov.in/; https://dotpension.gov.in/; https://jeevanpramaan.gov.in/; https://www.pensionseva.sbi/; https://mis.epfindia.gov.in/PensionPaymentEnquiry/pensionStatus.jsp'),
]

c.executemany('''
INSERT INTO schemes (name, language, keywords, eligibility, documents, steps, contact, video_url, apply_links)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', schemes)

conn.commit()
conn.close() 