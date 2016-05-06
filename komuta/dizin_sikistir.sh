dizin=/root/Desktop/gb
sd_ad=test
tar -zcvf "$(dirname "$dizin")"/"$sd_ad".tar.gz $dizin
echo "$(dirname "$dizin")"
ls -l "$(dirname "$dizin")" | grep "$sd_ad".*