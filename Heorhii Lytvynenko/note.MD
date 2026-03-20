
```
chmod +x map.py red.py

hdfs dfs -rm -r output
hdfs dfs -put input.txt input.txt

hadoop jar /path/to/hadoop-streaming.jar \
-files map.py,red.py \
-mapper map.py \
-reducer red.py \
-input input.txt \
-output output
```

code to run in the hadoop 

```
hadoop jar /path/to/hadoop-streaming.jar \
-files map.py,red.py \
-mapper "python3 map.py" \
-reducer "python3 red.py" \
-input input.txt \
-output output
```