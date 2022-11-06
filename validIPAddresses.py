def validIPAddresses(string):
    validIPAddresses = []
    if len(string) < 4:
        return validIPAddresses

    for i in range(1, len(string)-2):
        parts = ["", "", "", ""]

        parts[0] = string[:i]
        if not isValidIp(parts[0]):
            continue
            
        for j in range(i+1, len(string)-1):
            parts[1] = string[i:j]
            
            if not isValidIp(parts[1]):
                continue
            
            for k in range(j+1, len(string)):
                parts[2] = string[j:k]
                parts[3] = string[k:]
                if isValidIp(parts[2]) and isValidIp(parts[3]):
                    validIPAddresses.append(".".join(parts))

    return validIPAddresses
                
                
def isValidIp(iPAddress):
    ipAddressAsInt = int(iPAddress)

    if ipAddressAsInt > 255:
        return False

    return len(str(ipAddressAsInt))  == len(iPAddress)


def test_validIPAddresses():
    input = "1921680"
    expected = [
        "1.9.216.80",
        "1.92.16.80",
        "1.92.168.0",
        "19.2.16.80",
        "19.2.168.0",
        "19.21.6.80",
        "19.21.68.0",
        "19.216.8.0",
        "192.1.6.80",
        "192.1.68.0",
        "192.16.8.0",
    ]
    actual = validIPAddresses(input)
    assert(actual == expected)