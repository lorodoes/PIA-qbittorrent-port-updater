install:

pip install qbittorrent-api

To use those script just update the top section of the file:

conn_info = dict(
   host='<qbit host ip or hostname>',
   port='<qbit port>',
   username='<qbit username>',
   password='<qbit password>'
)

This will allow the system to connect to the qbit and update the port as needed.