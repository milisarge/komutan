servis=tor
/etc/init.d/$servis start
test_url=ifconfig.me
curl --socks5 127.0.0.1:9050 -s $test_url
