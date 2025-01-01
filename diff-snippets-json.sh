#!/bin/bash
# https://igorlima.github.io/unapologetic-thoughts/snippets/
usage() {
  echo
  echo "Usage: $0 [...options]"
  echo "Options:"
  echo "  -h, --help                 Show this help message."
  echo "  -s, --sort                 Diff by sorting JSON."
  echo "  -r, --raw                  Diff without sorting."
  echo
  echo "Example: $0 -s"
  echo
}
while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help)
      usage
      exit 1
      ;;
    -s|--sort)
      vim -d <(cat snippets/snippets.json | jq ". | sort_by(.date)" -) <(git show HEAD~1:./snippets/snippets.json | jq ". | sort_by(.date)" -)
      shift
      ;;
    -r|--raw)
      vim -d <(cat snippets/snippets.json | jq . -) <(git show HEAD~1:./snippets/snippets.json | jq . -)
      shift
      ;;
    -*|--*)
      echo "Error: Invalid option: $1"
      usage
      exit 1
      ;;
    *)
      args+=("$1")
      shift
      ;;
  esac
done
usage
