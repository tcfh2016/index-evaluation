import scrapper
import emailreport


if __name__ == "__main__":
    index_evaluation = scrapper.Scrapper.get_evaluation()
    report = emailreport.HtmlReporter(index_evaluation)
    report.send_email()
