#!/bin/bash
# job.sh

for i in {1..50}
do
	echo $i
	res=`cat iris.data |./KMeansMapper.py |sort|./KMeansReducer.py`
	echo '['$res']'
	echo '['$res']' >> c1.data
	sed -i '' "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py
	#sed on macOs默认 -i后需要加一个extension，无需备份+''
done

sed -i '' "7s/^.*$/centerList\ = [$res]/" visualization.py
cat iris.data |./visualization.py
