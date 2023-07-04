import urllib as ul
import urllib.request as req
import json
import secretkey
    
class Locale:
    def __init__(self,addr,lng,lat):
        self.addr = addr #도로명 주소(road_address_name)
        self.longitude = lng #경도(x)
        self.latitude = lat #위도(y)
    @staticmethod
    def json2locale(item):
        addr = item['road_address']
        lng = item['x']
        lat = item['y']
        return Locale(addr,lng,lat)
    def write(self,fs):
        fs.write(self.addr)
        fs.write(",")
        fs.write(self.longitude)
        fs.write(",")
        fs.write(self.latitude)
        fs.write('\n')
    
def search(text):
    api_key = secretkey.api_key
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    text = ul.parse.quote(text)
    query = "query="+text
    query_str = f'{url}?{query}'
    request = req.Request(query_str)
    request.add_header("Authorization","KakaoAK "+api_key)
    resp = req.urlopen(request)
    if resp.getcode()!=200:
        return None
    data = resp.read()
    jdata = json.loads(data)
    items = jdata['documents']

    return [Locale.json2locale(item) for item in items] 