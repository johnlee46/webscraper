import requests
from bs4 import BeautifulSoup

class pageProcessor:

    def __init__(self):
        self.request = "";

    def scrapePage(self, web_page,element_id):
        """
        Scrapes the webpage for the specified id using requests and soup
        :param web_page: url string
        :return: request result
        """
        page = requests.get(web_page)

        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id=element_id)
        #print(results.prettify())
        return results

    def findWithinScrape(self,web_page,element_id,search_class,element_type):
        """
        Finds specific element with class inside the scrape
        :param web_page: url
        :param element_id: id of the element
        :param search_class: class of the searching element
        :param element_type: type of the element, example <a> would be 'a'
        :return:
        """
        results = self.scrapePage(web_page,element_id)
        search = results.find_all(element_type,class_=search_class)
        for result_elem in search:
            print(result_elem, end='\n')



def main():
    process = pageProcessor()
    #processed = process.scrapePage("https://ca.indeed.com/jobs?q=software&l=Vancouver%2C+BC&fromage=1&sort=date","resultsCol")
    filtered = process.findWithinScrape("https://ca.indeed.com/jobs?q=software&l=Vancouver%2C+BC&fromage=1&sort=date","resultsCol","jobtitle","a")


if __name__ == '__main__':
    main()


#<div class="jobsearch-SerpJobCard unifiedRow row result clickcard" id="pj_d6b46544c1f1ac16" data-jk="d6b46544c1f1ac16" data-empn="6297244632622535" data-ci="360712613">
