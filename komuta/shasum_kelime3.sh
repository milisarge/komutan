kelime="test3"
echo -n $kelime | sha1sum | awk '{print toupper($1)}'