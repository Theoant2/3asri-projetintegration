echo "Extracting package"
rm -rf motoman
mv * ../
cd ..
rm -rf 3asri-projetintegration

echo "Moving xarco files"
mv hc10.xacro motoman/motoman_hc10_support/urdf/
mv hc10_macro.xacro motoman/motoman_hc10_support/urdf/

echo "Setup done ..."