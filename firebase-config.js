// Sync between devices. Paste the web app config from the Firebase project that holds
// Living Bonsai's synced trees (Firebase console → Project settings → Your apps → firebaseConfig).
// While this is null, the app works fully on each device and the sync section stays hidden.
// The config is not a secret: who can read and write what is decided by firestore.rules.
window.LB_FIREBASE = null;
