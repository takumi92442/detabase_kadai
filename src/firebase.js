// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore} from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAZRbG5u5FIYOCvcYi0PY5A3bub8p1B0jQ",
  authDomain: "database-86fcc.firebaseapp.com",
  projectId: "database-86fcc",
  storageBucket: "database-86fcc.appspot.com",
  messagingSenderId: "696037603422",
  appId: "1:696037603422:web:13e6ee7757ba817370dccf",
  measurementId: "G-BKYD1TYJE3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const db = getFirestore(app);
const serverTimestamp = () => {
  return new Date();
}

export { db, serverTimestamp};