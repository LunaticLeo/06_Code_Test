import onedrivesdk_fork as onedrivesdk

redirect_uri = 'http://localhost:8080/'
client_secret = 'flB7Q~tt8R5noLfyUWpOtFEfko57-w6yAtsti'
client_id='5187d658-e7f7-43b6-8c67-9f92f0fe37fa'
api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(
    http_provider=http_provider,
    client_id=client_id,
    scopes=scopes)

client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
auth_url = client.auth_provider.get_auth_url(redirect_uri)
# Ask for the code
print('Paste this URL into your browser, approve the app\'s access.')
print('Copy everything in the address bar after "code=", and paste it below.')
print(auth_url)
code = raw_input('Paste code here: ')

client.auth_provider.authenticate(code, redirect_uri, client_secret)