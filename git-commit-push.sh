if [ -z "$1" ]; then
  echo "Commit message is required"
  exit 1
fi

# Add all changes
git add .

# Commit with provided message
git commit -m "$1"

# Push to the repository
git push