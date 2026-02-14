cd "c:\Users\Vishnu\Downloads\LLM\LLM"

# Abort any ongoing rebase
git rebase --abort 2>$null

# Rewrite all commits with correct author info
$env:FILTER_BRANCH_SQUELCH_WARNING=1
git filter-branch -f --env-filter 'if [ "$GIT_COMMIT" != "" ]; then
  export GIT_AUTHOR_NAME="PALETI VISHNU"
  export GIT_AUTHOR_EMAIL="vishnuvardhanpaleti24@gmail.com"
  export GIT_COMMITTER_NAME="PALETI VISHNU"
  export GIT_COMMITTER_EMAIL="vishnuvardhanpaleti24@gmail.com"
fi' --all

Write-Host "Done! All commits updated with correct author."
