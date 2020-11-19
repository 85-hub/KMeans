#!/bin/bash
# job.sh
rm c.data
touch c.data
bin/hdfs dfs -rm -R /user/guyi/outputKmeans/*
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming*.jar -input /user/guyi/inputIris -mapper ./KMeansMapper.py -reducer ./KMeansReducer.py -output /user/guyi/outputKmeans/1
prev=`bin/hdfs dfs -cat /user/guyi/outputKmeans/1/part-00000`

sed -i '' "7s/^.*$/centerList\ = [$prev]/" KMeansMapper.py#替换line7

for i in {2..50}
do
	echo $i
	bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming*.jar -input /user/guyi/inputIris -mapper ./KMeansMapper.py -reducer ./KMeansReducer.py -output /user/guyi/outputKmeans/$i
	res=`bin/hdfs dfs -cat /user/guyi/outputKmeans/$i/part-00000`
	if [ "$res" = "$prev" ]
	then
		echo "The Center is found!"
		break
	else
		prev=$res
		echo '['$res']'
		echo '['$res']' >> c.data
		sed -i '' "7s/^.*$/centerList\ = [$res]/" KMeansMapper.py
	fi
done
