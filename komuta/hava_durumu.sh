URL='http://www.accuweather.com/en/tr/city/no/weather-forecast/318290'

wget -q -O- "$URL" | awk -F\' '/acm_RecentLocationsCarousel\.push/{print $2": "$16" "$12"°"" "$14 }'| head -1
