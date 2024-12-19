import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'two cats with green background grass',
    },
    headers={'api-key': '6e247657-3eb4-4463-b063-ff9d547ad99e'}
)
print(r.json())