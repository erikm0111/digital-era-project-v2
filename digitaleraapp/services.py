from .phonenumberextractor import PhoneNumberExtractor

class WebsiteAnalyzerService(object):
    @staticmethod
    def analyzeUrl(url):
        extractor = PhoneNumberExtractor()
        matches = extractor.extract_phone_numbers(url)
        return matches

    def print_result(phone_nums):
        result = ', '.join(phone_nums)
        print(result)
