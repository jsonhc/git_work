# $ wget https://curl.haxx.se/download/curl-7.62.0.tar.gz
# $ tar xf curl-7.62.0.tar.gz
# $ cd curl-7.62.0/
# $ sudo ./configure
# $ sudo make && sudo make install
# $ which curl-config --->/usr/local/bin/curl-config
# $ pip3 install pycurl
# >>> import pycurl
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: pycurl: libcurl link-time version (7.58.0) is older than compile-time version (7.62.0)
# $ sudo echo "/usr/local/lib"  >> /etc/ld.so.conf
# $ sudo ldconfig
import pycurl
