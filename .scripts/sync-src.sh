#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="${ROOT_DIR}/.src"
TMP_ROOT="$(mktemp -d "${ROOT_DIR}/.tmp-sync.XXXXXX")"

REPOS=(
  "brickspacelab/slab"
  "brickspacelab/paper"
  "brickspacelab/space"
  "brickspacelab/keystone"
)

cleanup() {
  rm -rf "${TMP_ROOT}"
}
trap cleanup EXIT

mkdir -p "${SRC_DIR}"

if [[ -z "${BRICKSPACE_GITHUB_TOKEN:-}" ]]; then
  echo "BRICKSPACE_GITHUB_TOKEN is required to sync private BrickspaceLab repositories." >&2
  exit 1
fi

echo "Syncing repository snapshots into ${SRC_DIR}"

for repo in "${REPOS[@]}"; do
  name="${repo##*/}"
  clone_url="https://github.com/${repo}.git"

  tmp_clone="${TMP_ROOT}/${name}-clone"
  tmp_target="${TMP_ROOT}/${name}-target"
  final_target="${SRC_DIR}/${name}"

  echo ""
  echo "-> ${repo}"

  rm -rf "${tmp_clone}" "${tmp_target}"
  mkdir -p "${tmp_target}"

  auth_header="$(printf "x-access-token:%s" "${BRICKSPACE_GITHUB_TOKEN}" | base64 | tr -d '\n')"

  if ! git -c "http.https://github.com/.extraheader=AUTHORIZATION: basic ${auth_header}" \
    clone --depth 1 --quiet "${clone_url}" "${tmp_clone}"; then
    echo "Failed to clone ${repo}. Verify BRICKSPACE_GITHUB_TOKEN has read access." >&2
    exit 1
  fi

  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete \
      --exclude ".git/" \
      --exclude ".github/" \
      --exclude ".gitignore" \
      --exclude ".gitmodules" \
      "${tmp_clone}/" "${tmp_target}/"
  else
    cp -a "${tmp_clone}/." "${tmp_target}/"
    rm -rf "${tmp_target}/.git" \
      "${tmp_target}/.github" \
      "${tmp_target}/.gitignore" \
      "${tmp_target}/.gitmodules"
  fi

  rm -rf "${final_target}"
  mv "${tmp_target}" "${final_target}"

  echo "   Synced to .src/${name}"
done

echo ""
echo "Sync complete."
