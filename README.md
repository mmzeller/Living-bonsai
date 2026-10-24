# Living Bonsai

A trident maple that lives on the real calendar. It keeps growing while the app is closed, buds open when they would on a real tree, and spring arrives when it does outside. Wire, prune, pinch and defoliate it over the seasons, working toward fine ramification.

**Play:** https://mmzeller.github.io/living-bonsai/

Anyone who opens the link gets their own trees. Nothing is shared between people.

## Install it like an app

- **iPhone or iPad:** open the link in Safari, tap the Share button, then **Add to Home Screen**.
- **Mac:** in Safari, choose **File → Add to Dock**. In Chrome or Edge, use the install button in the address bar.
- **Android:** open the link in Chrome and choose **Add to Home screen**.

After the first visit it works offline.

## Your two trees

- **Real-time tree.** Follows today's date and your local time. It can't be sped up: buds take days or weeks to open, wire takes about two months of growing season to set, and growth stops for winter. There are no shortcuts.
- **Practice tree.** A separate tree for learning and experimenting. Its clock can run at Steady (a garden week per day), Quick (a week per hour) or Time-lapse (a week every 20 seconds).

Switch between them in the menu under **Your trees**.

## Tools

- **Prune:** swipe across a branch to cut it. Buds near the cut wake and push new shoots.
- **Pinch:** tap a glowing shoot tip in spring or summer to stop it, so buds lower down grow instead.
- **Wire:** tap a branch to wire its whole length, then drag from any joint to bend it there, **Up / down** or **Side to side**. Thick wood bends less and can crack or snap. Wire sets in about two months of growing season and bites into the bark if left on too long. **Focus** fades the rest of the tree and colors the selected branch by order: primary, secondary, tertiary.
- **Leaves:** pluck single leaves, drag to pluck several, or defoliate 25%, 50%, 75% or all of the tree. In early summer a strong tree answers with a new flush of smaller leaves.
- **Water:** the soil dries faster in summer. A dry tree stops growing and its leaves scorch.

Drag across the tree to turn it, drag down to look from above, and pinch to zoom. Pick the side you like best and make it the front.

**Ramification** in the header counts how many times each primary branch has divided into fine twigs: 3 means about 8 twigs per branch, 5 about 32.

## Back up and move

**Menu → Back up and move → Export trees** saves both trees to a file. **Import a backup** on another device or browser brings them over. A real-time tree can only be restored as a real-time tree, and any time that passed since the backup plays out when you import it.

## Sync between devices

**Menu → Sync between devices → Turn on sync** shows a private code. Enter it on your other devices with **Join**. There are no accounts. The code decides where your trees are stored, and they're encrypted on your device before they're sent, so the database only ever holds scrambled data. Keep the code private: anyone who has it can see and change your trees.

Sync appears in the menu once the site's Firebase project is set up (below).

## Setting up sync (site owner, one time)

1. In the [Firebase console](https://console.firebase.google.com), create a project for Living Bonsai, or open an existing one.
2. Open **Firestore Database** and click **Create database** if there isn't one (production mode, any location).
3. Open **Firestore Database → Rules** and add the block from [`firestore.rules`](firestore.rules) inside `match /databases/{database}/documents { … }`, then click **Publish**. For a new project, paste the whole file.
4. Open **Project settings → Your apps**. Add a web app if there isn't one (the `</>` button), then copy its `firebaseConfig`.
5. Paste the config into [`firebase-config.js`](firebase-config.js) in place of `null`, and commit.

The config isn't a secret. The rules decide what anyone can read or write: trees can only be fetched by someone holding their code, the collection can't be listed, and each upload is size-limited.

## Development

The whole app is one page, `source/app.html`. The same page also runs inside Claude as an artifact.

```
python3 source/build.py
```

builds `index.html` for the web from it: home-screen app tags, the manifest, the Firebase config and the offline service worker. Edit `source/app.html`, run the build, and commit both.
