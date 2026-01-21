# =========================================================
# IDARVIZHI — MULTILINGUAL CONFIG (FINAL)
# =========================================================

COMMON_KEYS = {

    # language
    "select_language": "",

    # sidebar
    "select_state": "",
    "select_district": "",
    "select_year": "",
    "select_disaster": "",

    # sections
    "risk_summary": "",
    "risk_analysis": "",
    "environment_simulation": "",
    "district_map": "",
    "ai_report": "",
    "chatbot": "",

    # map
    "choose_map_style": "",

    # chatbot
    "ask_question": "",
    "ai_assistant": "",
    "ai_perspective": "",
    "structured_guidance": "",
    "sources": "",

    # risk
    "overall_risk": "",
    "high": "",
    "medium": "",
    "low": "",

    # actions
    "download_pdf": "",
    "voice_alert": "",

    # analysis
    "risk_factor_analysis": "",
    "analysis_complete": "",

    # metrics
    "temperature": "",
    "humidity": "",
    "rainfall": "",
    "wind_speed": "",
    "pressure": "",
    "river_level": "",
    "population_density": "",
    "hospital_access": "",
    "evacuation_index": "",
    "severity_index": ""
}


translations = {

# =========================================================
# ENGLISH
# =========================================================
"English": {
    **COMMON_KEYS,
    "select_language":"Language",
    "select_state":"Select State",
    "select_district":"Select District",
    "select_year":"Select Year",
    "select_disaster":"Select Disaster Type",

    "risk_summary":"Real-Time Risk Summary",
    "risk_analysis":"Risk Factor Analysis",
    "environment_simulation":"Live Environmental Risk Simulation",
    "district_map":"Live District Risk Map",

    "ai_report":"AI Situation Report",
    "chatbot":"Disaster Assistant",

    "choose_map_style":"Choose Map Style",

    "ask_question":"Ask your disaster question",
    "ai_assistant":"Disaster Assistant",
    "ai_perspective":"AI Perspective",
    "structured_guidance":"Structured Guidance",
    "sources":"Sources",

    "overall_risk":"Overall Risk",
    "high":"High",
    "medium":"Medium",
    "low":"Low",

    "download_pdf":"Download AI Report PDF",
    "voice_alert":"Auto Disaster Voice Alert",

    "risk_factor_analysis":"Risk Factor Analysis",
    "analysis_complete":"Risk factor analysis completed!",

    "temperature":"Temperature (°C)",
    "humidity":"Humidity (%)",
    "rainfall":"Rainfall (mm)",
    "wind_speed":"Wind Speed (km/h)",
    "pressure":"Pressure (hPa)",
    "river_level":"River Level (m)",
    "population_density":"Population / km²",
    "hospital_access":"Hospital Access",
    "evacuation_index":"Evacuation Index",
    "severity_index":"Composite Disaster Severity Index"
},

# =========================================================
# TAMIL
# =========================================================
"Tamil": {
    **COMMON_KEYS,
    "select_language":"மொழி",
    "select_state":"மாநிலத்தை தேர்வு செய்க",
    "select_district":"மாவட்டத்தை தேர்வு செய்க",
    "select_year":"ஆண்டை தேர்வு செய்க",
    "select_disaster":"பேரிடர் வகை",

    "risk_summary":"நேரடி ஆபத்து சுருக்கம்",
    "risk_analysis":"ஆபத்து காரண பகுப்பாய்வு",
    "environment_simulation":"சுற்றுச்சூழல் ஆபத்து மாதிரி",
    "district_map":"மாவட்ட ஆபத்து வரைபடம்",

    "ai_report":"AI நிலை அறிக்கை",
    "chatbot":"பேரிடர் உதவியாளர்",

    "choose_map_style":"வரைபட வடிவத்தை தேர்வு செய்க",

    "ask_question":"உங்கள் பேரிடர் கேள்வியை கேளுங்கள்",
    "ai_assistant":"பேரிடர் உதவியாளர்",
    "ai_perspective":"AI பார்வை",
    "structured_guidance":"கட்டமைக்கப்பட்ட வழிகாட்டல்",
    "sources":"மூலங்கள்",

    "overall_risk":"மொத்த ஆபத்து",
    "high":"உயர்",
    "medium":"மத்திய",
    "low":"குறைவு",

    "download_pdf":"PDF அறிக்கை பதிவிறக்கம்",
    "voice_alert":"குரல் எச்சரிக்கை",

    "risk_factor_analysis":"ஆபத்து பகுப்பாய்வு",
    "analysis_complete":"ஆபத்து பகுப்பாய்வு முடிந்தது",

    "temperature":"வெப்பநிலை (°C)",
    "humidity":"ஈரப்பதம் (%)",
    "rainfall":"மழை (மிமீ)",
    "wind_speed":"காற்று வேகம் (கிமீ/ம)",
    "pressure":"அழுத்தம் (hPa)",
    "river_level":"ஆறு நீர்மட்டம் (மீ)",
    "population_density":"மக்கள் அடர்த்தி",
    "hospital_access":"மருத்துவ வசதி",
    "evacuation_index":"வெளியேற்ற குறியீடு",
    "severity_index":"மொத்த பேரிடர் தீவிரம்"
},

# =========================================================
# HINDI
# =========================================================
"Hindi": {
    **COMMON_KEYS,
    "select_language":"भाषा",
    "select_state":"राज्य चुनें",
    "select_district":"जिला चुनें",
    "select_year":"वर्ष चुनें",
    "select_disaster":"आपदा प्रकार",

    "risk_summary":"वास्तविक समय जोखिम सारांश",
    "risk_analysis":"जोखिम विश्लेषण",
    "environment_simulation":"पर्यावरणीय जोखिम सिमुलेशन",
    "district_map":"जिला जोखिम मानचित्र",

    "ai_report":"AI स्थिति रिपोर्ट",
    "chatbot":"आपदा सहायक",

    "choose_map_style":"मानचित्र शैली चुनें",

    "ask_question":"अपना आपदा प्रश्न पूछें",
    "ai_assistant":"आपदा सहायक",
    "ai_perspective":"AI दृष्टिकोण",
    "structured_guidance":"संरचित मार्गदर्शन",
    "sources":"स्रोत",

    "overall_risk":"कुल जोखिम",
    "high":"उच्च",
    "medium":"मध्यम",
    "low":"कम",

    "download_pdf":"PDF रिपोर्ट डाउनलोड",
    "voice_alert":"वॉइस अलर्ट",

    "risk_factor_analysis":"जोखिम विश्लेषण",
    "analysis_complete":"जोखिम विश्लेषण पूर्ण हुआ",

    "temperature":"तापमान (°C)",
    "humidity":"आर्द्रता (%)",
    "rainfall":"वर्षा (मिमी)",
    "wind_speed":"पवन गति (किमी/घं)",
    "pressure":"दाब (hPa)",
    "river_level":"नदी स्तर (मी)",
    "population_density":"जनसंख्या घनत्व",
    "hospital_access":"अस्पताल सुविधा",
    "evacuation_index":"निकासी सूचकांक",
    "severity_index":"आपदा तीव्रता सूचकांक"
},

# =========================================================
# TELUGU
# =========================================================
"Telugu": {
    **COMMON_KEYS,
    "select_language":"భాష",
    "select_state":"రాష్ట్రాన్ని ఎంచుకోండి",
    "select_district":"జిల్లాను ఎంచుకోండి",
    "select_year":"సంవత్సరం ఎంచుకోండి",
    "select_disaster":"విపత్తు రకం",

    "risk_summary":"ప్రత్యక్ష ప్రమాద సంగ్రహం",
    "risk_analysis":"ప్రమాద విశ్లేషణ",
    "environment_simulation":"పర్యావరణ ప్రమాద అనుకరణ",
    "district_map":"జిల్లా ప్రమాద మ్యాప్",

    "ai_report":"AI నివేదిక",
    "chatbot":"విపత్తు సహాయకుడు",

    "choose_map_style":"మ్యాప్ శైలి ఎంచుకోండి",

    "ask_question":"మీ విపత్తు ప్రశ్న అడగండి",
    "ai_assistant":"విపత్తు సహాయకుడు",
    "ai_perspective":"AI దృష్టికోణం",
    "structured_guidance":"సంఘటిత మార్గదర్శనం",
    "sources":"మూలాలు",

    "overall_risk":"మొత్తం ప్రమాదం",
    "high":"అధిక",
    "medium":"మధ్యస్థ",
    "low":"తక్కువ",

    "download_pdf":"PDF నివేదిక",
    "voice_alert":"వాయిస్ అలర్ట్",

    "risk_factor_analysis":"ప్రమాద విశ్లేషణ",
    "analysis_complete":"విశ్లేషణ పూర్తైంది",

    "temperature":"ఉష్ణోగ్రత (°C)",
    "humidity":"తేమ (%)",
    "rainfall":"వర్షపాతం (మిమీ)",
    "wind_speed":"గాలి వేగం (కిమీ/గం)",
    "pressure":"పీడనం (hPa)",
    "river_level":"నది మట్టం (మీ)",
    "population_density":"జనసాంద్రత",
    "hospital_access":"ఆసుపత్రి ప్రాప్తి",
    "evacuation_index":"తప్పించుకునే సూచిక",
    "severity_index":"ప్రమాద తీవ్రత సూచిక"
},
"Kannada": {
    **COMMON_KEYS,

    "select_language": "ಭಾಷೆ",
    "select_state": "ರಾಜ್ಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    "select_district": "ಜಿಲ್ಲೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    "select_year": "ವರ್ಷ ಆಯ್ಕೆಮಾಡಿ",
    "select_disaster": "ವಿಪತ್ತು ಪ್ರಕಾರ ಆಯ್ಕೆಮಾಡಿ",

    "risk_summary": "ತಕ್ಷಣದ ಅಪಾಯ ಸಾರಾಂಶ",
    "risk_analysis": "ಅಪಾಯ ಕಾರಣ ವಿಶ್ಲೇಷಣೆ",
    "environment_simulation": "ಪರಿಸರ ಅಪಾಯ ಅನುಕರಣೆ",
    "district_map": "ಜಿಲ್ಲಾ ಅಪಾಯ ನಕ್ಷೆ",

    "ai_report": "AI ವರದಿ",
    "chatbot": "ವಿಪತ್ತು ಸಹಾಯಕ",

    "choose_map_style": "ನಕ್ಷೆ ಶೈಲಿ ಆಯ್ಕೆಮಾಡಿ",

    "ask_question": "ನಿಮ್ಮ ವಿಪತ್ತು ಪ್ರಶ್ನೆಯನ್ನು ಕೇಳಿ",
    "ai_assistant": "ವಿಪತ್ತು ಸಹಾಯಕ",
    "ai_perspective": "AI ದೃಷ್ಟಿಕೋನ",
    "structured_guidance": "ಸಂರಚಿತ ಮಾರ್ಗದರ್ಶನ",
    "sources": "ಮೂಲಗಳು",

    "overall_risk": "ಒಟ್ಟು ಅಪಾಯ",
    "high": "ಹೆಚ್ಚು",
    "medium": "ಮಧ್ಯಮ",
    "low": "ಕಡಿಮೆ",

    "download_pdf": "PDF ಡೌನ್‌ಲೋಡ್",
    "voice_alert": "ಧ್ವನಿ ಎಚ್ಚರಿಕೆ",

    "risk_factor_analysis": "ಅಪಾಯ ವಿಶ್ಲೇಷಣೆ",
    "analysis_complete": "ಅಪಾಯ ವಿಶ್ಲೇಷಣೆ ಪೂರ್ಣವಾಯಿತು",

    "temperature": "ತಾಪಮಾನ (°C)",
    "humidity": "ಆರ್ದ್ರತೆ (%)",
    "rainfall": "ಮಳೆ (ಮಿಮೀ)",
    "wind_speed": "ಗಾಳಿಯ ವೇಗ (ಕಿಮೀ/ಗಂ)",
    "pressure": "ಒತ್ತಡ (hPa)",
    "river_level": "ನದಿ ಮಟ್ಟ (ಮೀ)",
    "population_density": "ಜನಸಂಖ್ಯೆ ಸಾಂದ್ರತೆ",
    "hospital_access": "ಆಸ್ಪತ್ರೆ ಪ್ರವೇಶ",
    "evacuation_index": "ಸ್ಥಳಾಂತರ ಸೂಚ್ಯಂಕ",
    "severity_index": "ವಿಪತ್ತು ತೀವ್ರತಾ ಸೂಚ್ಯಂಕ"
},
"Malayalam": {
    **COMMON_KEYS,

    "select_language": "ഭാഷ",
    "select_state": "സംസ്ഥാനം തിരഞ്ഞെടുക്കുക",
    "select_district": "ജില്ല തിരഞ്ഞെടുക്കുക",
    "select_year": "വർഷം തിരഞ്ഞെടുക്കുക",
    "select_disaster": "ദുരന്ത തരം തിരഞ്ഞെടുക്കുക",

    "risk_summary": "തത്സമയ അപകട സംഗ്രഹം",
    "risk_analysis": "അപകട കാരണ വിശകലനം",
    "environment_simulation": "പരിസ്ഥിതി അപകട അനുകരണം",
    "district_map": "ജില്ലാ അപകട മാപ്പ്",

    "ai_report": "AI റിപ്പോർട്ട്",
    "chatbot": "ദുരന്ത സഹായി",

    "choose_map_style": "മാപ്പ് ശൈലി തിരഞ്ഞെടുക്കുക",

    "ask_question": "നിങ്ങളുടെ ദുരന്ത ചോദ്യം ചോദിക്കുക",
    "ai_assistant": "ദുരന്ത സഹായി",
    "ai_perspective": "AI കാഴ്ചപ്പാട്",
    "structured_guidance": "ഘടനാപരമായ മാർഗനിർദേശം",
    "sources": "ഉറവിടങ്ങൾ",

    "overall_risk": "ആകെ അപകടം",
    "high": "ഉയർന്ന",
    "medium": "മധ്യം",
    "low": "കുറവ്",

    "download_pdf": "PDF ഡൗൺലോഡ്",
    "voice_alert": "വോയിസ് അലർട്ട്",

    "risk_factor_analysis": "അപകട വിശകലനം",
    "analysis_complete": "വിശകലനം പൂർത്തിയായി",

    "temperature": "താപനില (°C)",
    "humidity": "ആർദ്രത (%)",
    "rainfall": "മഴ (മിമീ)",
    "wind_speed": "കാറ്റിന്റെ വേഗം (കിമീ/മ)",
    "pressure": "മർദ്ദം (hPa)",
    "river_level": "നദി നില (മീ)",
    "population_density": "ജനസാന്ദ്രത",
    "hospital_access": "ആശുപത്രി ലഭ്യത",
    "evacuation_index": "ഒഴിപ്പിക്കൽ സൂചിക",
    "severity_index": "ദുരന്ത തീവ്രത സൂചിക"
},
"Marathi": {
    **COMMON_KEYS,

    "select_language": "भाषा",
    "select_state": "राज्य निवडा",
    "select_district": "जिल्हा निवडा",
    "select_year": "वर्ष निवडा",
    "select_disaster": "आपत्ती प्रकार निवडा",

    "risk_summary": "थेट धोका सारांश",
    "risk_analysis": "धोका विश्लेषण",
    "environment_simulation": "पर्यावरण धोका अनुकरण",
    "district_map": "जिल्हा धोका नकाशा",

    "ai_report": "AI अहवाल",
    "chatbot": "आपत्ती सहाय्यक",

    "choose_map_style": "नकाशा शैली निवडा",

    "ask_question": "आपला आपत्ती प्रश्न विचारा",
    "ai_assistant": "आपत्ती सहाय्यक",
    "ai_perspective": "AI दृष्टीकोन",
    "structured_guidance": "संरचित मार्गदर्शन",
    "sources": "स्रोत",

    "overall_risk": "एकूण धोका",
    "high": "उच्च",
    "medium": "मध्यम",
    "low": "कमी",

    "download_pdf": "PDF डाउनलोड",
    "voice_alert": "व्हॉइस अलर्ट",

    "risk_factor_analysis": "धोका विश्लेषण",
    "analysis_complete": "विश्लेषण पूर्ण झाले",

    "temperature": "तापमान (°C)",
    "humidity": "आर्द्रता (%)",
    "rainfall": "पर्जन्यमान (मिमी)",
    "wind_speed": "वाऱ्याचा वेग (किमी/ता)",
    "pressure": "दाब (hPa)",
    "river_level": "नदी पातळी (मी)",
    "population_density": "लोकसंख्या घनता",
    "hospital_access": "रुग्णालय प्रवेश",
    "evacuation_index": "स्थलांतर निर्देशांक",
    "severity_index": "आपत्ती तीव्रता निर्देशांक"
},
"Bengali": {
    **COMMON_KEYS,

    "select_language": "ভাষা",
    "select_state": "রাজ্য নির্বাচন করুন",
    "select_district": "জেলা নির্বাচন করুন",
    "select_year": "বছর নির্বাচন করুন",
    "select_disaster": "দুর্যোগের ধরন নির্বাচন করুন",

    "risk_summary": "তাৎক্ষণিক ঝুঁকি সারসংক্ষেপ",
    "risk_analysis": "ঝুঁকি বিশ্লেষণ",
    "environment_simulation": "পরিবেশগত ঝুঁকি অনুকরণ",
    "district_map": "জেলা ঝুঁকি মানচিত্র",

    "ai_report": "AI প্রতিবেদন",
    "chatbot": "দুর্যোগ সহকারী",

    "choose_map_style": "মানচিত্র শৈলী নির্বাচন করুন",

    "ask_question": "আপনার দুর্যোগ প্রশ্ন জিজ্ঞাসা করুন",
    "ai_assistant": "দুর্যোগ সহকারী",
    "ai_perspective": "AI দৃষ্টিভঙ্গি",
    "structured_guidance": "গঠিত নির্দেশনা",
    "sources": "উৎস",

    "overall_risk": "মোট ঝুঁকি",
    "high": "উচ্চ",
    "medium": "মধ্যম",
    "low": "কম",

    "download_pdf": "PDF ডাউনলোড",
    "voice_alert": "ভয়েস সতর্কতা",

    "risk_factor_analysis": "ঝুঁকি বিশ্লেষণ",
    "analysis_complete": "বিশ্লেষণ সম্পন্ন হয়েছে",

    "temperature": "তাপমাত্রা (°C)",
    "humidity": "আর্দ্রতা (%)",
    "rainfall": "বৃষ্টিপাত (মিমি)",
    "wind_speed": "বাতাসের গতি (কিমি/ঘ)",
    "pressure": "চাপ (hPa)",
    "river_level": "নদীর স্তর (মি)",
    "population_density": "জনসংখ্যা ঘনত্ব",
    "hospital_access": "হাসপাতাল সুবিধা",
    "evacuation_index": "উচ্ছেদ সূচক",
    "severity_index": "দুর্যোগ তীব্রতা সূচক"
},
"Gujarati": {
    **COMMON_KEYS,

    "select_language": "ભાષા",
    "select_state": "રાજ્ય પસંદ કરો",
    "select_district": "જિલ્લો પસંદ કરો",
    "select_year": "વર્ષ પસંદ કરો",
    "select_disaster": "આપત્તિ પ્રકાર પસંદ કરો",

    "risk_summary": "તાત્કાલિક જોખમ સારાંશ",
    "risk_analysis": "જોખમ વિશ્લેષણ",
    "environment_simulation": "પર્યાવરણીય જોખમ અનુસંધાન",
    "district_map": "જિલ્લા જોખમ નકશો",

    "ai_report": "AI અહેવાલ",
    "chatbot": "આપત્તિ સહાયક",

    "choose_map_style": "નકશા શૈલી પસંદ કરો",

    "ask_question": "તમારો આપત્તિ પ્રશ્ન પૂછો",
    "ai_assistant": "આપત્તિ સહાયક",
    "ai_perspective": "AI દૃષ્ટિકોણ",
    "structured_guidance": "રચનાત્મક માર્ગદર્શન",
    "sources": "સ્ત્રોત",

    "overall_risk": "કુલ જોખમ",
    "high": "ઉચ્ચ",
    "medium": "મધ્યમ",
    "low": "નિમ્ન",

    "download_pdf": "PDF ડાઉનલોડ",
    "voice_alert": "વોઇસ એલર્ટ",

    "risk_factor_analysis": "જોખમ વિશ્લેષણ",
    "analysis_complete": "વિશ્લેષણ પૂર્ણ થયું",

    "temperature": "તાપમાન (°C)",
    "humidity": "આર્દ્રતા (%)",
    "rainfall": "વરસાદ (મિમી)",
    "wind_speed": "પવન ગતિ (કિમી/ક)",
    "pressure": "દબાણ (hPa)",
    "river_level": "નદી સ્તર (મી)",
    "population_density": "વસ્તી ઘનતા",
    "hospital_access": "હોસ્પિટલ સુલભતા",
    "evacuation_index": "ખાલી કરવાના સૂચકાંક",
    "severity_index": "આપત્તિ તીવ્રતા સૂચકાંક"
},
"Punjabi": {
    **COMMON_KEYS,

    "select_language": "ਭਾਸ਼ਾ",
    "select_state": "ਰਾਜ ਚੁਣੋ",
    "select_district": "ਜ਼ਿਲ੍ਹਾ ਚੁਣੋ",
    "select_year": "ਸਾਲ ਚੁਣੋ",
    "select_disaster": "ਆਫ਼ਤ ਦੀ ਕਿਸਮ ਚੁਣੋ",

    "risk_summary": "ਤੁਰੰਤ ਜੋਖਮ ਸਾਰ",
    "risk_analysis": "ਜੋਖਮ ਵਿਸ਼ਲੇਸ਼ਣ",
    "environment_simulation": "ਵਾਤਾਵਰਣ ਜੋਖਮ ਅਨੁਕਰਨ",
    "district_map": "ਜ਼ਿਲ੍ਹਾ ਜੋਖਮ ਨਕਸ਼ਾ",

    "ai_report": "AI ਰਿਪੋਰਟ",
    "chatbot": "ਆਪਦਾ ਸਹਾਇਕ",

    "choose_map_style": "ਨਕਸ਼ਾ ਸ਼ੈਲੀ ਚੁਣੋ",

    "ask_question": "ਆਪਣਾ ਆਪਦਾ ਸਵਾਲ ਪੁੱਛੋ",
    "ai_assistant": "ਆਪਦਾ ਸਹਾਇਕ",
    "ai_perspective": "AI ਦ੍ਰਿਸ਼ਟੀਕੋਣ",
    "structured_guidance": "ਸੰਰਚਿਤ ਮਾਰਗਦਰਸ਼ਨ",
    "sources": "ਸਰੋਤ",

    "overall_risk": "ਕੁੱਲ ਜੋਖਮ",
    "high": "ਉੱਚ",
    "medium": "ਮੱਧਮ",
    "low": "ਘੱਟ",

    "download_pdf": "PDF ਡਾਊਨਲੋਡ",
    "voice_alert": "ਵੌਇਸ ਅਲਰਟ",

    "risk_factor_analysis": "ਜੋਖਮ ਵਿਸ਼ਲੇਸ਼ਣ",
    "analysis_complete": "ਵਿਸ਼ਲੇਸ਼ਣ ਪੂਰਾ ਹੋਇਆ",

    "temperature": "ਤਾਪਮਾਨ (°C)",
    "humidity": "ਨਮੀ (%)",
    "rainfall": "ਵਰਖਾ (ਮਿਮੀ)",
    "wind_speed": "ਹਵਾ ਦੀ ਗਤੀ (ਕਿਮੀ/ਘੰ)",
    "pressure": "ਦਬਾਅ (hPa)",
    "river_level": "ਨਦੀ ਪੱਧਰ (ਮੀ)",
    "population_density": "ਆਬਾਦੀ ਸੰਘਣਾਪਣ",
    "hospital_access": "ਹਸਪਤਾਲ ਪਹੁੰਚ",
    "evacuation_index": "ਖਾਲੀ ਕਰਨ ਸੂਚਕ",
    "severity_index": "ਆਫ਼ਤ ਗੰਭੀਰਤਾ ਸੂਚਕ"
},
"Odia": {
    **COMMON_KEYS,

    "select_language": "ଭାଷା",
    "select_state": "ରାଜ୍ୟ ବାଛନ୍ତୁ",
    "select_district": "ଜିଲ୍ଲା ବାଛନ୍ତୁ",
    "select_year": "ବର୍ଷ ବାଛନ୍ତୁ",
    "select_disaster": "ବିପଦ ପ୍ରକାର ବାଛନ୍ତୁ",

    "risk_summary": "ତତ୍କାଳିକ ଝୁମ୍ପ ସାରାଂଶ",
    "risk_analysis": "ଝୁମ୍ପ ବିଶ୍ଳେଷଣ",
    "environment_simulation": "ପରିବେଶ ଝୁମ୍ପ ଅନୁକରଣ",
    "district_map": "ଜିଲ୍ଲା ଝୁମ୍ପ ମାନଚିତ୍ର",

    "ai_report": "AI ରିପୋର୍ଟ",
    "chatbot": "ବିପଦ ସହାୟକ",

    "choose_map_style": "ମାପ୍ ଶୈଳୀ ବାଛନ୍ତୁ",

    "ask_question": "ଆପଣଙ୍କ ବିପଦ ପ୍ରଶ୍ନ ପଚାରନ୍ତୁ",
    "ai_assistant": "ବିପଦ ସହାୟକ",
    "ai_perspective": "AI ଦୃଷ୍ଟିକୋଣ",
    "structured_guidance": "ଗଠିତ ମାର୍ଗଦର୍ଶନ",
    "sources": "ସ୍ରୋତ",

    "overall_risk": "ମୋଟ ଝୁମ୍ପ",
    "high": "ଉଚ୍ଚ",
    "medium": "ମଧ୍ୟମ",
    "low": "ନିମ୍ନ",

    "download_pdf": "PDF ଡାଉନଲୋଡ୍",
    "voice_alert": "ଭଏସ୍ ଆଲର୍ଟ",

    "risk_factor_analysis": "ଝୁମ୍ପ ବିଶ୍ଳେଷଣ",
    "analysis_complete": "ବିଶ୍ଳେଷଣ ସମ୍ପୂର୍ଣ୍ଣ",

    "temperature": "ତାପମାନ (°C)",
    "humidity": "ଆର୍ଦ୍ରତା (%)",
    "rainfall": "ବର୍ଷା (ମିମି)",
    "wind_speed": "ପବନ ଗତି (କିମି/ଘ)",
    "pressure": "ଚାପ (hPa)",
    "river_level": "ନଦୀ ସ୍ତର (ମି)",
    "population_density": "ଜନସଂଖ୍ୟା ଘନତା",
    "hospital_access": "ହସ୍ପିଟାଲ ସୁବିଧା",
    "evacuation_index": "ସ୍ଥାନାନ୍ତର ସୂଚକ",
    "severity_index": "ବିପଦ ତୀବ୍ରତା ସୂଚକ"
},
"Assamese": {
    **COMMON_KEYS,

    "select_language": "ভাষা",
    "select_state": "ৰাজ্য বাছনি কৰক",
    "select_district": "জিলা বাছনি কৰক",
    "select_year": "বৰ্ষ বাছনি কৰক",
    "select_disaster": "দুৰ্যোগৰ প্ৰকাৰ বাছনি কৰক",

    "risk_summary": "তাৎক্ষণিক ঝুঁকি সাৰাংশ",
    "risk_analysis": "ঝুঁকি বিশ্লেষণ",
    "environment_simulation": "পৰিৱেশ ঝুঁকি অনুকৰণ",
    "district_map": "জিলা ঝুঁকি মানচিত্ৰ",

    "ai_report": "AI প্ৰতিবেদন",
    "chatbot": "দুৰ্যোগ সহায়ক",

    "choose_map_style": "মানচিত্ৰ শৈলী বাছনি কৰক",

    "ask_question": "আপোনাৰ দুৰ্যোগ প্ৰশ্ন সুধক",
    "ai_assistant": "দুৰ্যোগ সহায়ক",
    "ai_perspective": "AI দৃষ্টিভংগী",
    "structured_guidance": "সংগঠিত নিৰ্দেশনা",
    "sources": "উৎস",

    "overall_risk": "মুঠ ঝুঁকি",
    "high": "উচ্চ",
    "medium": "মধ্যম",
    "low": "নিম্ন",

    "download_pdf": "PDF ডাউনলোড",
    "voice_alert": "ভয়েচ এলাৰ্ট",

    "risk_factor_analysis": "ঝুঁকি বিশ্লেষণ",
    "analysis_complete": "বিশ্লেষণ সম্পূৰ্ণ",

    "temperature": "তাপমাত্রা (°C)",
    "humidity": "আৰ্দ্ৰতা (%)",
    "rainfall": "বৰষুণ (মিমি)",
    "wind_speed": "বতাহৰ গতি (কিমি/ঘণ্টা)",
    "pressure": "চাপ (hPa)",
    "river_level": "নদীৰ স্তৰ (মি)",
    "population_density": "জনসংখ্যা ঘনত্ব",
    "hospital_access": "হাসপাতাল প্ৰৱেশ",
    "evacuation_index": "উচ্ছেদ সূচক",
    "severity_index": "দুৰ্যোগ তীব্ৰতা সূচক"
}

# =========================================================
# Remaining languages are fully filled similarly
# Kannada, Malayalam, Marathi, Bengali, Gujarati,
# Punjabi, Odia, Assamese
# (File length trimmed only in explanation — yours is complete)
# =========================================================
}
