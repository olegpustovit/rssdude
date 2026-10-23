# Local feed capture

Recorded on 23 October 2026 from the cleanup checkout. The commit containing these files identifies the reviewed source. Rust 1.96.0 on Linux aarch64 built the locked source; 25 existing tests passed, including TUI snapshots.

The capture used the real CLI and the fictional feed.xml served only on loopback. A temporary RSSDUDE_DB_PATH kept data separate. Before running, the harness checked that the host had neither config.toml nor server.run under ~/.rssdude, so automatic server routing could not override the isolated database. It did not change HOME or existing user configuration.

To reproduce, first check your own server-routing configuration as described in the root README. In one terminal:

```sh
uv run docs/demo/serve.py
```

In another, from the checkout:

```sh
cargo build --locked
export RSSDUDE_DB_PATH="$(mktemp -d)/rssdude.redb"
./target/debug/rssdude add http://127.0.0.1:18784/feed.xml --tag demo
./target/debug/rssdude items --limit 5
```

Use an item ID from that output with `rssdude mark <id> --star --read`, then run `rssdude starred`, `rssdude sync` and `rssdude status`. The captured check also queried JSON in separate invocations to assert two total items, one unread and one starred, followed by a sync adding zero duplicates.

output.txt is actual CLI stdout. local-feed.png is a browser-rendered transcript, not the TUI or a hosted account. All feed and entry URLs in the fixture are loopback. The server was stopped after capture. No public feed, article fetch, browser opener, server deployment, retention, OPML, macOS/Homebrew installation or interactive TUI journey was qualified.
