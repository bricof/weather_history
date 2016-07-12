# Wrangling the Daily Global Weather Measurements data set

The [Daily Global Weather Measurements data set](https://aws.amazon.com/datasets/daily-global-weather-measurements-1929-2009-ncdc-gsod/) was originally collected by the National Climactic Data Center and is available as a public data set on Amazon Web Services (AWS). (Note that, as per the note at the bottom of the [link](https://aws.amazon.com/datasets/daily-global-weather-measurements-1929-2009-ncdc-gsod/), this data set can only be used within the United States.) On AWS, the data is available on an EBS snapshot as a collection of text files. The volume is 20 GB in size.

To aid in exploration and analysis of this data, the [weather_mysqlconfig notebook](https://github.com/bricof/weather_history/blob/master/weather_mysqlconfig.ipynb) sets up a MySQL server on an EC2 instance with the data loaded as tables. The notebook uses the boto and paramiko libraries in Python, and but for one manual ssh action required in the middle of the process (as described in the notebook), it can otherwise run through on its own. The result is a database with three tables, indexed for fast searches on station ID, year, month, day and temperature. The database uses 34 GB of disk space.

Example queries of this database (via the MySQLdb library in Python) are shown in the [weather_queries notebook](https://github.com/bricof/weather_history/blob/master/weather_queries.ipynb). 

See [this blog post](http://briancoffey.ca/blogpost5.html) for an interactive visualization using some of this data.
