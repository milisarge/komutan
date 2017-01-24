kelime="test"
echo -n $kelime | sha1sum | awk '{print $1}'