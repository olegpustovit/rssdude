# Install

## Apple Silicon mac (Homebrew)

```bash
brew tap olegpustovit/tap
brew install rssdude
```

The tap installs its pinned release version, not necessarily the newest GitHub release. The checked-in formula targets Apple Silicon; confirm the active tap formula before installation. Homebrew installation was not tested in the local documentation check.

## From source on macOS

```bash
brew install libiconv     # keg-only, the linker needs it
git clone https://github.com/olegpustovit/rssdude
cd rssdude
make install              # cargo install --locked --path . into ~/.cargo/bin
```

The `LIBRARY_PATH=/opt/homebrew/opt/libiconv/lib` is set automatically by the Makefile. If you build with bare `cargo build` outside the Makefile, you'll need to export it yourself.

## From source on Linux

```bash
git clone https://github.com/olegpustovit/rssdude
cd rssdude
cargo install --path .
```

The recorded Linux aarch64 build did not need an extra libiconv path. Other systems were not qualified in that check.

## Make targets

The Makefile is a tiny convenience layer over `cargo`. The targets you'll actually use:

| Target | What it does |
|--------|--------------|
| `make build`     | Release build into `target/release/rssdude` |
| `make install`   | `cargo install` to `$(PREFIX)/bin` (default `~/.cargo`) |
| `make uninstall` | Remove the installed binary |
| `make test`      | Unit + snapshot tests |
| `make clippy`    | Lint with `-D warnings` |
| `make run ARGS="items --unread"` | `cargo run` passthrough |

Pass `make install PREFIX=/usr/local` if you'd rather it land somewhere else.

## Verify

```bash
rssdude --version
rssdude --help
```

If `rssdude` isn't found, check that `~/.cargo/bin` is on your `PATH`.

## Upgrading

Homebrew:

```bash
brew update && brew upgrade rssdude
```

From source:

```bash
cd rssdude && git pull && make install
```

The database format is forward-compatible on your existing `~/.rssdude/rssdude.redb` keeps working across upgrades. If a future version ever needs a migration, the binary handles it on first run.

## Uninstall

```bash
make uninstall              # removes the binary
rm -rf ~/.rssdude            # removes the database & config on only if you really want to
```
