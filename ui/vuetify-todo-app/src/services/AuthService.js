import axios from "axios";
import HttpStatus from "../shared/HttpStatus"

const usernameRegex = /^\w{3,16}$/
const emailRegex = /^.{1,50}@.{1,25}\..{1,25}$/

export default {
  current: null,

  loadCurrent() {
    axios.get("auth/current-user", {withCredentials: true})
      .then(r => {
        if (r.status === HttpStatus.OK) {
          this.current = r.data
        }
      })
      .catch(e => console.log(e));
  },

  signIn(email, password) {
    return axios.post("auth/sign-in", {email, password})
      .then(r => {
        this.current = r.data;
        return r.data;
      });
  },

  signUp(username, email, password) {
    return axios.post("auth/sign-up", {username, email, password})
      .then(r => {
        this.current = r.data;
        return r.data;
      });
  },

  signOut() {
    return axios.post("auth/sign-out")
      .then(() => this.current = null)
      .catch(e => console.log(e))
  },

  usernameRules: [
    v => usernameRegex.test(v) || 'Username has wrong format'
  ],

  emailRules: [
    v => emailRegex.test(v) || 'Email has wrong format'
  ],

  passwordRules: [
    v => (v.length >= 7 && v.length <= 75) || 'Password has wrong format'
  ]
}