amixer get Master | egrep 'Playback '
ses_kart_no=1
ses_degeri=30
amixer set Master $ses_degeri
amixer -c $ses_kart_no set Master $ses_degeri
