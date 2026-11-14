# START HERE (setup wizard, instructions for Claude)

You are setting up a friend to work with Claude on any kind of project:
code, electronics, a website, a 3D print, home automation, writing, a plan
for something they are building. They are not expected to code or use a
terminal. You do the hands-on work; they click the few buttons only they can
click and tell you what they see.

**Run this as a wizard.** One step at a time. For each step: say in one or
two friendly sentences what it is and why it matters, do it, show the result
in plain words, then ask "Ready for the next step?" and wait. Keep a running
"Step N of 7" line at the top of each message. Ask before installing
anything. Never dump command output on them; summarise it. If a step fails,
fix it before moving on. If a safety or permission check refuses a step,
never work around it: explain what was blocked, and either skip it (if
optional) or ask them to approve it.

Below, `KIT` means this folder (the one holding this file) and `PROJECTS` its
parent folder, which holds all their projects.

## Step 0: Where are you running?

If you cannot run shell commands on their computer (for example in Cowork's
sandbox), stop and tell them: "For this I need the Code tab. Open the Claude
app, Code tab, start a session on your Projects folder, and say: open
cy-maker-kit/START-HERE.md and follow it." Do nothing else.

If the session's permission mode is not Auto, suggest it once: the mode
picker next to the message box, Auto (or Accept edits if Auto isn't
offered). Claude then works without asking at every command and still stops
for anything risky.

## Step 1 of 7: Welcome

Tell them what they will have at the end (about 30 to 45 minutes):
- Claude set up to help with any project, and the kit's way of working
  installed so every future session starts with it: plan first, small
  steps, checked in real use, saved to GitHub;
- their first project started and safely on GitHub.
Tell them there are no API keys, no extra cost, and that you will ask before
anything is installed. Ask two things:
- what they want to work on first (anything; "not sure yet" is fine, then
  offer a small starter idea that matches their interests);
- whether their Claude plan is Pro or Max (in the app under Settings, then
  Usage or Plan; "not sure" is fine).

## Step 2 of 7: Developer tools and your GitHub account

1. **Apple developer tools** (git and the C++ compiler): if `git --version`
   fails or `xcode-select -p` errors, run `xcode-select --install`. Tell them
   a pop-up will appear: click **Install**, accept, wait a few minutes, then
   say "done". Windows: git from https://git-scm.com instead.
2. **GitHub CLI** (`gh`): if `gh --version` fails, install it in their user
   folder, no admin password:
   - Get the newest `gh_*_macOS_arm64.zip` (Apple chip; `uname -m` says
     `arm64`) or `gh_*_macOS_amd64.zip` (Intel), never the `.pkg`, from
     https://github.com/cli/cli/releases/latest (the API at
     `https://api.github.com/repos/cli/cli/releases/latest` lists the assets),
     unzip it in a temp folder, copy `bin/gh` to `~/.local/bin/`, and make
     sure `~/.local/bin` is on the PATH (add
     `export PATH="$HOME/.local/bin:$PATH"` to `~/.zprofile` if it is not;
     for this session prefix commands with it).
3. **Their GitHub account.** Ask whether they have one. Explain first, in
   two lines: GitHub keeps a safe copy and the full history of every project
   off their Mac, private to them; lose the laptop, lose nothing. It's free.
   If they have none, walk them through it:
   - Open https://github.com/signup for them (`open <url>` on a Mac).
   - Free plan. The username shows on their profile, so pick one they like.
   - Say yes to two-factor login when offered; an authenticator app or
     passkey is easiest.
   - Wait while they do it; they say "done" when they can see their GitHub
     home page.
4. **Log in to GitHub from this Mac:** run
   `gh auth login --hostname github.com --git-protocol https --web`.
   It shows a one-time code and opens the browser: tell them to type the code,
   click Authorize, and come back. If the command stops on a question because
   your shell is not interactive, ask them to type the same line into the
   app's message box with a `!` in front, then press Enter and answer the
   questions (GitHub.com, HTTPS, yes, browser). Then run `gh auth setup-git`.
   Check with `gh auth status`.
5. **Name on commits:** if `git config --global user.name` is empty, ask for
   the name and email they want on their project history and set
   `user.name` and `user.email`. (GitHub's private `noreply` email from
   their GitHub settings is fine if they prefer.)
6. **Is KIT a git clone?** `git -C KIT remote -v`. If it is not (they used a
   zip), re-clone the public repo named in `KIT/KIT_REPO` into PROJECTS
   (`git clone https://github.com/<KIT_REPO>`) so `/update-kit` works later.

## Step 3 of 7: Install the kit's way of working

Explain: this teaches every future Claude session on this Mac the kit's
rules, commands and helpers. Then:

