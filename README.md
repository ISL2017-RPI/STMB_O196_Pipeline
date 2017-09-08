# STMB_O196_Pipeline

This is the source code for our STMB primitive on the seed data O196

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t stmb196 ./

Then, you can run the pipeline script in the following way:

docker run stmb196 python O196_STMB_wrapper.py "trainData.csv" "trainTargets.csv"

The output is the selected features stored in a csv file
