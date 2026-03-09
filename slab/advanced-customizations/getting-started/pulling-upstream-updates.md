# Pulling upstream updates

If you forked the repo, you can pull in new Slab releases at any time:

```sh
git fetch upstream
git merge upstream/main
```

Resolve any conflicts, then run `npm install` to pick up any dependency changes.
