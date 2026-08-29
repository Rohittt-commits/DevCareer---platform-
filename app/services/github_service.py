import os

import requests


GITHUB_API_URL = "https://api.github.com"


class GitHubService:
    """Service for retrieving public GitHub developer data."""

    def __init__(self):
        self.username = os.getenv("GITHUB_USERNAME")

        self.headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10"
        }

    def get_profile(self):
        """Return the GitHub user's public profile."""

        if not self.username:
            return {
                "success": False,
                "error": "GITHUB_USERNAME is not configured."
            }

        response = requests.get(
            f"{GITHUB_API_URL}/users/{self.username}",
            headers=self.headers,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "success": False,
                "error": "GitHub profile could not be retrieved.",
                "status_code": response.status_code
            }

        data = response.json()

        return {
            "success": True,
            "profile": {
                "username": data.get("login"),
                "name": data.get("name"),
                "bio": data.get("bio"),
                "avatar_url": data.get("avatar_url"),
                "profile_url": data.get("html_url"),
                "public_repositories": data.get("public_repos", 0),
                "followers": data.get("followers", 0),
                "following": data.get("following", 0)
            }
        }

    def get_repositories(self):
        """Return the user's public repositories."""

        if not self.username:
            return {
                "success": False,
                "error": "GITHUB_USERNAME is not configured."
            }

        response = requests.get(
            f"{GITHUB_API_URL}/users/{self.username}/repos",
            params={
                "sort": "updated",
                "direction": "desc",
                "per_page": 30
            },
            headers=self.headers,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "success": False,
                "error": "GitHub repositories could not be retrieved.",
                "status_code": response.status_code
            }

        repositories = response.json()

        result = []

        for repository in repositories:
            result.append({
                "id": repository.get("id"),
                "name": repository.get("name"),
                "description": repository.get("description"),
                "language": repository.get("language"),
                "stars": repository.get("stargazers_count", 0),
                "forks": repository.get("forks_count", 0),
                "url": repository.get("html_url"),
                "updated_at": repository.get("updated_at"),
                "is_fork": repository.get("fork", False)
            })

        return {
            "success": True,
            "count": len(result),
            "repositories": result
        }

    def get_language_summary(self):
        """Return a summary of programming languages used."""

        repositories_result = self.get_repositories()

        if not repositories_result.get("success"):
            return repositories_result

        language_counts = {}

        for repository in repositories_result["repositories"]:
            language = repository.get("language")

            if language:
                language_counts[language] = (
                    language_counts.get(language, 0) + 1
                )

        sorted_languages = sorted(
            language_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return {
            "success": True,
            "languages": [
                {
                    "language": language,
                    "repositories": count
                }
                for language, count in sorted_languages
            ]
        }