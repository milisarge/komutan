dizin=/mnt/disk
cd $dizin
mount -t proc none proc
mount --rbind /sys sys
mount --rbind /dev dev
