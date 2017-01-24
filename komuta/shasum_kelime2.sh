kelime="test3"
echo -n $kelime | sha1sum | awk '{print $1}'