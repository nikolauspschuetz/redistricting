#!/bin/bash

# make and enter a data resource dir #
mkdir -pv resources/data
cd resources/data

# JeffreyBLewis: congressional-district-boundaries (https://github.com/JeffreyBLewis/congressional-district-boundaries)
mkdir -pv JeffreyBLewis/congressional-district-boundaries
cd JeffreyBLewis/congressional-district-boundaries
git init
git remote add orign https://github.com/JeffreyBLewis/congressional-district-boundaries.git
git pull orign master

cd ../..

# http://cdmaps.polisci.ucla.edu/
# 
# United States Congressional District Shapefiles
# Jeffrey B. Lewis, Brandon DeVine, and Lincoln Pritcher with Kenneth C. Martis
mkdir -pv ucla-polisci-edu/cdmaps
cd ucla-polisci-edu/cdmaps

N_DISTRICTS=114

for i in $(seq ${N_DISTRICTS}); do
	FILE_NAME=$"districts$(printf %03d ${i})"
	URL=$"http://cdmaps.polisci.ucla.edu/shp/${FILE_NAME}.zip"
	curl -o $"${FILE_NAME}.zip" ${URL}
	mkdir ${FILE_NAME}
	unzip $"${FILE_NAME}.zip"
	mv districtShapes/* ${FILE_NAME}/
	rmdir districtShapes
	rm $"${FILE_NAME}.zip"
done

cd ../..