# Heroku Dyno Switcher V2
<div align=center>

>  🍿[**Main Repo**](https://github.com/tiararosebiezetta/HerokuDynoSwitcher)   |  📡 [**This Repo**](https://github.com/5MysterySD/HerokuDynoSwitcherV2)

</div>

---

## 🔍 Navigation
- <a href="#-description"><b>Description</b></a>
- <a href="#%EF%B8%8F-mechanism"><b>Mechanism</b></a>
- <a href="#%EF%B8%8F-drawbacks"><b>Drawbacks</b></a>
- <a href="#-deployment"><b>Deployment</b></a>
- <a href="#-variables"><b>Variables</b></a>
- <a href="#-improvement"><b>Improvement</b></a>
- <a href="#-credits-and-references"><b>Credits and References</b></a>

---

## 📋 Description
<p>A little python project to make your heroku app alive forever without being concerned about dyno hours. You do not need to bother adding a credit card to get more dyno hours.</p>
<p align="center">
  <a href="https://github.com/5MysterySD/HerokuDynoSwitcherV2/fork">
    <img src="https://img.shields.io/github/forks/5MysterySD/HerokuDynoSwitcherV2?label=HerokuDynoSwitcherV2 Fork &style=social">
    
  </a>
  <a href="https://github.com/5MysterySD/HerokuDynoSwitcherV2">
    <img src="https://img.shields.io/github/stars/5MysterySD/HerokuDynoSwitcherV2?style=social">
  </a>
</p>

<div align=center>

[![](https://img.shields.io/github/repo-size/5MysterySD/HerokuDynoSwitcherV2?color=green&label=Repo%20Size&labelColor=292c3b)](#)
[![](https://img.shields.io/github/commit-activity/m/5MysterySD/HerokuDynoSwitcherV2?logo=github&labelColor=292c3b&label=Github%20Commits)](#)
[![](https://img.shields.io/github/languages/top/5MysterySD/HerokuDynoSwitcherV2?style=flat&logo=python&labelColor=292c3b)](#)
[![](https://img.shields.io/github/last-commit/5MysterySD/HerokuDynoSwitcherV2?style=flat&label=Last%20Commit&labelColor=292c3b&color=important)](#)
[![](https://img.shields.io/badge/Telegram%20Channel-Join-9cf?style=for-the-badge&logo=telegram&logoColor=blue&style=flat&labelColor=292c3b)](https://t.me/FXTorrentz)
[![](https://img.shields.io/badge/Support%20Group-Join-9cf?style=for-the-badge&logo=telegram&logoColor=blue&style=flat&labelColor=292c3b)](https://t.me/+aj0yG0qvAjZiOTNl)

</div>

## ⚙️ Mechanism
<p>The main idea is to use three accounts (yeah, you need 2 of them to make this work and 1 more for 2 Bots to Run Unlimited without Any Dyno Loss) with two same apps and shift the dyno every 1st and 23rd of a month.</p>
<p>There are two methods you can use, No loop and Autoloop.</p>
<p>I recommend you to use no loop method with Github Actions because it's less complicated and less obstructive.</p>
<p>There is a Github Actions workflow that have been set with cron jobs. They will run automatically at 00:00 UTC 1st and 23rd of a month and when they're running, they will switch the dynos respectively between 3 Accounts.<br>
</p>

---

## ⚠️ Drawbacks
- This may make your app restart once more at 1st and 15th of the month though (besides the usual 24h restart in heroku free tier).
- You need to deploy to both apps at first, and whenever there's a change you want to make to the app, you need to deploy to both apps too. Patience is really needed for that.
- Only for autoloop method: The primary app's dyno will be automatically activated every 10 minutes for the entire day of 1st of a month and the secondary app's dyno will be automatically activated every 10 minutes for the entire day of 15th of a month. That will be bad for you when you don't want to activate the dynos at those certain days. Deactivate this script first before doing that.
- Heroku API will be called more at 1st and 15th of a month with this script. At least, there'll be 18 API calls per hour per acc. It's not that many and it's acceptable, but please note this if you are planning to use heroku API calls.

---

## 🚀 Deployment

<h4>What to do first?</h4>
You need to deploy two similar apps to one heroku account and two individuals in two individual Heroku Accounts. If the day you deploy this script is under 15th (in UTC), only enable the dyno of the app in the first acc. If it's 15th or more than that (in UTC), only enable the dyno of the app in the second acc. Otherwise, the script won't run well in the first month (the next month will be adjusted correctly automatically).
<br>
<h4>Where to deploy this?</h4>

| Platform                                | Method   | Deployment                                                                                                                       | Notes                                                                                                                                                                                                                                                                       |
|-----------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Github Actions<br> <i>(Recommended)</i> | No Loop  | <a href="https://github.com/5MysterySD/HerokuDynoSwitcherV2/blob/master/gh-actions-tutorial.md">Deploy to GH Actions</a>         | Recommended deployment platform as "No loop" method won't be intrusive.                                                                                                                                                                                                     |

---

## 📊 Variables
<h4>Required Variables</h4>

| ℹ️ Put All AppNames, API Keys in Repective Vars Separated By Space, Put the Things in Chronological Order in Each Var, Code is Made like that Else will Not Work !!
| ---

- `A_APPNAME` is the app names of your Primary apps in 1st Accounts.<br>
- `A_APIKEY` is the API keys of the heroku accounts your primary app is in. Check it in your heroku settings, in the last of the page.<br>
- `B_APPNAME` is the app names of your Secondary apps in 2nd Accounts.<br>
- `B_APIKEY` is the API keys of the heroku accounts your secondary apps is in. Check it in your heroku settings, in the last of the page.<br>
- `PROCESSTYPE` is the process type of your app, you can use `web`, `worker` or something else. Check it in the Resources tab of your heroku app.<br>
- `C_APIKEY` is the API key of the heroku account your Tertiary apps is in. Check it in your heroku settings, in the last of the page.<br>
- `CA_APPNAME` is the 1st app names of your Tertiary apps in 3nd Accounts.<br>
- `CB_APPNAME` is the 2st app names of your Tertiary apps in 3nd Accounts.<br>

---

## 🌞 Improvement
If you have time, check this code in `script.py` for Autoloop method and `script_noloop.py` for No loop method, report any error in Issues, and do pull request. That will be highly appriciated.

---

## 📝 Credits and References
- <a href="https://github.com/5MysterySD">5MysterySD </a> [ For Modified V2 Script ] with More Features !!
- <a href="https://github.com/tiararosebiezetta">Katarina (tiararosebiezetta)</a> who happened to have written this very little and simple script (<a href="https://t.me/katarina_ox">Her telegram</a> and <a href="https://t.me/katarina_novi">Her another telegram acc</a>)
- https://pypi.org/project/heroku3/ for allowing us using heroku API with python
- Many userbot repos that for how heroku3 module works
- <a href="https://github.com/ZekXtreme">@ZekXtreme</a> for Github Actions deployment concept
- And many others that I can't say all of them here

---
