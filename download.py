import requests

def download_file(url):
response = requests.get(url)
if response.status_code == 200:
return response.content
else:
raise Exception('Failed to download file: {}'.format(url))


