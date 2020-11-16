import cgi
import requests
import json
from simple_salesforce import Salesforce

consumer_key = '3MVG959Nd8JMmavT2IGqAtf_hIQJuHEhHcDy_OJnSZclsG0eBdmDwRwF29Qn5aXEJlEib.SxQ3FG1w3R9KinS'
consumer_secret = '5F7229307FF5539BCC91AABE6D7B8BA49175B2C1FCD3140CAD06F432664E9945'
request_token_url = 'https://test.salesforce.com/services/oauth2/token'
access_token_url = 'https://test.salesforce.com/services/oauth2/token'
redirect_uri = 'https://test.salesforce.com/services/oauth2/callback'
authorize_url = 'https://test.salesforce.com/services/oauth2/authorize'  # ?response_type=token&client_id='+consumer_key+'&redirect_uri='+redirect_uri

query = cgi.FieldStorage()
req = None

if 'login' in query:
    print("Location: https://test.salesforce.com/services/oauth2/authorize?response_type=code&client_id=" + consumer_key + "&redirect_uri=" + redirect_uri)

if 'code' in query:
    code = query.getvalue('code')

    data = {
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'code': code,
        'client_id': consumer_key,
        'client_secret': consumer_secret
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    req = requests.post(access_token_url, data=data, headers=headers)
    response = req.json()
    print(response)
    sf = Salesforce(instance_url=response['instance_url'], session_id=response['access_token'])
    records = sf.query("SELECT Id, Name, Email FROM Contact")
    # records = records['records']

# print web page
print("Content-type: text/html")

print("<html><body>")
print("<h1>SELECT Id, Name, Email FROM Contact</h1>")

print("<table>")
print("<tr><td><b>Name</b></td><td><b>Email</b></td></tr>")
for record in records:
    print("<tr><td>" + record['Name'] + "</td><td>" + record['Email'] + "</td></tr>")

print("</table>")

print("</body></html>")