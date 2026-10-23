# Homebrew tap

Files staged here belong in the [`olegpustovit/homebrew-tap`](https://github.com/olegpustovit/homebrew-tap) repo.
After a release, copy `Formula/rssdude.rb` into that repo with the real SHA256s filled in.

## End-user install

```bash
brew tap olegpustovit/tap
brew install rssdude
```

## Release workflow

1. Push a `v*` tag on this repo. `.github/workflows/release.yml` builds
   an `aarch64-apple-darwin` binary and attaches them
   to the GitHub release.
2. Grab the SHA256s from the `*.sha256` files in the release.
3. Update `Formula/rssdude.rb` in the tap repo with the new `version` and SHAs,
   commit, push.
