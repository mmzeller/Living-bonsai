# Living Bonsai

Bonsai that live on the real calendar. They keep growing while the app is closed, buds open when they would on a real tree, and spring arrives when it does outside. Keep a bench of trident maples and Japanese black pines, and wire, prune and refine them over the seasons, working toward fine ramification.

**Play:** https://mmzeller.github.io/Living-bonsai/

Anyone who opens the link gets their own trees. Nothing is shared between people.

## Install it like an app

- **iPhone or iPad:** open the link in Safari, tap the Share button, then **Add to Home Screen**.
- **Mac:** in Safari, choose **File → Add to Dock**. In Chrome or Edge, use the install button in the address bar.
- **Android:** open the link in Chrome and choose **Add to Home screen**.

After the first visit it works offline.

## Your bench

Keep up to eight trees. **Menu → Your bench → Add a tree**, then pick a species and a clock:

- **Real time.** Follows today's date and your local time. It can't be sped up: buds take days or weeks to open, wire takes months of growing season to set, and growth stops for winter. There are no shortcuts.
- **Practice.** For learning and experimenting. Its clock can run at Steady (a garden week per day), Quick (a week per hour) or Time-lapse (a week every 20 seconds).

Tap a tree in the list to switch to it. **Settings → Remove** takes the tree you're looking at off the bench.

## Species

- **Trident maple** (*Acer buergerianum*). Deciduous. Buds back readily after cutting, and answers pinching, pruning and defoliation with fine twigs.
- **Japanese black pine** (*Pinus thunbergii*). Evergreen, with one flush of growth a year. Buds set at the shoot tips in late summer open as candles in spring, with spare buds making a whorl. Needles live about three years, and the oldest yellow and drop in autumn. Pines don't bud back on bare wood, so a branch with no needles left dies. Wire takes longer to set than on a maple.

## Tools

- **Prune:** swipe across a branch to cut it. On a maple, buds near the cut wake and push new shoots.
- **Pinch** (maple): tap a glowing shoot tip in spring or summer to stop it, so buds lower down grow instead.
- **Candles** (pine): the tool follows the pine's year. In spring, tap an extending candle to pinch it. From early June to late July, decandle: cut this year's candles, one at a time or with **Decandle strong areas** and **Decandle all**, and a strong tree pushes a shorter second flush with shorter needles. From late summer through winter, reduce each tip to two buds, one at a time or with **Keep two buds**.
- **Wire:** tap a branch to wire its whole length, then drag from any joint to bend it there, **Up / down** or **Side to side**. Thick wood bends less and can crack or snap. Wire sets in about two months of growing season and bites into the bark if left on too long. **Focus** fades the rest of the tree and colors the selected branch by order: primary, secondary, tertiary.
- **Leaves** (maple): pluck single leaves, drag to pluck several, or defoliate 25%, 50%, 75% or all of the tree. In early summer a strong tree answers with a new flush of smaller leaves.
- **Needles** (pine): pull needles by tapping or dragging, **Pull old needles** so light reaches the inner buds, or **Thin strong areas** so weaker shoots catch up next spring. Pulled needles don't grow back.
- **Water:** the soil dries faster in summer. A dry tree stops growing and its leaves scorch.

Drag across the tree to turn it, drag down to look from above, and pinch to zoom. Pick the side you like best and make it the front.

**Ramification** in the header counts how many times each primary branch has divided into fine twigs: 3 means about 8 twigs per branch, 5 about 32.

## Back up and move

**Menu → Back up and move → Export trees** saves every tree on your bench to a file. **Import a backup** on another device or browser brings them over: trees already on that bench are replaced and new ones are added. A real-time tree can only be restored as a real-time tree, and any time that passed since the backup plays out when you import it.

## Sync between devices

**Menu → Sync between devices → Turn on sync** shows a private code. Enter it on your other devices with **Join**. There are no accounts. The code decides where your trees are stored, and they're encrypted on your device before they're sent, so the database only ever holds scrambled data. Keep the code private: anyone who has it can see and change your trees.

Sync appears in the menu once the site's Firebase project is set up (below).

## Setting up sync (site owner, one time)

1. In the [Firebase console](https://console.firebase.google.com), create a project for Living Bonsai, or open an existing one.
2. Open **Firestore Database** and click **Create database** if there isn't one (production mode, any location).
3. Open **Firestore Database → Rules** and add the block from [`firestore.rules`](firestore.rules) inside `match /databases/{database}/documents { … }`, then click **Publish**. For a new project, paste the whole file. (If you set this up before version 0.8, publish the rules again: they now allow more than two trees.)
4. Open **Project settings → Your apps**. Add a web app if there isn't one (the `</>` button), then copy its `firebaseConfig`.
5. Paste the config into [`firebase-config.js`](firebase-config.js) in place of `null`, and commit.

The config isn't a secret. The rules decide what anyone can read or write: trees can only be fetched by someone holding their code, the collection can't be listed, and each upload is size-limited.

## Development

The whole app is one page, `source/app.html`. The same page also runs inside Claude as an artifact.

```
python3 source/build.py
```

builds `index.html` for the web from it: home-screen app tags, the manifest, the Firebase config and the offline service worker. Edit `source/app.html`, run the build, and commit both.
