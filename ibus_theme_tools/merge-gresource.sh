#!/usr/bin/env bash

resource_file=()
temp="/tmp/ibus-theme-tools/gresource"
rm -rf $temp
mkdir -p $temp
dest=$1
shift 1
for par in $@; do
    if [ -f $par ]; then
        for file in `gresource list $par`; do
            mkdir -p `dirname $temp$file`
            gresource extract $par $file > $temp$file;
            resource_file+=("$file");
        done
    else
        echo "File not found: $par";
    fi
done

cat <<EOF > "$temp/gtk.gresource.xml"
<?xml version="1.0" encoding="UTF-8"?>
<gresources>
  <gresource prefix="/">
EOF

for value in "${resource_file[@]}"
do
     echo "    <file>${value: 1}</file>" >> $temp/gtk.gresource.xml;
done

cat <<EOF >> "$temp/gtk.gresource.xml"
  </gresource>
</gresources>
EOF

org_dir=`pwd`
cd $temp;
glib-compile-resources gtk.gresource.xml
cd $org_dir;

mkdir -p `dirname $dest`
mv $temp/gtk.gresource $dest

rm -rf $temp
