BEGIN {FS=":"; ORS="\n\n"; OFS="."}
{print "dn: uid=" $1 ", dc=example, dc=com\ncn: " $2, $3 "\nsn: " $3 "\ntelephone number: " $4}
