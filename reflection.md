# Git Reflection

While preparing my grade calculator repository, I ran into a Git author-identity
problem. When I checked the repository settings, Git displayed the generic values
"Your Name" and "your-github-email" instead of my own details. I realized that
if I committed without fixing them, my work could appear in the history under
the wrong name or an invalid email, making it harder to show that the commits
were mine. I solved the problem by setting the author name and the email
associated with my GitHub account in the repository's local Git configuration.
I then created a commit and checked the commit history to confirm the author
information was correct. I also learned to check `git status` and `git log`
before pushing: status helps me see which changes still need committing, while
log confirms the commits and their messages. This experience taught me that Git
configuration is part of preparing a repository, not just an optional setting.
Next time, I will verify my identity and remote before making commits so my
work is recorded accurately.
