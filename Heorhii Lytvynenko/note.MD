
-mapper "python3 map.py"
-reducer "python3 red.py"

hdfs dfs -rm -r output

# this commands to run in hadoop cluster terminal