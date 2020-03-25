import requests

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

# Populate 'pagespeed.txt' file with URLs to query against API.
content = ['http://festino.hr']

columnTitleRow = "URL, First Contentful Paint, First Interactive, Website Images, Website Images Overall Savings ms\n"

# This is the google pagespeed api url structure, using for loop to insert each url in .txt file
for line in content:
    # If no "strategy" parameter is included, the query by default returns desktop data.
    x = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+line+'&strategy=mobile'
    print('Requesting ' + x)
    r = requests.get(x)
    final = r.json()

    try:
        urlid = final['id']
        split = urlid.split('?')  # This splits the absolute url from the api key parameter
        urlid = split[0]  # This reassigns urlid to the absolute url
        ID = 'URL ~ ' + urlid
        ID2 = str(urlid)
        urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
        FCP = 'First Contentful Paint ~ ' + str(urlfcp)
        FCP2 = str(urlfcp)
        urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
        FI = 'First Interactive ~ ' + str(urlfi)
        FI2 = str(urlfi)
        urlimages = final['lighthouseResult']['audits']['uses-webp-images']['displayValue']
        UIMG = 'Website Images ~ ' + str(urlimages)
        UIMG2 = str(urlimages)
        urlimagesMS = final['lighthouseResult']['audits']['uses-webp-images']['details']['overallSavingsMs']
        UIMGMS = 'Website Images ~ ' + str(urlimagesMS) + 'ms'
        UIMGMS2 = str(urlimagesMS) + 'ms'
    except KeyError:
        print('<KeyError> One or more keys not found ' + line)

    try:
        row = ID2 +', '+ FCP2 +', '+ FI2 + ', ' + UIMG2 +', ' + UIMGMS2 + '\n'
    except NameError:
        print('<NameError> Failing because of KeyError: ' + line)

    try:
        print(ID)
        print(FCP)
        print(FI)
        print(UIMG)
        print(UIMGMS)
    except NameError:
        print('<NameError> Failing because of KeyError: ' + line)