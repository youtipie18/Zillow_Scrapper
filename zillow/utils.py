from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-82.197042453125%2C%22east%22%3A-69.343038546875%2C%22south%22%3A39.496477277590934%2C%22north%22%3A45.91376812538369%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=3"


def cookie_parser():
    cookie_string = "zguid=24|%24932de289-ac03-4d66-97c3-5aa9bb1ee7e1; zgsession=1|90c27f68-8e30-4f16-814c-b7d269a980b3; zjs_anonymous_id=%22932de289-ac03-4d66-97c3-5aa9bb1ee7e1%22; zjs_user_id=null; zg_anonymous_id=%22fa219001-e781-4741-b597-cd6d81b9db18%22; _ga=GA1.2.1911029767.1697980512; _gid=GA1.2.1387314771.1697980512; _gat=1; _gcl_au=1.1.1851564284.1697980512; DoubleClickSession=true; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; pxcts=07a97b04-70dd-11ee-ac2d-43c6b4e46b83; _pxvid=07a96617-70dd-11ee-ac2d-cb9d98c94d26; _pxff_cfp=1; _pxff_bsco=1; x-amz-continuous-deployment-state=AYABeCzF7xfWSpa7NipzypGZoc0APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADKpg2tc96JBgt2y5DwAwHe0KX8GXW9w%2FEuEBFEV0Yh9DlAfcNdu2nR4Wn4bfvt2eDhCoTLxfjWg7Swl27g21AgAAAAAMAAQAAAAAAAAAAAAAAAAAAKfMqblAz6D0GenpimsxC3P%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAyjCZucsuiU2WayfNeygVQRJIFMeZf3jZt4vzN6eZf3jZt4vzN6; __pdst=55d5fc0d262748f284cbbe2fa7e222d0; _hp2_id.1215457233=%7B%22userId%22%3A%225996864343871353%22%2C%22pageviewId%22%3A%227915827689845085%22%2C%22sessionId%22%3A%223149629306971226%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.1215457233=%7B%22ts%22%3A1697980512717%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _pin_unauth=dWlkPU56YzRNRGhoTm1NdE56WTJZaTAwTVRsa0xXRXlaak10TVdReVpqY3dNR0kwWW1OaQ; _clck=1cfcuvw|2|fg2|0|1390; JSESSIONID=A9125D4FAB060C6E4ABDB2776FAFB275; _px3=779e19f888fbb65ea6bc69b828cb86161a1bf07fc4869c9ae0e076a89db92d76:JfSx9QbZ6ucgfCAbMxRkBac8naQlLVU3OiBw5PBg3DTI+3vuoL+zjFGKbv0MKNZ0MSQQ1+CzGDzRrrHVnrqIog==:1000:EKVMyk0k1d2LTq0yGmpPjpk5vpVzEuE0KQMxmZQ0l8BtWccluLNvqXIchb2WqmubcYqPeikw6tfLvwbT5IecSx/mB8z+emjAkP0Wb4mHhknwJGgwvbnXVCHgydFqbwO4vMSugmI1V8YVlQp/dYGIQUSSS0bDSMI6BOLcdGTonshTCNF41szdDtiLN2RrlV4XKXMlXLFq7Ny8qJVLUcfvFWh3nYnribnUmtcKo1tzpDs=; _uetsid=087c7c5070dd11ee8476ddad25007a99; _uetvid=087c968070dd11ee82b2fdd0a10e553b; AWSALB=cX220aA2es7CPSe+3dtsfTKanRF8+YQmU9YBzbbXMh6Kn2EVVrTgjJ+xoynyuRa2paJ6vwx7t4a+IShefIpBzhpHpeo2OO6QA/tzoOQ9VDLG5ed3KUiNpy66sYA8; AWSALBCORS=cX220aA2es7CPSe+3dtsfTKanRF8+YQmU9YBzbbXMh6Kn2EVVrTgjJ+xoynyuRa2paJ6vwx7t4a+IShefIpBzhpHpeo2OO6QA/tzoOQ9VDLG5ed3KUiNpy66sYA8; search=6|1700572536385%7Crect%3D45.91376812538369%252C-69.343038546875%252C39.496477277590934%252C-82.197042453125%26rid%3D43%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0943%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; _clsk=1gb551n|1697980537468|3|0|z.clarity.ms/collect"
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies


def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url
