from digitaleraapp.business_logic.emailextractor import EmailExtractor
from digitaleraapp.business_logic.phonenumberextractor import PhoneNumberExtractor
from digitaleraapp.business_logic.website_profiler import WebsiteProfiler


class WebsiteAnalyzerService(object):
    @staticmethod
    def analyzeUrl(url):
        phoneNumbersExtractor = PhoneNumberExtractor()
        emailsExtractor = EmailExtractor()
        websiteProfiler = WebsiteProfiler()
        phoneNumbers = phoneNumbersExtractor.extract_phone_numbers(url)
        emails = emailsExtractor.extract_emails(url)
        audits = websiteProfiler.extract_audits(url)
        return phoneNumbers, emails, audits
