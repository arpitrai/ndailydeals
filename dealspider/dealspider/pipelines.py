import os,sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import string

from dailydeals.models import DailyDeals

class DealspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name=='SgGroupOn':
            source_website_url = 'http://www.groupon.sg'
            source_website_logo = 'images/logos/singaporegroupon.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>' 
            price = item['price'][0].strip()[2:].replace(',','')
            url = item['url']
            city = 'Singapore'
            currency = 'SGD'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()

        if spider.name == 'SgBigDeal':
            source_website_url = 'http://plus.bigdeal.sg'
            source_website_logo = 'images/logos/bigdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[2:].replace(',','')
            url = source_website_url + item['url'][0].strip()
            city = 'Singapore'
            currency = 'SGD'

            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()

        if spider.name == 'SgShiokDeal':
            source_website_url = 'http://www.shiokdeal.com'
            source_website_logo = 'images/logos/shiokdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[2:].replace(',','')
            url = item['url']
            city = 'Singapore'
            currency = 'SGD'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            

        if spider.name == 'SgAllDealsAsia':
            source_website_url = 'http://www.alldealsasia.com'
            source_website_logo = 'images/logos/alldealsasia.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][1].strip()[2:].replace(',','')
            url = source_website_url + item['url'][0].strip()
            city = 'Singapore'
            currency = 'SGD'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            

        if spider.name == 'SgVoucherWow':
            source_website_url = 'http://www.voucherwow.com/cities/singapore'
            source_website_logo = 'images/logos/voucherwow.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[2:].replace(',','')
            url = 'http://www.voucherwow.com' + item['url'][0].strip()
            city = 'Singapore'
            currency = 'SGD'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            

        if spider.name == 'SgDealComSg':
            source_website_url = 'http://www.deal.com.sg'
            source_website_logo = 'images/logos/dealcomsg.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[2:].replace(',','')
            url = source_website_url + item['url'][0].strip()
            city = 'Singapore'
            currency = 'SGD'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BngGroupOn':
            source_website_url = 'http://www.crazeal.com/deals/bangalore'
            source_website_logo = 'images/logos/indiagroupon.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[1:].replace(',','')
            url = item['url']
            city = 'Bangalore'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BomGroupOn':
            source_website_url = 'http://www.crazeal.com/deals/mumbai'
            source_website_logo = 'images/logos/indiagroupon.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[1:].replace(',','')
            url = item['url']
            city = 'Bombay'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'CheGroupOn':
            source_website_url = 'http://www.crazeal.com/deals/chennai'
            source_website_logo = 'images/logos/indiagroupon.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[1:].replace(',','')
            url = item['url']
            city = 'Chennai'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'DelGroupOn':
            source_website_url = 'http://www.crazeal.com/deals/delhi'
            source_website_logo = 'images/logos/indiagroupon.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[1:].replace(',','')
            url = item['url']
            city = 'Delhi'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'KolGroupOn':
            source_website_url = 'http://www.crazeal.com/deals/kolkata'
            source_website_logo = 'images/logos/indiagroupon.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip()[1:].replace(',','')
            url = item['url']
            city = 'Kolkata'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BngTimesDeal':
            source_website_url = 'http://www.timesdeal.com/bangalore-deals'
            source_website_logo = 'images/logos/timesdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Bangalore'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BomTimesDeal':
            source_website_url = 'http://www.timesdeal.com/mumbai-deals'
            source_website_logo = 'images/logos/timesdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Bombay'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'CheTimesDeal':
            source_website_url = 'http://www.timesdeal.com/chennai-deals'
            source_website_logo = 'images/logos/timesdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Chennai'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'DelTimesDeal':
            source_website_url = 'http://www.timesdeal.com/delhi-deals'
            source_website_logo = 'images/logos/timesdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Delhi'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'KolTimesDeal':
            source_website_url = 'http://www.timesdeal.com/kolkata-deals'
            source_website_logo = 'images/logos/timesdeal.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Kolkata'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BngRediffDeal':
            source_website_url = 'http://dealhojaye.rediff.com/bangalore'
            source_website_logo = 'images/logos/rediffdeal.jpg'
            description = string.join(item['description']).strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][3].strip()[3:].replace(',','')
            url = item['url']
            city = 'Bangalore'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BomRediffDeal':
            source_website_url = 'http://dealhojaye.rediff.com/mumbai'
            source_website_logo = 'images/logos/rediffdeal.jpg'
            description = string.join(item['description']).strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][3].strip()[3:].replace(',','')
            url = item['url']
            city = 'Bombay'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'CheRediffDeal':
            source_website_url = 'http://dealhojaye.rediff.com/chennai'
            source_website_logo = 'images/logos/rediffdeal.jpg'
            description = string.join(item['description']).strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][3].strip()[3:].replace(',','')
            url = item['url']
            city = 'Chennai'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'DelRediffDeal':
            source_website_url = 'http://dealhojaye.rediff.com/delhi'
            source_website_logo = 'images/logos/rediffdeal.jpg'
            description = string.join(item['description']).strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][3].strip()[3:].replace(',','')
            url = item['url']
            city = 'Delhi'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'KolRediffDeal':
            source_website_url = 'http://dealhojaye.rediff.com/kolkata'
            source_website_logo = 'images/logos/rediffdeal.jpg'
            description = string.join(item['description']).strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][3].strip()[3:].replace(',','')
            url = item['url']
            city = 'Kolkata'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BngBuzzInTownDeal':
            source_website_url = 'http://deals.buzzintown.com/bangalore/home.html'
            source_website_logo = 'images/logos/buzzintown.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url']
            city = 'Bangalore'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BomBuzzInTownDeal':
            source_website_url = 'http://deals.buzzintown.com/mumbai/home.html'
            source_website_logo = 'images/logos/buzzintown.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url']
            city = 'Bombay'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'CheBuzzInTownDeal':
            source_website_url = 'http://deals.buzzintown.com/chennai/home.html'
            source_website_logo = 'images/logos/buzzintown.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url']
            city = 'Chennai'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'DelBuzzInTownDeal':
            source_website_url = 'http://deals.buzzintown.com/delhi/home.html'
            source_website_logo = 'images/logos/buzzintown.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url']
            city = 'Delhi'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'KolBuzzInTownDeal':
            source_website_url = 'http://deals.buzzintown.com/kolkata/home.html'
            source_website_logo = 'images/logos/buzzintown.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url']
            city = 'Kolkata'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BngMyDala':
            source_website_url = 'http://www.mydala.com/deals-bangalore/restaurant'
            source_website_logo = 'images/logos/mydala.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Bangalore'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'BomMyDala':
            source_website_url = 'http://www.mydala.com/deals-mumbai/restaurant'
            source_website_logo = 'images/logos/mydala.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Bombay'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'CheMyDala':
            source_website_url = 'http://www.mydala.com/deals-chennai/restaurant'
            source_website_logo = 'images/logos/mydala.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Chennai'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'DelMyDala':
            source_website_url = 'http://www.mydala.com/deals-delhi/restaurant'
            source_website_logo = 'images/logos/mydala.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Delhi'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
            
        if spider.name == 'KolMyDala':
            source_website_url = 'http://www.mydala.com/deals-kolkata/restaurant'
            source_website_logo = 'images/logos/mydala.jpg'
            description = item['description'][0].strip()
            if len(description) > 128:
                description = description[:128]+'...'
            if len(description) < 68:
                description = description + '<br>&nbsp;</br>'
            price = item['price'][0].strip().replace(',','')
            url = item['url'][0].strip()
            city = 'Kolkata'
            currency = 'INR'
            
            deal = DailyDeals(source_website_url=source_website_url, source_website_logo=source_website_logo, description=description, price=price, url=url, city=city, currency=currency)
            deal.save()
