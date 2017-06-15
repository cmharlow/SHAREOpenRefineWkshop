import requests
import json

def getData(URL):
    r = requests.get(URL, headers={'Content-Type': 'application/vnd.api+json'})
    resp = r.json()
    for n in resp['data']:
        out.append(n)
        with open('sampleData.json', 'w') as fh:
            json.dump(out, fh)
    try:
        next_link = r.json()['links']['next']
        getData(next_link)
    except Exception as e:
        print(e)


def main():
    getData("https://share.osf.io/api/v2/normalizeddata/")


if __name__ == '__main__':
    out = []
    main()
