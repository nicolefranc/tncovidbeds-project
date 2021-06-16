BODY_STR = 'Body'
SOURCE = 'Source: https://tncovidbeds.tnega.org'
ERROR_MESSAGE = 'Please check that you followed the command and try again'

LIST_DISTRICTS_RESPONSE = '''
Ariyalur - ARI
Chengalpattu - CPT
Chennai - CHN
Coimbatore - CBE
Cuddalore - CUD
Dharmapuri - DPI
Dindigul - DGL
Erode - ERD
Kallakurichi - KKI
Kancheepuram - KPM
Kanniyakumari - KKM
Karur - KAR
Krishnagiri - KGI
Madurai - MDU
Mayiladuthurai - MYD
Nagapattinam - NGP
Namakkal - NMK
Nilgiris - NLG
Perambalur - PMB
Pudukkottai - PDK
Ramanathapuram - RMD
Ranipet - RPT
Salem - SLM
Sivagangai - SVG
Tenkasi - TKS
Thanjavur - TNJ
Theni - THN
Thiruchirappalli - TRY
Thirupathur - TPT
Thiruvarur - TVR
Thoothukudi - TUT
Tirunelveli - TNV
Tiruppur - TPR
Tiruvallur - TLR
Tiruvannamalai - TVM
Vellore - VEL
Villupuram - VPM
Virudhunagar - VNR
'''

DISTRICT_CODES = ["5ea0abd3d43ec2250a483a4f", "5ea0abd4d43ec2250a483a61", "5ea0abd2d43ec2250a483a40", "5ea0abd3d43ec2250a483a4a", "5ea0abd3d43ec2250a483a50", "5ea0abd2d43ec2250a483a43", "5ea0abd3d43ec2250a483a4b", "5ea0abd2d43ec2250a483a48", "5ea0abd4d43ec2250a483a5f", "5ea0abd2d43ec2250a483a41", "5ea0abd3d43ec2250a483a5c", "5ea0abd3d43ec2250a483a4c", "5ea0abd3d43ec2250a483a5d", "5ea0abd3d43ec2250a483a56", "60901c5f2481a4362891d572", "5ea0abd3d43ec2250a483a51", "5ea0abd2d43ec2250a483a47", "5ea0abd3d43ec2250a483a49", "5ea0abd3d43ec2250a483a4e",
                  "5ea0abd3d43ec2250a483a54", "5ea0abd3d43ec2250a483a59", "5ea0abd4d43ec2250a483a63", "5ea0abd2d43ec2250a483a46", "5ea0abd3d43ec2250a483a55", "5ea0abd4d43ec2250a483a60", "5ea0abd3d43ec2250a483a53", "5ea0abd3d43ec2250a483a57", "5ea0abd3d43ec2250a483a4d", "5ea0abd4d43ec2250a483a62", "5ea0abd3d43ec2250a483a52", "5ea0abd3d43ec2250a483a5a", "5ea0abd3d43ec2250a483a5b", "5ea0abd4d43ec2250a483a5e", "5ea0abd1d43ec2250a483a3f", "5ea0abd2d43ec2250a483a44", "5ea0abd2d43ec2250a483a42", "5ea0abd2d43ec2250a483a45", "5ea0abd3d43ec2250a483a58"]

district_hash = '''
Ariyalur,5ea0abd3d43ec2250a483a4f,அரியலூர்
Chengalpattu,5ea0abd4d43ec2250a483a61,செங்கல்பட்டு
Chennai,5ea0abd2d43ec2250a483a40,சென்ன
Coimbatore,5ea0abd3d43ec2250a483a4a,கோயம்புத்தூர்
Cuddalore,5ea0abd3d43ec2250a483a50,கடலூர்
Dharmapuri,5ea0abd2d43ec2250a483a43,தர்மபுர
Dindigul,5ea0abd3d43ec2250a483a4b,திண்டுக்கல்
Erode,5ea0abd2d43ec2250a483a48,ஈரோட
Kallakurichi,5ea0abd4d43ec2250a483a5f,கள்ளக்குறிச்ச
Kancheepuram,5ea0abd2d43ec2250a483a41,காஞ்சிபுரம்
Kanniyakumari,5ea0abd3d43ec2250a483a5c,கன்னியாகுமர
Karur,5ea0abd3d43ec2250a483a4c,கரூர்
Krishnagiri,5ea0abd3d43ec2250a483a5d,கிருஷ்ணகிர
Madurai,5ea0abd3d43ec2250a483a56,மதுர
Mayiladuthurai,60901c5f2481a4362891d572,மயிலாடுதுற
Nagapattinam,5ea0abd3d43ec2250a483a51,நாகப்பட்டினம்
Namakkal,5ea0abd2d43ec2250a483a47,நாமக்கல்
Nilgiris,5ea0abd3d43ec2250a483a49,நீலகிர
Perambalur,5ea0abd3d43ec2250a483a4e,பெரம்பலூர்
Pudukkottai,5ea0abd3d43ec2250a483a54,புதுக்கோட்ட
Ramanathapuram,5ea0abd3d43ec2250a483a59,ராமநாதபுரம்
Ranipet,5ea0abd4d43ec2250a483a63,ராணிப்பேட்ட
Salem,5ea0abd2d43ec2250a483a46,சேலம்
Sivagangai,5ea0abd3d43ec2250a483a55,சிவகங்க
Tenkasi,5ea0abd4d43ec2250a483a60,தென்காச
Thanjavur,5ea0abd3d43ec2250a483a53,தஞ்சாவூர்
Theni,5ea0abd3d43ec2250a483a57,தேன
Thiruchirappalli,5ea0abd3d43ec2250a483a4d,திருச்சிராப்பள்ளி
Thirupathur,5ea0abd4d43ec2250a483a62,திருப்பத்தூர்
Thiruvarur,5ea0abd3d43ec2250a483a52,தி௫வாரூர்
Thoothukudi,5ea0abd3d43ec2250a483a5a,தூத்துக்குட
Tirunelveli,5ea0abd3d43ec2250a483a5b,திருநெல்வேல
Tiruppur,5ea0abd4d43ec2250a483a5e,திருப்பூர்
Tiruvallur,5ea0abd1d43ec2250a483a3f,திருவள்ளூர்
Tiruvannamalai,5ea0abd2d43ec2250a483a44,திருவண்ணாமலை
Vellore,5ea0abd2d43ec2250a483a42,வேலூர்
Villupuram,5ea0abd2d43ec2250a483a45,விழுப்புரம்
Virudhunagar,5ea0abd3d43ec2250a483a58,விருதுநகர்'''

DISTRICT_SHORTS = []
for district in LIST_DISTRICTS_RESPONSE.split('\n'):
    if district:
        DISTRICT_SHORTS.append(district.split(' - ')[1].strip())
