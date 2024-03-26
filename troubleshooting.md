# Troubleshooting
## HTTP response codes
### 401
Probably missing "ocp-apim-subscription-key" in HTTP header

### 500 - Internal server error
Body is probably incorrect

### 404 - Resource not found
Probably URL is incorrect

## Example commands for testing with curl
### Testing API Endpoint
```
curl -X POST -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: xxx" -d '{"messages": [{"role": "system", "content": "You are a helpful assistant"}], "context": {}}' https://xxx/chat
```

To just get the HTTP response code
```
curl -X POST -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: xxx" -d '{"messages": [{"role": "system", "content": "You are a helpful assistant"}], "context": {}}' -o /dev/null -s -w "%{http_code}\n" https://xxx/chat
```

## API Managementに通信が到達しているかの確認方法
APIM OverviewのMonitor

## Check HTTP logs for App Service
1. Send diagnostic logs to Log Analytics
1. `AppServiceHTTPLogs | where CsUriStem !contains "/webssh"`

