#!/bin/sh

static_score=0
dynamic_score=0

if [ -f /etc/network/interfaces ]; then
    grep -qi "address" /etc/network/interfaces && ! grep -qi "dhcp" /etc/network/interfaces && static_score=$((static_score+1))
    grep -qi "dhcp" /etc/network/interfaces && dynamic_score=$((dynamic_score+1))
fi

if [ -d  /etc/NetworkManager ]; then
    nmcli -t -f ipv4.method connection show 2>/dev/null | grep -qi manual && static_score=$((static_score+1))
    nmcli -t -f ipv4.method connection show 2>/dev/null | grep -qi auto && dynamic_score=$((dynamic_score+1))
fi

ls  /var/lib/dhcp/*lease* >/dev/null 2>&1 && dynamic_score=$((dynamic_score+1))

total=$((static_score+dynamic_score))

if [ "$total" -eq 0 ]; then
    echo "unknown confidence=0%"
elif [ "$static_score" -gt "$dynamic_score" ]; then
    echo "static confidence=$((static_score*100/total))%"
else
    echo "dynamic confidence=$((dynamic_score*100/total))%"
fi

