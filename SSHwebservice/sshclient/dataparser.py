import re


def returnparsed(data):
    print(data)
    blocks = re.findall(r'(interface.*?)\!', data, re.DOTALL)
    print(blocks)
    data1 = []
    for i in blocks:
        ds = {}
        interface = validate(re.findall(r'interface\s*(.*?)\n', i))
        description = validate(re.findall(r'description\s*(.*?)\n', i))
        ipaddress = validate(re.findall(r'ip\s*address\s*(.*?)\n', i))
        duplex = validate(re.findall(r'duplex\s*(.*?)\n', i))
        speed = validate(re.findall(r'speed\s*(.*?)\n', i))
        ds["interface"] = interface
        ds["description"] = description
        ds["ip address"] = ipaddress
        ds["duplex"] = duplex
        ds["speed"] = speed
        data1.append(ds)
        print(data1)
    return data1


def validate(da):
    if len(da)>0:
        return da[0]
    else:
        return ''