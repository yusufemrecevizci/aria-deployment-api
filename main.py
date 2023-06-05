import http.client
import json

connectionAddress = http.client.HTTPSConnection("api.mgmt.cloud.vmware.com")
payload = ''
headers = {
  'Authorization': 'Your Bearer Token'
}
connectionAddress.request("GET", "/deployment/api/deployments", payload, headers)
res = connectionAddress.getresponse()
data = res.read()
#print(data.decode("utf-8"))
deployments = json.loads(data.decode("utf-8"))

#print(deployments)

for deployment in deployments['content']:
  deployment_id = deployment['createdAt']
  print(deployment_id)