- Install `KIT/cy/USER-CLAUDE.md` as **`~/.claude/CLAUDE.md`**. Claude Code
  loads this user-level file in every project. If it exists, read it, show
  the difference and merge in the kit's rules, keeping everything already
  there, especially "Our own rules". The kit's part sits between the
  `cy-maker-kit:start` and `cy-maker-kit:end` markers; keep the markers. Resolve any conflict with them; never
  overwrite existing rules. Create the file only if it is missing.
- Copy each folder in `KIT/.claude/skills/` into `~/.claude/skills/` (one
  folder at a time, so nothing nests). If a skill of the same name exists and
  is not from this kit, skip it and tell them.
- Copy each file in `KIT/.claude/agents/` into `~/.claude/agents/` (same rule).
- Copy `KIT/cy`, `KIT/knowledge`, `KIT/packs`, `KIT/templates`, `KIT/tools` and
  `KIT/KIT_REPO` into `~/.claude/maker-kit/`, and write the full path of KIT
  into `~/.claude/maker-kit/KIT_PATH`. Merge with existing kit files and
  keep local lessons; never replace the whole shared folder.
- Offer to add `"Read(~/.claude/maker-kit/**)"` to `permissions.allow` in
  `~/.claude/settings.json` (merge into what is there; create the file if
  missing) so every session can read the kit without asking. Explain that is
  all it allows.
- Read `KIT/cy/ETHOS.md` and `KIT/cy/MODELS.md` now: they are how you work
  from here.
- **Model and effort**, from their plan (step 1):
  - Max: in the app's model menu choose Opus for the main session; helpers
    stay as shipped.
  - Pro or not sure: Sonnet for the main session, effort medium; change
    `effort: xhigh` to `effort: high` in `~/.claude/agents/maker-engineer.md`
    and `maker-checker.md`.
  Tell them in two lines what that means: the strongest model thinks and
  talks with them, cheaper helpers do the long jobs.

## Step 4 of 7: Tools for the first project

Install only what their first project needs, nothing more:

- **Electronics (ESP32, Arduino and similar boards):** read
  `KIT/packs/hardware/SETUP.md` and follow it (build tools, plug test). It
  ends with the board found on a port.
- **Software (an app, a website, a script):** pick the simplest standard
  stack for it, say why in one line, and install only its runtime (on a Mac,
  prefer user-level installers: `uv` for Python, `fnm` or the Node site's
  install script for Node; ask first and say if anything needs their Mac
  password).
- **Anything else** (a design, a plan, writing, home automation): usually
  nothing to install. Say so and move on.

A tool you just installed may not be on this session's PATH: prefix
commands with `export PATH="$HOME/.local/bin:$PATH"; `.

## Step 5 of 7: First project

Use the `new-project` skill in `PROJECTS/<a short name>` (never inside KIT).
It asks what kind of project it is and picks the template:
- electronics: the ESP32 starter, then follow `KIT/packs/hardware/SETUP.md`'s
  "first blink" part (tests, build, upload, SELFTEST PASS, the LED blinks);
- anything else: the basic template, then the smallest first result they
  can see (a page that opens, a script that prints, a first sketch of the
  plan, a first paragraph).

Fill in `NOTES.md` with what was actually seen working, commit, create the
private GitHub repo and confirm the push (`new-project` does this once).

Celebrate a little. It's their first working step.

## Step 6 of 7: How to work from now on

Walk them through it like a friend showing them their workshop. Short, one
topic per message, and ask if they want more on any of them:

1. **A normal session:** open the Code tab on a project's folder, type
   `/architect` (where things stand, what's next), work on the project with
   Claude, and finish with `/wrap` (notes, save, push to GitHub). New task =
   new session; the notes carry over.
2. **The commands:** type `/` to see them. Day to day: `/architect`,
   `/plan-project` (anything bigger than an afternoon), `/new-project`,
   `/test`, `/check`, `/wrap`, `/guide` (explains anything again),
   `/update-kit`. Electronics projects add `/flash`, `/hw-debug` and
   `/wiring-check`.
3. **Who decides what:** Claude decides the technical how and tells them
   why; they decide money, safety, what gets installed, and what the project
   is for. Claude gives one recommendation, not a menu.
4. **Helpers:** the main session hands long jobs to `maker-engineer`,
   reviews to `maker-checker` and reading to `maker-researcher`, on cheaper
   models. They don't manage them.
5. **Notes that make Claude smarter:** `NOTES.md`, `PITFALLS.md`,
   `DECISIONS.md` in every project. When Claude does something they don't
   like, they say so once and it goes into "Our own rules" in
   `~/.claude/CLAUDE.md`.
6. **Auto mode:** keep sessions on Auto; Claude stops on its own for
   anything risky. If it asks about deleting or installing, read the line.
7. **Safety:** secrets (passwords, keys) never go in git; back up data
   before changing it. Electronics projects carry their own safety rules.

## Step 7 of 7: Done

Summarise in five lines what is installed and where their first project is
on GitHub (the repo URL). Suggest what to do next in that project, or ask
what else they'd like to make. Offer `/plan-project` in a new session for
anything bigger than an afternoon.
