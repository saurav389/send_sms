import requests
import json
URL = 'https://www.way2sms.com/api/v1/sendCampaign'
apiKey ='RV4QLRFSYMTOS4EIXCY0RSGPON8055IO'
secretKey = '9HJA45PW4D6QRU38'
useType = 'stage'
phoneNo = '+918789238416'
senderId = '9709034301'
textMessage = "Hi Good Morning everyone, This is a test message using Python\nSaurav\n(Programer/Coder)"

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, apiKey, secretKey, useType, phoneNo, senderId, textMessage )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)
