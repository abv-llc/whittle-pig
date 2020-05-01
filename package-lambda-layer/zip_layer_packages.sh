chmod +x get_layer_packages.sh
./get_layer_packages.sh
zip -r Custom-Python37-Layer.zip python/
rm -rf python/
