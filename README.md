# ICMP2RAKP

This script helps to convert the impi hash retrieved from the `msfconsole` into rakp format applicable for the `hashcat` cracking.

## Example:
IMPI hash:
```sh
10.129.248.23:623 - IPMI - Hash found: admin:2220317482000000c20604d15fd7ec21e27741cb28646942483fda89bcf74086ec15bec601520bafa123456789abcdefa123456789abcdef140561646d696e:fc85bc04c9023c6d79195edd0438d69b6761c096
```

Rakp format:
```sh
$rakp$0$10.129.248.23$admin$2220317482000000c20604d15fd7ec21e27741cb28646942483fda89bcf74086ec15bec601520bafa$123456789abcdefa123456789abcdef140561646d696e$fc85bc04c9023c6d79195edd0438d69b6761c096
```

## Usage
The script accepts two arguments:
1. Target IP
2. Credentials hash

```sh
python3 ipmi_to_rakp.py 10.129.248.23 'admin:2220317482000000c20604d15fd7ec21e27741cb28646942483fda89bcf74086ec15bec601520bafa123456789abcdefa123456789abcdef140561646d696e:fc85bc04c9023c6d79195edd0438d69b6761c096'
```
