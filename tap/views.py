import requests
url = "https://www.taptap.com/webapiv2/landing/v5/timeline-with-guest?action=refresh&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D44%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D3f3a0a6a-a342-4782-80f2-eb5b48165b75%26DT%3DPC"
# url = "https://www.taptap.com/"
param = {
    'action': 'refresh',
    'X-UA': "V=1&PN=WebApp&LANG=zh_CN&VN_CODE=44&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=3f3a0a6a-a342-4782-80f2-eb5b48165b75&DT=PC",
}
response = requests.request("GET", url, params=param)

# title = response.json()["data"]["list"]
# print(title)
for i in range(10):
    type = response.json()["data"]["list"][i]["type"]
    if type != "default":
        continue
    title = response.json()["data"]["list"][i]["title"]
    contents = response.json()["data"]["list"][i]["contents"]

    print(title,contents)

