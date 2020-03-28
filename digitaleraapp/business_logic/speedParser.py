# https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://theorionlabs.com
import requests




def main():
    url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://theorionlabs.com'
    data = requests.get(url).json()
    for k, v in data.items():
        try:
            for k1, v1 in v.items():
                if "audits" in k1:
                    for k2, v2 in v1.items():
                        #print(k2, v2)
                        for k3, v3 in v2.items():
                            if "id" in k3:
                                print("ID = " + v3)
                            if "title" in k3:
                                print("     title: " + v3)
                            if "description" in k3:
                                print("     description: " + v3)
                            if "displayValue" in k3:
                                print("     displayValue: " + v3)


        except:
            continue



main()



