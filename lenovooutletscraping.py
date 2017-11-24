import re
from StringIO import StringIO

from lxml import etree
import requests
import dataset


# Filter criteria from the url, currently 'New, Refurbished, Scractch&Dent' and 'T Series':
FACETS = {'facet-1': '1,2,3,4',
                 'facet-3': '14',}

# Additional criteria setting:
PRICE_POINT = 850
IGNORE_SLIM = True

# In the Network tab of Chrome's Developer tools, there will be a series
# of requests to 'catalog.workflow:GetCategoryFacetResultRow?category-id='
# for each product; however, the value doesn't seem to change.
CATEGORY_ID = '908B184AED4F29502E6EB3E1E76AFC13'


def list_itemids():
    url = 'http://outlet.lenovo.com/SEUILibrary/controller/e/outlet_us/LenovoPortal/en_US/wci.workflow:load?'
    headers = {'Accept': 'text/html, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive',
               'Content-Length': '125',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Cookie': 'ConfigContext=LenovoPortal',
               'Host': 'outlet.lenovo.com',
               'Origin': 'http://outlet.lenovo.com',
               'Referer': 'http://outlet.lenovo.com/outlet_us/laptops/',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest',}
    params = {'page': '/WW/site/templates/faceted-browse/owv2/CategoryFacetResults.html'}
    data = {'category-id': CATEGORY_ID,
            'sort-criteria': '1',
            'page-size': '100',}
    data.update(FACETS)
    response = requests.post(url, headers=headers, params=params, data=data)
    itemids = re.findall(r':[0-9A-F]{8}:[0-9A-F]{8}:', response.content)
    return itemids


def get_details(itemid):
    url = 'http://outlet.lenovo.com/SEUILibrary/controller/e/outlet_us/LenovoPortal/en_US/catalog.workflow:GetCategoryFacetResultRow?'
    headers = {'Accept': 'text/html, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.8',
               'ADRUM': 'isAjax:true',
               'Connection': 'keep-alive',
               'Cookie': 'ConfigContext=LenovoPortal',
               'Host': 'outlet.lenovo.com',
               'Origin': 'http://outlet.lenovo.com',
               'Referer': 'http://outlet.lenovo.com/outlet_us/laptops/',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest',}
    params = {'category-id': CATEGORY_ID,
              'facetType': 'null',
              'page': '1',
              'itemid': itemid,}
    response = requests.get(url, headers=headers, params=params)
    return response.content


def parse_tree(details):

    li = re.findall(r'<li.*>.*</li>', details, flags=re.DOTALL)
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(StringIO(li[0]), parser)
    return tree


def summarize(tree):

    details = {'product_name': tree.xpath('//*[@class="facetedResults-header"]/h3/a/text()')[0].strip(),
               'inventory': tree.xpath('//*[@class="inventory"]/text()')[0].strip(),
               'part_number': tree.xpath('//*[@class="facetedResults-header"]/div/text()')[0].strip(),
               'list_price': tree.xpath('//*[@class="webprice pricingSummary-priceList-value"]/text()')[0].strip(),
               'sale_price': tree.xpath('//*[@class="aftercoupon pricingSummary-details-final-price"]/text()')[0].strip(),}
    labels = ['processor', 'operating_system', 'display', 'graphics', 'memory', 'hard_drive', 'optical_drive']
    features = dict(zip(labels, tree.xpath('//*[@class="facetedResults-feature-list"]/dl/dd/text()')))
    details.update(features)
    return details


def render(summary, cached=False):
    if check_criteria(summary):
        if cached: print '**cached**',
        print(summary['product_name'] + ' (' + summary['part_number'] + ')')
        print(summary['inventory'] + ': ' + summary['sale_price'] + ' (' + summary['list_price'] + ')\n')
        print('Processor: '.rjust(20) + summary['processor'])
        print('Operating System: '.rjust(20) + summary['operating_system'])
        print('Display: '.rjust(20) + summary['display'])
        print('Graphics: '.rjust(20) + summary['graphics'])
        print('Memory: '.rjust(20) + summary['memory'])
        print('Hard Drive: '.rjust(20) + summary['hard_drive'])
        print('Optical Drive: '.rjust(20) + summary['optical_drive'] + '\n')


def check_criteria(summary):

    # Ignore slim/ultrabook models
    if IGNORE_SLIM and re.match(r'.*T[45]{1}[3456]{1}0[us]{1}', summary['product_name']):
        return False

    # Stop after price point
    elif float(summary['sale_price'].replace('$', '').replace(',', '')) > PRICE_POINT:
        return False

    else:
        return True


def listings():
    with dataset.connect('sqlite:///lenovo.db') as db:
        laptops = db['laptops']
        for itemid in list_itemids():
            record = laptops.find_one(itemid=itemid)
            if not record:
                laptop = {'itemid': itemid}
                laptop.update(summarize(parse_tree(get_details(itemid))))
                laptops.insert(laptop, ensure=True)
                render(laptop)
            else:
                render(record, cached=True)


if __name__ == "__main__":
    listings()
