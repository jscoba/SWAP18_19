#### Apache sin balancear

```
javier@javier-zenbook ~/D/3/S/S/practica3> ab -n 50000 -c 300 http://192.168.56.20/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.56.20 (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:        Apache/2.4.18
Server Hostname:        192.168.56.20
Server Port:            80

Document Path:          /
Document Length:        125 bytes

Concurrency Level:      300
Time taken for tests:   27.884 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      19750000 bytes
HTML transferred:       6250000 bytes
Requests per second:    1793.13 [#/sec] (mean)
Time per request:       167.305 [ms] (mean)
Time per request:       0.558 [ms] (mean, across all concurrent requests)
Transfer rate:          691.69 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    5  70.6      0    3112
Processing:    14  118 1404.6     38   27860
Waiting:       13  113 1404.3     38   27857
Total:         15  122 1406.8     38   27869

Percentage of the requests served within a certain time (ms)
  50%     38
  66%     39
  75%     39
  80%     40
  90%     42
  95%     49
  98%    190
  99%    452
 100%  27869 (longest request)

```

#### NGINX

```
javier@javier-zenbook ~/D/3/S/S/practica3> ab -n 50000 -c 300 http://192.168.56.30/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.56.30 (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:        nginx/1.10.3
Server Hostname:        192.168.56.30
Server Port:            80

Document Path:          /
Document Length:        125 bytes

Concurrency Level:      300
Time taken for tests:   57.905 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      19700000 bytes
HTML transferred:       6250000 bytes
Requests per second:    863.48 [#/sec] (mean)
Time per request:       347.432 [ms] (mean)
Time per request:       1.158 [ms] (mean, across all concurrent requests)
Transfer rate:          332.24 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   23 193.9      0    7103
Processing:    28  233 2788.0     89   57866
Waiting:       27  233 2788.0     88   57866
Total:         50  256 2796.5     89   57885

Percentage of the requests served within a certain time (ms)
  50%     89
  66%     89
  75%     90
  80%     90
  90%     92
  95%     95
  98%   1097
  99%   1316
 100%  57885 (longest request)
```



#### HAProxy

```
javier@javier-zenbook ~/D/3/S/S/practica3> ab -n 50000 -c 300 http://192.168.56.30/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.56.30 (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:        Apache/2.4.18
Server Hostname:        192.168.56.30
Server Port:            80

Document Path:          /
Document Length:        125 bytes

Concurrency Level:      300
Time taken for tests:   20.481 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      19750000 bytes
HTML transferred:       6250000 bytes
Requests per second:    2441.27 [#/sec] (mean)
Time per request:       122.887 [ms] (mean)
Time per request:       0.410 [ms] (mean, across all concurrent requests)
Transfer rate:          941.70 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   19 138.8      0    1066
Processing:    33  102  42.7     90    1341
Waiting:       33  102  42.7     90    1341
Total:         33  121 146.3     91    1366

Percentage of the requests served within a certain time (ms)
  50%     91
  66%    107
  75%    122
  80%    131
  90%    151
  95%    169
  98%    358
  99%   1133
 100%   1366 (longest request)

```

#### Pound

```
javier@javier-zenbook ~/D/3/S/S/practica3> ab -n 50000 -c 300 http://192.168.56.30/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.56.30 (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:        Apache/2.4.18
Server Hostname:        192.168.56.30
Server Port:            80

Document Path:          /
Document Length:        125 bytes

Concurrency Level:      300
Time taken for tests:   55.778 seconds
Complete requests:      50000
Failed requests:        12
   (Connect: 0, Receive: 0, Length: 12, Exceptions: 0)
Total transferred:      19745260 bytes
HTML transferred:       6248500 bytes
Requests per second:    896.40 [#/sec] (mean)
Time per request:       334.671 [ms] (mean)
Time per request:       1.116 [ms] (mean, across all concurrent requests)
Transfer rate:          345.70 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   53 244.5      0    7103
Processing:    19  242 2155.7    110   55750
Waiting:        0  227 2095.2    107   55747
Total:         38  295 2177.1    111   55761

Percentage of the requests served within a certain time (ms)
  50%    111
  66%    118
  75%    136
  80%    163
  90%    252
  95%   1112
  98%   1286
  99%   1414
 100%  55761 (longest request)

```
