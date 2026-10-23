# Storage and backup

## Paths

| Path | Purpose |
| --- | --- |
| `~/.rssdude/rssdude.redb` | Default database |
| `~/.rssdude/config.toml` | Optional server/client, theme and retention configuration |
| `~/.rssdude/server.run` | Runtime discovery information for a local server |
| `$RSSDUDE_DB_PATH` | Overrides the database path only |

The database uses native_db over redb. It contains feeds, folders, items and local marks/notes. Database-format compatibility and migration across future releases are not guaranteed by this documentation. Keep a backup before an upgrade.

## Backup

Close the TUI and CLI processes and stop any server using this database before copying it:

```sh
cp ~/.rssdude/rssdude.redb backup.redb
```

Copy config.toml separately if you need it, treating any server token as sensitive. This review does not establish a hot-backup guarantee for copying a live file. Do not synchronize the open database file between machines; use server mode for shared access.

## Restore

With all database users stopped, preserve the current file before replacing it with your backup:

```sh
cp ~/.rssdude/rssdude.redb before-restore.redb
cp backup.redb ~/.rssdude/rssdude.redb
```

Use the path from RSSDUDE_DB_PATH if you override the default. Test a restored copy separately before relying on it; restoration and upgrade compatibility were not exercised in the documentation capture.

## Separate databases

```sh
RSSDUDE_DB_PATH=/tmp/example-feeds.redb rssdude items --unread
```

The application creates missing parent directories for the database path. Server routing still takes precedence: a configured server address or reachable server.run can send commands elsewhere even when RSSDUDE_DB_PATH is set. Check both before using an isolated fixture.

## OPML

```sh
rssdude opml export --output subscriptions.opml
```

OPML represents subscriptions and folder structure, rather than a full copy of items, marks and notes. Keep the database backup when those records matter. The local fixture check did not exercise OPML import/export.
