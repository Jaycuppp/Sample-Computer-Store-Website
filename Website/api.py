#Libs For API Calls
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class Home_Page_API(object):      
    def Crypto_Pricing_Data(Coin_ID="", Currency=""):    
            EndPoint = '''/v1/cryptocurrency/quotes/latest'''

            API_DOMAIN = f'''https://pro-api.coinmarketcap.com{EndPoint}'''
            API_KEY = "aac109c3-a3e3-4b2e-8c07-5e1ce57ee9f9"

            TEST_API_DOMAIN = f'''https://sandbox-api.coinmarketcap.com{EndPoint}'''
            TEST_API_KEY = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"

            URL = TEST_API_DOMAIN
        
            Parameters = {
                'id': Coin_ID,
                'convert': Currency,
                'skip_invalid': True } 
            
            Headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': TEST_API_KEY}
            
            session = Session()
            session.headers.update(Headers)
            
            try:
                Response = session.get(URL, params=Parameters)
                Data = json.loads(Response.text)
                
                # Will Write Down The JSON Data Onto the File Below
                # Data = (Response.json())
                # with open("CryptoData.json", "w") as File:
                #     json.dump(Data, File)
                    
                # print("Data Got Transfered to CryptoData.json")
                
                Error = Data["status"]["error_message"]
                
                ALL_DATA = Data['data']
                Crypt_Price = Data['data'][Coin_ID]['quote'][Currency]['price']
                
                
                if Error != None:
                    return f'''There is a {Error} Error'''
                
                else:
                    return Crypt_Price
                
            except (ConnectionError, Timeout, TooManyRedirects) as Error:
                return Error
            
        

class Location_Index_Page_API(object):
    def Current_Weather_API(City="", State=""):
        Country = 'USA'
        Fahrenheit = 'imperial'
        
        Weather_API_Key = 'f85aca7bc19a1d4d2b4f6fb57f636aed'
        Weather_API_Domain = f'https://api.openweathermap.org/data/2.5/weather?q={City},{State},{Country}&appid={Weather_API_Key}'


        session = Session()

        Weather_Parameters = {
            'q': (City, State, Country),
            'appid': Weather_API_Key,
            'units': Fahrenheit
        }

        try:
            Weather_Response = session.get(Weather_API_Domain, params=Weather_Parameters)
            Weather_Data = json.loads(Weather_Response.text)
            Weather_Weather_Data = Weather_Data['weather']
            Weather_Temperature_Data = Weather_Data['main']['temp']
            
            return round(Weather_Temperature_Data, 0)

        except (ConnectionError, Timeout, TooManyRedirects) as Error:
            return Error
        
        
        
def MapBox():
    
    Map_Access_Token = 1
    Map_Access_Token = 'pk.pk.eyJ1IjoibmluamEwODE0IiwiYSI6ImNsbjBqcGpzcjFkc3YybHBoMGpzb3d6NDEifQ.Q327KcgWcaRFoAQSuuDmGQ.Q327KcgWcaRFoAQSuuDmGQ'
    
    return 0