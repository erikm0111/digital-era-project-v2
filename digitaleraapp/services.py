from .phonenumberextractor import PhoneNumberExtractor
from .emailextractor import EmailExtractor

class WebsiteAnalyzerService(object):
    @staticmethod
    def analyzeUrl(url):
        phoneNumbersExtractor = PhoneNumberExtractor()
        emailsExtractor = EmailExtractor()
        phoneNumbers = phoneNumbersExtractor.extract_phone_numbers(url)
        emails = emailsExtractor.extract_emails(url)
        return phoneNumbers, emails
