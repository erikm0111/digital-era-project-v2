import requests

# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started

# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed

# Populate 'pagespeed.txt' file with URLs to query against API.
class WebsiteProfiler:

    def extract_audits(self, url):
        content = [url]

        for line in content:
            x = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+line
            # x = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+line+'&strategy=mobile'
            print('Requesting ' + x)
            r = requests.get(x)
            data = r.json()

            list_report = []
            for k, v in data["lighthouseResult"]["audits"].items():
                try:
                    audit_object = {}
                    if v["id"]:
                        audit_object["id"] = v["id"]
                        # dict_report[v["id"]] = {}
                        if v["title"]:
                            audit_object["title"] = v["title"]
                            # dict_report[v["id"]]["title"] = v["title"]
                        if v["description"]:
                            audit_object["description"] = v["description"]
                            # dict_report[v["id"]]["description"] = v["description"]
                        if v["displayValue"]:
                            audit_object["displayValue"] = v["displayValue"]
                            # dict_report[v["id"]]["displayValue"] = v["displayValue"]
                        if "details" in v:
                            if "overallSavingsMs" in v["details"]:
                                audit_object["overallSavingsMs"] = v["details"]["overallSavingsMs"]
                        list_report.append(audit_object)

                except:
                    continue

            return list_report
