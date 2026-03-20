chmod +x map.py red.py


hdfs dfs -rm -r input.txt
hdfs dfs -put input.txt input.txt

hdfs dfs -rm -r output

# this commands to run in hadoop cluster terminal