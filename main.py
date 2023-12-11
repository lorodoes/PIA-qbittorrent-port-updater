from qbittorrentapi import Client
import subprocess

# qBittorrent web UI details
conn_info = dict(
   host='<qbit host ip or hostname>',
   port='<qbit port>',
   username='<qbit username>',
   password='<qbit password>'
)
# Default is 'adminadmin', change if you've set a different one
qbt_client = Client(**conn_info)
# Desired port
#NEW_PORT = 6881
output = subprocess.check_output(['piactl', 'get', 'portforward'])
NEW_PORT = output.decode('utf-8').strip()
print(NEW_PORT)

# Login to qBittorrent
preferences_data = {
    'listen_port': NEW_PORT
}


get_pref = qbt_client.app_preferences()
if get_pref != NEW_PORT:
    qbt_client.app_set_preferences(prefs=preferences_data)
else:
    print("same port")