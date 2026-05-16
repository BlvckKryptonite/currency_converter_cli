# Migrating to Fly.io from Heroku

This guide walks through deploying your Currency Converter CLI app to Fly.io.

## What's Been Set Up

- **`fly.toml`** - Main Fly.io configuration file with TCP health checks
- **`Dockerfile`** - Container with Node.js web server + Python CLI (serves web terminal interface)
- **`.dockerignore`** - Optimizes Docker build by excluding unnecessary files

### Important: App Architecture
Your app is a **web-based terminal interface** that runs via:
1. **Node.js** (Total.js framework) - serves the web terminal UI and WebSocket
2. **Python CLI** - runs the currency converter logic inside the terminal

The fixed Dockerfile runs `node index.js` as the entry point, which properly serves the web interface.

## Prerequisites

1. **Install Fly CLI**: https://fly.io/docs/getting-started/installing-flyctl/
2. **Heroku app name** (to migrate): you'll reference this for environment variables
3. **Fly.io account**: https://fly.io/

## Deployment Steps

### 1. Authenticate with Fly.io
```bash
flyctl auth login
```

### 2. Create your Fly.io app
```bash
flyctl launch
```
When prompted:
- **App name**: Enter your desired app name (e.g., `currency-converter-cli`)
- **Region**: Choose nearest to your users (default: `iad` is good for US)
- **Dockerfile**: Choose "Yes" (it will use the one provided)
- **Database**: Choose "No" (not needed for this app)

### 3. Set Environment Variables (if needed)
If your Heroku app had environment variables, copy them to Fly.io:
```bash
flyctl secrets set KEY=VALUE
```

Or set them from a file:
```bash
flyctl secrets import < .env
```

### 4. Deploy
```bash
flyctl deploy
```

### 5. Monitor Deployment
```bash
flyctl logs
```

### 6. Access Your App
```bash
flyctl open
```

## After Migration

### Stop your Heroku app
Once confirmed working on Fly.io:
```bash
heroku apps:destroy --app your-app-name --confirm
```

### Update DNS/Domain (if applicable)
If you have a custom domain:
1. Get your Fly.io app's address:
   ```bash
   flyctl info
   ```
2. Update your domain's DNS CNAME to point to your Fly.io app

### Useful Fly.io Commands

**View logs:**
```bash
flyctl logs
```

**SSH into machine:**
```bash
flyctl ssh console
```

**Scale machines:**
```bash
flyctl scale count=2
```

**Check app status:**
```bash
flyctl status
```

**View machine details:**
```bash
flyctl machines list
```

## Key Differences from Heroku

| Aspect | Heroku | Fly.io |
|--------|--------|--------|
| **Cost** | $7+ dyno minimum | Machines scale from $0 (auto-stop) |
| **Config** | `Procfile` | `fly.toml` + `Dockerfile` |
| **Scaling** | Dynos | Machines |
| **Logs** | Dashboard | CLI command |
| **Health Checks** | Basic | Customizable |

## Troubleshooting

### App won't start
Check logs: `flyctl logs`

### Port issues
The Dockerfile sets `PORT=8080` internally. Fly.io automatically maps this to HTTP/HTTPS.

### Need to rebuild?
```bash
flyctl deploy --force-machines
```

### High memory/CPU usage?
Optimize your `Dockerfile` or adjust machine size in `fly.toml`:
```toml
[[services]]
  processes = ["app"]
  memory_mb = 256  # Default; adjust as needed
  cpu_kind = "shared"
```

## Support

- **Fly.io Docs**: https://fly.io/docs/
- **Getting Help**: https://fly.io/docs/getting-started/get-help/
