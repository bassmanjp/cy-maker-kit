# Working with Claude: pitfalls we learned the hard way

1. **One session per project folder.** Two sessions editing the same folder
   overwrite each other. Second task in the same project: wait, or copy it.
2. **"Done" without a check is a guess.** Ask "how do you know?" if Claude
   says it works without having seen the output.
3. **Three tries, then stop.** The same fix attempted a fourth time won't
   work. Go back to what is known for sure.
4. **Commit before anything risky.** Every working step committed means any
   mistake is one `git revert` away.
5. **Memory is not knowledge.** Libraries and tools change between
   versions and rename whole APIs. Check the docs or examples.
6. **Long sessions get worse and cost more.** Start a fresh session per
   task; NOTES.md carries the state across.
7. **Read the whole error.** The real cause is often the first error, not
   the last line.
8. **A helper's report is a claim.** Check its diff and run the tests.
9. **Don't let it work around a refusal.** If a permission or safety check
   blocks something, find out why; never copy the file elsewhere to dodge it.
10. **Correct it once, in writing.** When Claude does something you don't
    want, say so and have it added to CLAUDE.md, or it will do it again.
11. **Plans hide assumptions.** Before building, ask what the plan depends
    on that hasn't been checked yet.
12. **Pictures beat descriptions.** A screenshot or a photo (of the app,
    the error, the part, the breadboard) beats a description.
13. **Secrets stay out of git.** Passwords and API keys go in a
    git-ignored file (`.env`, `secrets.h`), never in what you commit or share.
14. **Pin versions.** An unpinned library or platform updates itself one
    day and breaks a project that worked yesterday.
15. **Small steps are faster.** Two new parts at once means two unknowns
    when it fails.
