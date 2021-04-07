import os, sys, json
import urllib.parse as ul
url='https://s282man.storage.yandex.net/rdisk/6f4a7bba8d3c41155df65bff3f4cc8400110cf4f78fe2f9c2a3790d520a9cf5b/6068ca90/9BD6OxNWNjt8lFGpKS9ULXY_JM3srOY34UGgFoRhQw7UjsHcnQRc_Oh2iG4TSpxsccOQaXux_X4YfnH-Fb3N8Q==?uid=0&filename=yolov3_608.weights&disposition=attachment&hash=6O24X7OCBTn10GNHkPjQtbuQiNIudVSpujDea08d34rwH04JtsjsPGtlcW5E/V%2Boq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Foctet-stream&owner_uid=500809706&fsize=248007048&hid=94ca59fcbe9d39cef0a159418f106640&media_type=data&tknv=v2&rtoken=nqLvfspm673P&force_default=no&ycrid=na-a80b22a8609c32ba05cd54330f484c18-downloader20h&ts=5bf16fcdbc400&s=4d6a3e67777405dc9717f0cf4615930cae48946c4001166f8924ec9453b69ee3&pb=U2FsdGVkX1876bBP9TCxCiSlCOBZpjrLQpdOZhGKY5anrOdiZnpTba5NHBABOkokqrMrDOTahhS-0_xUkzQJL2I7reOdt_TG6fJzdLrTxLo'
folder='yolo'
base_url = 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key='
url = ul.quote_plus(url)
folder = folder
res = os.popen('wget -qO - {}{}'.format(base_url, url)).read()
json_res = json.loads(res)
filename = ul.parse_qs(ul.urlparse(json_res['href']).query)['filename'][0]
os.system("wget '{}' -P '{}' -O '{}'".format(json_res['href'], folder, filename))