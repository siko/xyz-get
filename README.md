xyz-get
=======

download tools,now support download from below sites:

* http://ipn.li/itgonglun/


install
=======
    
    sudo pip3 install BeautifulSoup4
    git clone https://github.com/siko/xyz-get.git
    cd xyz-get 
    python3 xyz-get -h

usage
=====

    xyz-get -h
    
    Usage: xyz-get [OPTION]... [URL]...

    Startup options:
        -V | --version                           Display the version and exit.
        -h | --help                              Print this help and exit.
    
    Download options (use with URLs):
        -f | --force                             Force overwriting existed files.
        -i | --info                              Display the information of videos without downloading.
        -u | --url                               Display the real URLs of videos without downloading.
        -c | --cookies                           Load NetScape's cookies.txt file.
        -o | --output-dir <PATH>                 Set the output directory for downloaded videos.
        -x | --http-proxy <HOST:PORT>            Use specific HTTP proxy for downloading.
        -l | --limit 0,10 or 10                  Limit of every URL files for downloading, 0 can be skip.
             --no-proxy                          Don't use any proxy. (ignore $http_proxy)
             --debug                             Show traceback on KeyboardInterrupt.
    

examples
========

    python3 xyz-get -o /tmp -l 2 http://ipn.li/taiyilaile/
    
    Site:		 ipn.li
    Title:		 走进莆田系－－私立医院黑幕大起底（下）
    Type:		 MP3 (audio/mpeg)
    Size:		 39.26 MiB (41170386 Bytes)
    URL:		 http://ipn.li/taiyilaile/7/audio.mp3
    
    Downloading 走进莆田系－－私立医院黑幕大起底（下）.mp3 ...
    100.0% ( 39.3/39.3 MB) [========================================] 1/1
    
    Site:		 ipn.li
    Title:		 走进莆田系－－私立医院黑幕大起底（上）
    Type:		 MP3 (audio/mpeg)
    Size:		 44.25 MiB (46399018 Bytes)
    URL:		 http://ipn.li/taiyilaile/6/audio.mp3
    
    Skipping /tmp/走进莆田系－－私立医院黑幕大起底（上）.mp3: file already exists
    
        
        