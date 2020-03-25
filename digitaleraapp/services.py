from digitaleraapp.business_logic.emailextractor import EmailExtractor
from digitaleraapp.business_logic.phonenumberextractor import PhoneNumberExtractor


class WebsiteAnalyzerService(object):
    @staticmethod
    def analyzeUrl(url):
        phoneNumbersExtractor = PhoneNumberExtractor()
        emailsExtractor = EmailExtractor()
        phoneNumbers = phoneNumbersExtractor.extract_phone_numbers(url)
        emails = emailsExtractor.extract_emails(url)
        return phoneNumbers, emails
